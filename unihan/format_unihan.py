
import json

with open("unihan.json", "r", encoding="utf-8") as f:
    data = json.load(f)

out = {}

for entry in data:
    ch = entry["char"]

    readings = entry.get("kHangul", [])
    if not readings:
        continue

    # Keep only the first reading (would be nice is it is also the most common reading)
    sanitized = readings[0].split(":")[0]
    out[ch] = sanitized

with open("hanjareadings.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)