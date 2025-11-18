import json
import re

# reduce semantic variants by mapping hanja with semantic variants to the "best" hanja

with open("unihan_semantic_variant.json", "r", encoding="utf-8") as f:
    data = json.load(f)

with open("hanjareadings.json", "r", encoding="utf-8") as f:
    hanja_to_hangul = json.load(f)

ucn_to_variants = {}
ucn_to_flags = {}

# for unicode scalar value
unicode_re = re.compile(r'^U\+([0-9A-Fa-f]{4,6})')
# for T/B/Z/F/J flags (could be multiple)
flags_re = re.compile(r":([TBZFJ]+)")
flags_values = {
    "ZF": 0,  # preferred + traditional
    "F": 1,  # traditional
    "Z": 2,  # preferred
}

for entry in data:
    c = entry["char"]
    ucn = int(entry["ucn"][2:], 16)

    ucn_to_variants.setdefault(ucn, set())
    ucn_to_flags.setdefault(ucn, 3)

    readings = entry.get("kSemanticVariant", [])
    if not readings:
        continue

    for reading in readings:
        m = unicode_re.match(reading)
        unicode = m.group(1) if m else None

        if not unicode:
            continue

        unicode = int(unicode, 16)

        ucn_to_variants.setdefault(unicode, set())
        ucn_to_variants[ucn].add(unicode)
        ucn_to_variants[unicode].add(ucn)

        flags = flags_re.findall(reading)
        flags_value = 3
        for flag, value in flags_values.items():
            if flag in flags:
                flags_value = value
                break
        ucn_to_flags.setdefault(unicode, 3)
        ucn_to_flags[unicode] = min(flags_value, ucn_to_flags[unicode])

out = {}
seen = set()
count = 0
for ucn, variants in ucn_to_variants.items():
    if ucn in seen:
        continue

    variants_flags = [(ucn_to_flags[u], u) for u in variants]
    variants_flags.sort()

    for _, variant in variants_flags:
        if chr(variant) in hanja_to_hangul:
            for u in variants|{ucn,}:
                out[chr(u)] = chr(variant)
                seen.add(u)
            break

    print(f"char {chr(ucn)} (ucn {ucn}) :(  had {len(variants)} variants")
    count += 1

print(len(data), len(hanja_to_hangul), count, len(out))

with open("semanticvariants.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
