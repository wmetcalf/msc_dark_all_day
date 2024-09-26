#!/bin/python3
import io
import re
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


class MSCParser:
    def __init__(self, filename, clsid_map_filename=None):
        try:
            with open(filename) as f:
                self.soup = BeautifulSoup(f, "xml")
        except Exception as e:
            raise InvalidMSCFile from e

        if not bool(self.soup.find("MMC_ConsoleFile")):
            raise InvalidMSCFile

        self.urls = set()
        self.url_extractor = URLExtract()

        self.mime = magic.Magic(mime=True)

        self.clsid_map = {}
        self.clsid_nsi_re = re.compile(r"@(?P<dll_path>(?:[^,\x5c]*[\x5c]+)*)(?P<dll_name>[^,\x5c]+?),-(?P<str_id>[0-9]+)")
        if clsid_map_filename:
            with open(clsid_map_filename) as clsid_map_file:
                self.clsid_map = json.load(clsid_map_file)

        self.pem_wrapper_re = re.compile(r"^\s*-----BEGIN\s[^-]{0,256}-----(?P<binary>[A-Za-z0-9+/=\s]+)-----END\s[^-]{0,256}-----\s*$")

    def dump(self, output_dir, output_json, disable_image_hashes=False):
        os.makedirs(output_dir, exist_ok=True)
        self.dump_binaries(output_dir, disable_image_hashes)
        self.load_strings()

        data = {
            "urls": list(self.urls),
            "strings": list(self.strings.values()),
            "tasks": self.parse_tasks(),
            "nodes": self.parse_nodes(),
            "icons": self.parse_icons(),
            "binaries": list(b for i, b in self.binaries.items() if i not in self.used_binaries),
        }

        with open(os.path.join(output_dir, output_json), "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

    def extract_urls(self, string):
        try:
            found_urls = self.url_extractor.find_urls(string)
            self.urls.update(found_urls)
        except Exception as e:
            print(f"Error Extracting URLs: {e}")

    def dump_binaries(self, output_dir, disable_image_hashes=False):
        self.binaries = {}
        self.used_binaries = set()

        binary_storage = self.soup.find("BinaryStorage")
        if not binary_storage:
            return

        for i, binary in enumerate(binary_storage.find_all("Binary", string=True)):
            try:
                binary_string = binary.string
                if all(x in binary_string for x in ["-----BEGIN ", "-----END "]):
                    match = self.pem_wrapper_re.match(binary_string)
                    if match:  # remove PEM wrapper
                        binary_string = match.group("binary")

                binary_data = base64.b64decode(binary_string)
                self.binaries[i] = {"filename": os.path.join(output_dir, f"binary_{i}")}

                # special handling for ImageList
                if binary_data.startswith(b"IL"):
                    il_header = binary_data[:28]
                    binary_data = binary_data[28:]
                    try:
                        self.binaries[i]["image_list"] = []
                        for j, il_image in enumerate(self.process_image_list(il_header, binary_data)):
                            image = {"filename": os.path.join(output_dir, f"binary_{i}_image_{j}.bmp")}
                            il_image.save(image["filename"])
                            with open(image["filename"], "rb") as image_file:
                                image_data = image_file.read()
                                image["sha256"] = hashlib.sha256(image_data).hexdigest()
                                image["sha1"] = hashlib.sha1(image_data).hexdigest()
                                image["md5"] = hashlib.md5(image_data).hexdigest()
                                image["mime_type"] = self.mime.from_buffer(image_data)
                            if not disable_image_hashes:
                                try:
                                    image["ahash"] = str(imagehash.average_hash(il_image))
                                    image["dhash"] = str(imagehash.dhash(il_image))
                                    image["phash"] = str(imagehash.phash(il_image))
                                except Exception as e:
                                    print(f"Error Calculating IL Image Hashes: {e}")
                            self.binaries[i]["image_list"].append(image)
                    except Exception as e:
                        print(f"Error Parsing ImageList Header: {e}")

                with open(self.binaries[i]["filename"], "wb") as binary_file:
                    binary_file.write(binary_data)

                self.binaries[i]["sha256"] = hashlib.sha256(binary_data).hexdigest()
                self.binaries[i]["sha1"] = hashlib.sha1(binary_data).hexdigest()
                self.binaries[i]["md5"] = hashlib.md5(binary_data).hexdigest()

                self.binaries[i]["mime_type"] = self.mime.from_buffer(binary_data)
                if self.binaries[i]["mime_type"].startswith("image/") and not disable_image_hashes:
                    try:
                        image = Image.open(self.binaries[i]["filename"])
                        self.binaries[i]["ahash"] = str(imagehash.average_hash(image))
                        self.binaries[i]["dhash"] = str(imagehash.dhash(image))
                        self.binaries[i]["phash"] = str(imagehash.phash(image))
                    except Exception as e:
                        print(f"Error Calculating Image Hashes: {e}")

            except Exception as e:
                print(f"Error Extracting Binary Data: {e}")

    def process_image_list(self, il_header, il_data):
        header = struct.unpack_from("<2s6HL5H", il_header)
        if header[0] != b"IL":
            raise ValueError("IL header missing")

        # version_major = header[1] >> 8
        # version_minor = header[1] & 0xFF
        current_images = header[2]
        maximum_images = header[3]
        # grow_by_images = header[4]
        image_width = header[5]
        image_height = header[6]
        # bg_color = header[7]
        # flags = header[8]
        # # overlays index starts from one, not zero
        # overlay_1 = header[9]
        # overlay_2 = header[10]
        # overlay_3 = header[11]
        # overlay_4 = header[12]

        il_image = Image.open(io.BytesIO(il_data))
        if (image_width * maximum_images, image_height) != il_image.size:
            raise ValueError("IL size not matching")

        return list(il_image.crop((image_width * i, 0, image_width * (i + 1), image_height)) for i in range(current_images))

    def get_binary(self, tag):
        i = int(tag.get("BinaryRefIndex"))
        self.used_binaries.add(i)
        return self.binaries[i]

    def load_strings(self):
        self.strings = {}
        for st in self.soup.find_all("StringTable"):
            for s in st.find_all("String", {"ID": True}, string=True):
                try:
                    self.strings[int(s["ID"])] = s.string
                    self.extract_urls(s.string)
                except Exception as e:
                    print(f"Error Extracting Strings: {e}")

    def get_string(self, parent_tag, string_name):
        string_tag = parent_tag.find("String", {"Name": string_name}, recursive=False)
        if not string_tag:
            return ""

        if string_tag.get("Value"):
            return string_tag["Value"]

        if string_tag.get("ID"):
            return self.strings.get(int(string_tag["ID"]), "")

        return ""

    def get_clsid_info(self, clsid):
        clsid = clsid.strip()
        if clsid[0] == "{" and clsid[-1] == "}":
            clsid = clsid[1:-1]

        # we might want to make this a case-insensitive dict
        raw_info = self.clsid_map.get(clsid.upper(), {})

        info = {}
        name = raw_info.get("NameString")
        if name:
            info["name"] = name

        match = self.clsid_nsi_re.match(raw_info.get("NameStringIndirect", ""))
        if match:
            info["dll_path"] = match.group("dll_path")
            info["dll_name"] = match.group("dll_name")
            info["str_id"] = match.group("str_id")

        return info

    def parse_tasks(self):
        out_tasks = []
        for console_taskpad in self.soup.find_all("ConsoleTaskpad"):
            for task in console_taskpad.find_all("Task", {"Type": "CommandLine"}):
                try:
                    command = task.get("Command", "")
                    params = task.find("CommandLine").get("Params", "")
                    self.extract_urls(params)
                    full_command = f"{command} {params}"
                    task_name = self.get_string(task, "Name")
                    task_description = self.get_string(task, "Description")

                    images = []
                    for symbol in task.find_all("Symbol"):
                        for image in symbol.find_all("Image"):
                            try:
                                images.append(self.get_binary(image))
                            except Exception as e:
                                print(f"Error Extracting Console Task Images: {e}")

                    out_tasks.append(
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

        return out_tasks

    def parse_nodes(self):
        scope_tree = self.soup.find("ScopeTree")
        if not scope_tree:
            return []

        out_nodes = []
        for node in scope_tree.find_all("Node"):
            try:
                node_clsid = node.get("CLSID")
                out_node = {
                    "id": node.get("ID"),
                    "name": self.get_string(node, "Name"),
                    "clsid": node_clsid,
                    "clsid_info": self.get_clsid_info(node_clsid),
                }

                node_bitmaps = node.find("Bitmaps", recursive=False)
                if node_bitmaps:
                    out_node["bitmaps"] = []
                    for nbd in node_bitmaps.find_all("BinaryData"):
                        try:
                            out_node["bitmaps"].append(self.get_binary(nbd))
                        except Exception as e:
                            print(f"Error Extracting Node Bitmap: {e}")

                node_component_datas = node.find("ComponentDatas", recursive=False)
                if node_component_datas:
                    out_node["component_data"] = []
                    for ncd in node_component_datas.find_all("ComponentData"):
                        try:
                            ncd_guid = ncd.find("GUID", string=True).string
                            out_ncd = {"guid": ncd_guid, "guid_info": self.get_clsid_info(ncd_guid)}
                            ncd_stream = ncd.find("Stream")
                            if ncd_stream:
                                out_ncd["stream"] = self.get_binary(ncd_stream)
                            out_node["component_data"].append(out_ncd)
                        except Exception as e:
                            print(f"Error Extracting Node Component Data: {e}")

                node_components = node.find("Components", recursive=False)
                if node_components:
                    out_node["components"] = []
                    for nc in node_components.find_all("Component"):
                        try:
                            nc_guid = nc.find("GUID", string=True).string
                            out_nc = {"guid": nc_guid, "guid_info": self.get_clsid_info(nc_guid)}
                            nc_storage = nc.find("Storage")
                            if nc_storage:
                                out_nc["storage"] = self.get_binary()
                            out_node["components"].append(out_nc)
                        except Exception as e:
                            print(f"Error Extracting Node Component: {e}")

                out_nodes.append(out_node)
            except Exception as e:
                print(f"Error Extracting Scope Tree Nodes: {e}")

        return out_nodes

    def parse_icons(self):
        visual_attributes = self.soup.find("VisualAttributes")
        if not visual_attributes:
            return []

        out_icons = []
        for icon in visual_attributes.find_all("Icon"):
            out_icon = {
                "icon_index": icon.get("Index"),
                "icon_file": icon.get("File"),
                "images": [],
            }
            for image in icon.find_all("Image"):
                try:
                    out_icon["images"].append(self.get_binary(image))
                except Exception as e:
                    print(f"Error Extracting Icon Image: {e}")
            out_icons.append(out_icon)
            self.extract_urls(out_icon["icon_file"])

        return out_icons


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract CommandLine tasks and images from MSC file")
    parser.add_argument("--no-image-hashes", action="store_true", default=False, help="Do not include image hashes in the output")
    parser.add_argument("--clsid-map", default=None, help="Filename for loading map of CLSID")
    parser.add_argument("--input", required=True, help="Path to the input MSC file")
    parser.add_argument("--output", required=True, help="Path to the output directory")

    args = parser.parse_args()
    try:
        print("https://www.youtube.com/watch?v=ZLVwPZOW4iA")
        msc = MSCParser(args.input, args.clsid_map)
        msc.dump(args.output, "msc_dark_all_day.json", args.no_image_hashes)
        print(f"Commands, nodes, strings, images, files, json, all the MSC things have been saved to: {args.output}")
    except InvalidMSCFile:
        print("Give Me AN MSC File and Ill Darken Your Day!")
