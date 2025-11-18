# Simple non-optimal greedy algorithm for glossing Hanja strings with Hangul.
# May have some errors in practice,
# e.g. if two hanja compound boundaries actually have a irregular phonologic reading
#      when together in practice, or if singular character has multiple readings
# Also not optimal for some long compounds e.g. 生殺與奪權

import re
import json

hanja2hangulpath = './processed/OKHC_processed/news.jsonl'
# inp = "金雨英"
HANJA_ONLY_RE = re.compile(
    r'['
    r'\u3400-\u4DBF'
    r'\u4E00-\u9FFF'
    r'\U00020000-\U0002A6DF'
    r'\U0002A700-\U0002EBEF'
    r'\U00030000-\U000323AF'
    r']+'
)

LDELIM = "("
RDELIM = ")"

def greedy_hanja_match(s, data):
    # Greedy on earilest largest compound
    # I suspect that starting from the longest string and decreasing its size
    # might fare better since it would recognize longer compounds more readily
    try: 
        chaser_idx = -1
        runner_idx = 0
        substr = ""
        ret = ""
        s += " " # We need an extra space to trigger a "not in data"
        # print(f'on {s}')
        build_gloss = lambda s : s + LDELIM + data[s] + RDELIM
        while (chaser_idx != runner_idx):
            substr += s[runner_idx]
            if substr not in data:
                seq = s[chaser_idx : runner_idx]
                ret += build_gloss(seq)
                chaser_idx = runner_idx
                substr = s[runner_idx]
            runner_idx = min(len(s) - 1, runner_idx + 1)
            chaser_idx = max(chaser_idx, 0)
        return ret
    except Exception:
        unicode_seq = [f"U+{ord(c):04X}" for c in seq]
        if not unicode_seq:
            raise ValueError(f"Faulting string \"{s}\"")
        raise ValueError(
            f"Faulting String: \"{seq}\"\n"
            f"Full Unicode Sequence: {unicode_seq}"
        )

def single_inp():
    inp = "國家存在의 理由(三)\n辯護士 金雨英\n(三)國家成立의 理由를 法律上 制度에 求하는 學說\n此學說 中에도 國家成立을 家父權에 求하는 說과 契約에 求하는 說과 物權効力에 求하는 說 等이 有하니 (가)血族團體說(即家父權主張)原始時代에 家族이 擴張하야 國家가 成立됨은 洋의 東西을 勿論하고 例外가 無한 現象이라 希臘羅馬는 勿論이요 舊約聖書에도 家族이 國家에 進化하는 狀態를 明暸히 記載하엿도다.\n血族團體主義는 極히 幼稚한 原始時代의 小國家를 說明할 수 有하나 其他國家를 說明키 難하니 大槪 此主義는 臣民이 家父權 即 家父의 生殺與奪權에 絕對로 服從하든 時代의 國家를 說明한 것이라. 此主義下에서는 君主는 萬能이요 人民은 人格과 自由와 財產의 安固와 生命의 保證이 無하엿도다. 然함으로 某獨逸學者가 此說을 評하야「家父權主義는 人民의 全體를 永久히 無能力者로 宣言하는 主義라. 從하야 此主義를 賛同할 者도 精神能力이 無한 者에 不外하리라 하엿나니라. 此主義의 第二의 欠點은 絕對的 排他主義를 惹起함이니 此主義에 依하면 始祖를 同一하하지 아니하는 他民族이 介在함은 國家存在의 基礎를 破壞할 原因이 될지라. 然하면 此等國家는 絕對的 鎻國主義를 取하야 學問上으로든지 文化上으로든지 排他主義를 實行할밧게 道理가 無하도다.\n今日과 如히 世界主義 人道主義가 우리 人類生活를 支配하랴 하는 時代에 此等學說의 無價値함은 更言할 必要가 無할가 하노라.\n(나)家產國家說\n家產主義는 國家를 物權法上 製作物로 認定하는지라. 換言하면 國家君主의 所有權으로 看做하야 土地가 個人의 所有權의 目的物됨과갓치 國家가 君主의 所有權의 目的物이라 說明하도다.\n古代 君主國은 勿論이오 歐洲 中世의 封建制度時代의 國家는 擧皆 此家產國家主義라 할 것뿐 아니라 今日 國家理論이라도 君主를 統治權의 主體라하고 國家를 統治權의 客體라 하는 學說은 其實質上으로 觀察하면 家產國家主義라 할지라. 然이나 今日의 國家를 論하는 學者中 少數保守派 以外에는 國家를 統治權의 主體된 法人格으로 認定하고 비록 君主國에 在하더래도 君主는 法人인 國家의 機關이란 說에 一致되엿도다.\n(다)國家契約說\n國家의 成立을 個人의 契約에 求하는 說은 希臘 羅馬 猶太時代부터 發生된 것이나 最히 有名한 主張者는 \"릇소|\"라 하노니 即 \"룻소|\"가 主唱한 民約論이 直接으로 佛國革命에 大影響을 與한 故로 자못 後人의 注意를 惹起한 것이르다.\n此說은 \"루소|\"의 著書 民約論中 社會契約章下에 說明하엿스나 其要旨는 \"各人이 其體 其全力을 共同意思 最高指導下에 置하는 同時에 全體에서 分離치 못할 部分 即 團體의 一部分으로 其他位를 保持한다\"하엿나니라.\n從來 此說에 對하야는 非難이 多하엿스나 其非難中에 徃徃히 契約說의 眞義를 誤解한 것도 不無하도다. 民約論에 對한 非難의 一說은 此民約論이 事實과一致치 아니하다는 點이나 然이나 此非難은 事物의 存在와 其存在의 認識을 混同한 誤謬에서 出함이라. 國家成立의 歷史觀과 國家를 如何히 認識하면 其合理性을 正當히 理解할가 하는 것과는 相異한 것이 \"간트\"가 國民이 國家를 形成하는 行爲의 觀念 即 其行爲의 合理를 說明할 수 有한 觀念은 原始的契約에 依하야 國民全體는 國家라 稱하는 共同團體의 一員의 資格으로 다시 自由를 獲得하랴면 한번 自由를 抛棄치 아니치 못하리라 함도 이 合理性을 說明함에 不過하도다.\n契約說에 對한 第二의 非難点은 契約이란 觀念은 法律上 制度라. 即 國家가 有한 後에야 生하는 觀念이라. 故로 此契約으로써 國家成立을 說明하랴 함은 本末顚倒의 說이라 함이나 然이나 契約이란 觀念은 多數의 意思의 合致에서 生함이나 國家가 成立前이라도 多數人이 存在하는 以上에는 契約의 觀念이 生할지지라. 從하야 多數人의 意思가 合致하야 國家를 成立한다 說明할지라도 論理上 矛盾이 無할가 하노라.\n契約說에 對한 第三의 非難은 個人은 元來 自由人이라 其自由가 不可讓일 것이면 個人은 何時라도 此契約을 破毀하리라. 換言하면 만일 個人이 其意思를 變更할 境遇에는 其個人은 其時부터 契約의 拘束을 受치 아니할리니 그러면 其個人은 國家에 對하야 何等 權利義務가 無하리라. 그뿐만 안이라 一人이 國家에셔 脫退할 수 잇스면 多數人도 脫退할지니 脫退한 多數人이 互相結合하야 自由로 契約을 締結함도 得하리라. 그러면 國家成立을 辯護하는 契約論은 結局 國家를 打破하는 結果에 終한다는 非難이라. 然이나 此非難은 離婚이 有함으로 結婚를 攻擊함과 同一하니 人類生活에 男女가 自由意思로 結合하야 夫婦生活을 營|할 必要가 有한 以上에는 自由意思로 離散할 境遇가 有할지라도 此로 因하야 全然 自由意思로 結合한 夫婦制度를 非難할 理由가 無하도다. 그뿐만 아니라 徃徃히 國家가 革命이란 悲境에 處하게 됨은 此連帶的 觀念(契約論 善意的 解釋)에 違反된 施政을 當時 執政者가 取함으로 因한 所以라고 하노라. 然하면 此契約論은 엇던 進步된 國家現衆을 說明할 수 잇다 하겟도다."

    with open(hanja2hangulpath, 'r', encoding='utf-8') as file:
        data = json.load(file)

        h_starts = []
        h_ends = []

        for h_compound in HANJA_ONLY_RE.finditer(inp):
            h_starts.append(h_compound.start())
            h_ends.append(h_compound.end())

        last_e = 0
        cumstr = ""
        for s, e in zip(h_starts, h_ends):
            cumstr += inp[last_e : s]
            cumstr += greedy_hanja_match(inp[s : e], data)
            last_e = e
        cumstr += inp[last_e:]

        print(cumstr)

def mult_inp():
    num = 10
    with open(hanja2hangulpath, 'r', encoding='utf-8') as file:
        with open("hanjareadings.json", 'r', encoding='utf-8') as d:
            inps = json.load(file)
            data = json.load(d)
            for i in range(num):
                inp = inps[i]["text"]

                print("\n====================================================")
                print("Original Input")
                print(inp)
                print()

                try:
                    h_starts = []
                    h_ends = []

                    for h_compound in HANJA_ONLY_RE.finditer(inp):
                        h_starts.append(h_compound.start())
                        h_ends.append(h_compound.end())

                    last_e = 0
                    cumstr = ""
                    for s, e in zip(h_starts, h_ends):
                        cumstr += inp[last_e : s]
                        cumstr += greedy_hanja_match(inp[s : e], data)
                        last_e = e
                    cumstr += inp[last_e:]

                    print("Glossed Output")
                    print(cumstr)
                    print("====================================================\n")
                except Exception as e:
                    print("uhoh stinky! D:")
                    print(f"Error: {e}")    
                

mult_inp()
