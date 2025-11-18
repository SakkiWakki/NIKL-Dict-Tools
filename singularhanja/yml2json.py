import yaml
import json

with open("table.yml", "r", encoding="utf-8") as yml_file:
    data = yaml.safe_load(yml_file)

with open("singularhanja.json", "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=2)
