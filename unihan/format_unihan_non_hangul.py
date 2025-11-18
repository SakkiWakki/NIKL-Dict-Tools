import json

with open("hanjareadings.json", "r", encoding="utf-8") as f:
    hanjareadings = json.load(f)

with open("semanticvariants.json", "r", encoding="utf-8") as f:
    variant_to_hanja = json.load(f)

out = {}
for v, c in variant_to_hanja.items():
    if v not in hanjareadings:
        out[v] = c

print(len(hanjareadings), len(variant_to_hanja), len(out))

with open("variantreplacements", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
