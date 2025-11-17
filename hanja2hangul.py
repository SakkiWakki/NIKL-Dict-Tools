import os
import re
import json
import xml.etree.ElementTree as ET

in_dirs = ["dicts/krdict", "dicts/opendict", "dicts/stdict"]
out_dir = "out"
out_name = "hanja2hangul.json"
os.makedirs(out_dir, exist_ok=True)

# Instead of sanitizing, should prby consider
# breaking up the hangul based on the internal symbols 
# for better space efficiency 
def sanitize_hangul(s: str) -> str:
    # U+AC00–U+D7A3
    return re.sub(r'[^가-힣]', '', s)

HANJA_RE = re.compile( 
    # This is from my CJKV Folding Fonts project
    r'[^'
    r'\u3400-\u4DBF'              # CJK Extension A
    r'\u4E00-\u9FFF'              # Unified Ideographs
    r'\U00020000-\U0002A6DF'      # Extension B
    r'\U0002A700-\U0002EBEF'      # Extensions C–I
    r'\U00030000-\U000323AF'      # SIP/TIP
    r'\u3006\u3007'               # 〆, 〇
    r'\uFA0E\uFA0F\uFA11\uFA13\uFA14\uFA1F\uFA21\uFA23\uFA24\uFA27\uFA28\uFA29'  # compatibility ideographs
    r'\uFE00-\uFE0F'              # Variation Selectors
    r'\U000E0100-\U000E01EF'      # IVS
    r']'
)
def sanitize_hanja(s: str) -> str:
    # U+AC00–U+D7A3
    return  HANJA_RE.sub('', s)

# Don't explode!!!
out_data = {}

for in_dir in in_dirs:
    print(f"in {in_dir}")
    for name in os.listdir(in_dir):
        print(f"parsing {name}")
        in_path = os.path.join(in_dir, name)
        if not name.endswith(".xml"):
            continue

        tree = ET.parse(in_path)
        root = tree.getroot()

        for item in root.findall("item"):
            word_info = item.find("word_info")
            if word_info is None:
                continue

            word_type = word_info.findtext("word_type")
            if word_type != "한자어":
                continue

            hangul = word_info.findtext("word")
            hangul = sanitize_hangul(hangul)

            hanja = word_info.find("original_language_info/original_language")
            hanja = sanitize_hanja(hanja.text) if hanja is not None else None

            out_data[hanja] = hangul
    print(f'{in_dir} done')
    out_path = os.path.join(out_dir, out_name) 

with open(out_path, "w", encoding="utf-8") as f:
    json.dump(out_data, f, ensure_ascii=False, indent=2)

print("done")