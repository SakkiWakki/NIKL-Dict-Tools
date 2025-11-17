import json

files = ["unihan/hanjareadings.json", "hanja2hangul/hanja2hangul.json"]

combined = {}

for path in files:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
        combined.update(data)  

with open("hanjareadings.json", "w", encoding="utf-8") as f:
    json.dump(combined, f, ensure_ascii=False, indent=2)