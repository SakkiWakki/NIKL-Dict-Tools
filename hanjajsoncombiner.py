import json

# In order of reliability
files = ["hanja2hangul/hanja2hangul.json", "singularhanja/singularhanja.json", "unihan/hanjareadings.json"]

combined = {}

for path in files:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
        combined.update(data)  

with open("hanjareadings.json", "w", encoding="utf-8") as f:
    json.dump(combined, f, ensure_ascii=False, indent=2)