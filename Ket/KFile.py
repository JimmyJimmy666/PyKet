# 导入库
import xml.etree.ElementTree as ET
from .KEngines.KCmdGuiEngine import *
from .KClasses import *
import tomllib
import json
import csv

# 读取文件
def read(path: str | KString, type: str | KString):
    match type:
        case "UTF8":
            with open(path, "r", encoding="UTF8") as file:
                return file.read()
            
        case "CSV":
            with open(path, "r", newline="", encoding="UTF-8") as file:
                return csv.reader(file)
            
        case "JSON":
            with open(path, "r", encoding="UTF-8") as file:
                return json.load(file)
            
        case "XML":
            dict = {}
            root = ET.parse(path).getroot()
            for item in root.findall("item"):
                name = item.find("name").text
                price = item.find("price").text
                dict[name] = price
            return dict
        
        case "TOML":
            with open(path, "rb") as file:
                return tomllib.load(file)

# 写入文件
def write(path: str | KString, text: str | KString, type: str | KString):
    match type:
        case "UTF8":
            with open(path, "w", encoding="UTF8") as file:
                file.write(str(text))
                
        case "CSV":
            with open(path, "w", newline="", encoding="UTF-8") as file:
                writer = csv.writer(file)
                if isinstance(text, list):
                    if all(isinstance(row, list) for row in text):
                        writer.writerows(text)
                    else:
                        writer.writerow(text)
                
        case "JSON":
            with open(path, "w", encoding="UTF-8") as file:
                if isinstance(text, (dict, list)):
                    json.dump(text, file, ensure_ascii=False, indent=2)
                else:
                    json.dump(str(text), file, ensure_ascii=False, indent=2)
                
        case "XML":
            if isinstance(text, dict):
                root = ET.Element("data")
                for key, value in text.items():
                    child = ET.SubElement(root, str(key))
                    child.text = str(value)
                tree = ET.ElementTree(root)
                tree.write(path, encoding="utf-8", xml_declaration=True)
        
        case "TOML":
            printe("$g{waiting for an update}")