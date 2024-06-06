#!/bin/python3
import os
import json
import base64
import argparse
import magic
from bs4 import BeautifulSoup
from urlextract import URLExtract


def validate_msc_file(content):
    soup = BeautifulSoup(content, "xml")
    return bool(soup.find("MMC_ConsoleFile"))


def extract_and_resolve_commandline_tasks_with_images(content, output_dir):
    soup = BeautifulSoup(content, "xml")
    extractor = URLExtract()
    mime = magic.Magic(mime=True)

    string_table = {}
    urls = []
    for string in soup.find_all("String"):
        string_id = string.get("ID")
        string_value = string.text
        string_table[string_id] = string_value
        found_urls = extractor.find_urls(string_value)
        urls.extend(found_urls)

    binary_storage = []
    for binary in soup.find_all("Binary"):
        binary_data = base64.b64decode(binary.text)
        binary_storage.append(binary_data)

    tasks = soup.find_all("Task", {"Type": "CommandLine"})
    commands = []
    used_binaries = set()
    other_binaries = []
    visual_icons = []

    for task in tasks:
        if task.find_parent("ConsoleTaskpad"):
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
                    image_ref_index = int(image.get("BinaryRefIndex"))
                    if image_ref_index < len(binary_storage):
                        # wtf is this header
                        image_data = binary_storage[image_ref_index][28:]
                        image_filename = os.path.join(output_dir, f"image_{image_ref_index}")
                        with open(image_filename, "wb") as image_file:
                            image_file.write(image_data)
                        images.append({"image_ref_id": image_ref_index, "image_filename": image_filename})
                        used_binaries.add(image_ref_index)

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

    visual_attributes = soup.find("VisualAttributes")
    if visual_attributes:
        icons = visual_attributes.find_all("Icon")
        for icon in icons:
            icon_images = []
            for image in icon.find_all("Image"):
                image_ref_index = int(image.get("BinaryRefIndex"))
                if image_ref_index < len(binary_storage) and image_ref_index not in used_binaries:
                    if image_ref_index < len(binary_storage):
                        # wtf is this header
                        image_data = binary_storage[image_ref_index][28:]
                        image_filename = os.path.join(output_dir, f"image_{image_ref_index}")
                        with open(image_filename, "wb") as image_file:
                            image_file.write(image_data)
                        icon_images.append({"image_ref_id": image_ref_index, "image_filename": image_filename})
                        used_binaries.add(image_ref_index)
                elif image_ref_index in used_binaries:
                    for entry in images:
                        if entry.get("image_ref_id") == image_ref_index:
                            image_filename = entry.get("image_filename")
                    icon_images.append({"image_ref_id": image_ref_index, "image_filename": image_filename})
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
            if "image" in mime_type:
                file_path = os.path.join(output_dir, f"other_image_{index}")
            else:
                file_path = os.path.join(output_dir, f"other_binary_{index}.bin")
            with open(file_path, "wb") as file:
                file.write(writeme)
            other_binaries.append(file_path)

    return commands, string_table, urls, other_binaries, visual_icons


def main(input_file, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    print("https://www.youtube.com/watch?v=ZLVwPZOW4iA")
    with open(input_file, "r", encoding="utf-8") as file:
        content = file.read()

    if validate_msc_file(content):
        commands, string_table, urls, other_binaries, visual_icons = extract_and_resolve_commandline_tasks_with_images(content, output_dir)
        json_file_path = os.path.join(output_dir, "msc_dark_all_day.json")
        data = {"commands": commands, "strings": string_table, "urls": urls, "other_binaries": other_binaries, "visual_icons": visual_icons}
        with open(json_file_path, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Commands, strings, images, files, json, all the MSC things have been saved to: {output_dir}")
    else:
        print("Give Me AN MSC File and Ill Darken Your Day!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract CommandLine tasks and images from MSC file")
    parser.add_argument("--input", required=True, help="Path to the input MSC file")
    parser.add_argument("--output", required=True, help="Path to the output directory")

    args = parser.parse_args()
    main(args.input, args.output)
