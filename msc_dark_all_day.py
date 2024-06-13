#!/bin/python3
import os
import json
import base64
import argparse
import magic
import imagehash
import hashlib
import struct
from bs4 import BeautifulSoup
from urlextract import URLExtract
from PIL import Image


class InvalidMSCFile(Exception):
    pass


def calc_hashes(file_path):
    sha256 = hashlib.sha256()
    sha1 = hashlib.sha1()
    md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        buf = f.read()
        sha256.update(buf)
        sha1.update(buf)
        md5.update(buf)
    return sha256.hexdigest(), sha1.hexdigest(), md5.hexdigest()


def parse_imagelist_header(image_header):
    data = struct.unpack_from("<2s6HL5H", image_header)
    if data[0] != b"IL":
        return {}

    return {
        "version": f"{data[1] >> 8}.{data[1] & 0xFF}",
        "current_images": data[2],
        "maximum_images": data[3],
        # "grow_by_images": data[4],
        "image_width": data[5],
        "image_height": data[6],
        "bg_color": f"0x{data[7]:04X}",
        "flags": f"0x{data[8]:02X}",
        # overlays index starts from one, not zero
        "overlay_1": f"0x{data[9]:02X}",
        "overlay_2": f"0x{data[10]:02X}",
        "overlay_3": f"0x{data[11]:02X}",
        "overlay_4": f"0x{data[12]:02X}",
    }


def calc_image_hashes(file_path):
    image = Image.open(file_path)
    phash = str(imagehash.phash(image))
    dhash = str(imagehash.dhash(image))
    ahash = str(imagehash.average_hash(image))
    return phash, dhash, ahash


def extract_and_resolve_commandline_tasks_with_images(content, output_dir):
    soup = BeautifulSoup(content, "xml")
    if not bool(soup.find("MMC_ConsoleFile")):
        raise InvalidMSCFile

    extractor = URLExtract()
    mime = magic.Magic(mime=True)

    string_table = {}
    urls = []
    for st in soup.find_all("StringTable"):
        for string in st.find_all("String", {"ID": True}):
            try:
                string_id = string.get("ID")
                string_value = string.text
                string_table[string_id] = string_value
                if string_value:
                    try:
                        found_urls = extractor.find_urls(string_value)
                        urls.extend(found_urls)
                    except Exception as e:
                        print(f"Error Extracting URLs: {e}")
            except Exception as e:
                print(f"Error Extracting Strings: {e}")

    binary_storage = []
    for binary in soup.find_all("Binary"):
        try:
            binary_data = base64.b64decode(binary.text)
            binary_storage.append(binary_data)
        except Exception as e:
            print(f"Error Extracting Binary Data: {e}")

    tasks = soup.find_all("Task", {"Type": "CommandLine"})
    commands = []
    used_binaries = set()
    other_binaries = []
    visual_icons = []

    for task in tasks:
        if task.find_parent("ConsoleTaskpad"):
            try:
                command = task.get("Command", "")
                params = task.find("CommandLine").get("Params", "")
                task_name_id = task.find("String", {"Name": "Name"}).get("ID")
                task_description_id = task.find("String", {"Name": "Description"}).get("ID")
                task_name = string_table.get(task_name_id, "")
                task_description = string_table.get(task_description_id, "")
                full_command = f"{command} {params}"
                images = []
                for symbol in task.find_all("Symbol"):
                    for image in symbol.find_all("Image"):
                        try:
                            image_ref_index = int(image.get("BinaryRefIndex"))
                            if image_ref_index < len(binary_storage):
                                image_header = binary_storage[image_ref_index][:28]
                                image_data = binary_storage[image_ref_index][28:]
                                image_filename = os.path.join(output_dir, f"image_{image_ref_index}")
                                with open(image_filename, "wb") as image_file:
                                    image_file.write(image_data)
                                try:
                                    il_header = parse_imagelist_header(image_header)
                                except Exception as e:
                                    il_header = {}
                                    print(f"Error Parsing ImageList Header: {e}")
                                sha256, sha1, md5 = calc_hashes(image_filename)
                                phash, dhash, ahash = (None, None, None)
                                mime_type = mime.from_buffer(image_data)
                                if mime_type.startswith("image"):
                                    try:
                                        phash, dhash, ahash = calc_image_hashes(image_filename)
                                    except Exception as e:
                                        print(f"Error Calculating Image Hashes: {e}")
                                images.append(
                                    {
                                        "image_ref_id": image_ref_index,
                                        "image_filename": image_filename,
                                        "imagelist_header": il_header,
                                        "sha256": sha256,
                                        "sha1": sha1,
                                        "md5": md5,
                                        "phash": phash,
                                        "dhash": dhash,
                                        "ahash": ahash,
                                        "mime_type": mime_type,
                                    }
                                )
                                used_binaries.add(image_ref_index)
                        except Exception as e:
                            print(f"Error Extracting Console Task Images: {e}")

                commands.append(
                    {
                        "name": task_name,
                        "description": task_description,
                        "command": command,
                        "params": params,
                        "full_command": full_command,
                        "images": images,
                    }
                )
            except Exception as e:
                print(f"Error Extracting Console Task Commands: {e}")

    visual_attributes = soup.find("VisualAttributes")
    if visual_attributes:
        icons = visual_attributes.find_all("Icon")
        for icon in icons:
            icon_images = []
            for image in icon.find_all("Image"):
                image_ref_index = int(image.get("BinaryRefIndex"))
                if image_ref_index < len(binary_storage) and image_ref_index not in used_binaries:
                    if image_ref_index < len(binary_storage):
                        image_header = binary_storage[image_ref_index][:28]
                        image_data = binary_storage[image_ref_index][28:]
                        image_filename = os.path.join(output_dir, f"image_{image_ref_index}")
                        with open(image_filename, "wb") as image_file:
                            image_file.write(image_data)
                        try:
                            il_header = parse_imagelist_header(image_header)
                        except Exception as e:
                            il_header = {}
                            print(f"Error Parsing ImageList Header: {e}")
                        sha256, sha1, md5 = calc_hashes(image_filename)
                        phash, dhash, ahash = (None, None, None)
                        mime_type = mime.from_buffer(image_data)
                        if mime_type.startswith("image"):
                            try:
                                phash, dhash, ahash = calc_image_hashes(image_filename)
                            except Exception as e:
                                print(f"Error Calculating Image Hashes: {e}")
                        icon_images.append(
                            {
                                "image_ref_id": image_ref_index,
                                "image_filename": image_filename,
                                "imagelist_header": il_header,
                                "sha256": sha256,
                                "sha1": sha1,
                                "md5": md5,
                                "phash": phash,
                                "dhash": dhash,
                                "ahash": ahash,
                                "mime_type": mime_type,
                            }
                        )
                        used_binaries.add(image_ref_index)
                elif image_ref_index in used_binaries:
                    for entry in images:
                        if entry.get("image_ref_id") == image_ref_index:
                            icon_images.append(entry)
            visual_icons.append({"icon_index": icon.get("Index"), "icon_file": icon.get("File"), "images": icon_images})

    for index, binary_data in enumerate(binary_storage):
        if index not in used_binaries:
            data = binary_data[28:]
            writeme = binary_data
            mime_type = mime.from_buffer(writeme)
            if not mime_type.startswith("image"):
                mime_type = mime.from_buffer(data)
                if mime_type.startswith("image"):
                    writeme = data
            phash = None
            dhash = None
            ahash = None
            if mime_type == "application/x-empty" or len(writeme) == 0:
                print(f"Skipping empty binary data at index {index}")
                continue
            if "image" in mime_type:
                file_path = os.path.join(output_dir, f"other_image_{index}")
            else:
                file_path = os.path.join(output_dir, f"other_binary_{index}.bin")
            with open(file_path, "wb") as file:
                file.write(writeme)
            sha256, sha1, md5 = calc_hashes(image_filename)

            if mime_type.startswith("image"):
                try:
                    phash, dhash, ahash = calc_image_hashes(image_filename)
                except Exception as e:
                    print(f"Error Calculating Image Hashes: {e}")
            other_binaries.append(
                {
                    "filename": file_path,
                    "sha256": sha256,
                    "sha1": sha1,
                    "md5": md5,
                    "phash": phash,
                    "dhash": dhash,
                    "ahash": ahash,
                    "mime_type": mime_type,
                }
            )

    return commands, string_table, urls, other_binaries, visual_icons


def main(input_file, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    print("https://www.youtube.com/watch?v=ZLVwPZOW4iA")
    with open(input_file, "r", encoding="utf-8") as file:
        content = file.read()

    try:
        commands, string_table, urls, other_binaries, visual_icons = extract_and_resolve_commandline_tasks_with_images(content, output_dir)
        json_file_path = os.path.join(output_dir, "msc_dark_all_day.json")
        data = {"commands": commands, "strings": string_table, "urls": urls, "other_binaries": other_binaries, "visual_icons": visual_icons}
        with open(json_file_path, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Commands, strings, images, files, json, all the MSC things have been saved to: {output_dir}")
    except InvalidMSCFile:
        print("Give Me AN MSC File and Ill Darken Your Day!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract CommandLine tasks and images from MSC file")
    parser.add_argument("--input", required=True, help="Path to the input MSC file")
    parser.add_argument("--output", required=True, help="Path to the output directory")

    args = parser.parse_args()
    main(args.input, args.output)
