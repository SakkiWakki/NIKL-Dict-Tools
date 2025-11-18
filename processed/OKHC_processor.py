import json
import pathlib
import os

def load_info():
    """
    Output:

    range of 1330 years from 695 to 2025: {695, 710, 752, 755, 836, 840, 939, 975, 1019, 1031, 1079, 1145, 1198, 1205, 1216, 1230, 1237, 1259, 1262, 1267, 1270, 1271, 1280, 1281, 1289, 1290, 1292, 1297, 1301, 1305, 1330, 1331, 1332, 1333, 1334, 1336, 1349, 1354, 1355, 1357, 1360, 1361, 1366, 1367, 1371, 1372, 1373, 1376, 1377, 1382, 1383, 1385, 1386, 1387, 1390, 1391, 1392, 1393, 1394, 1395, 1396, 1397, 1398, 1399, 1400, 1401, 1402, 1403, 1404, 1405, 1406, 1407, 1408, 1409, 1410, 1411, 1412, 1413, 1414, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1422, 1423, 1424, 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1432, 1433, 1434, 1435, 1436, 1437, 1438, 1439, 1440, 1441, 1442, 1443, 1444, 1445, 1446, 1447, 1448, 1449, 1450, 1451, 1452, 1453, 1454, 1455, 1456, 1457, 1458, 1459, 1460, 1461, 1462, 1463, 1464, 1465, 1466, 1467, 1468, 1469, 1470, 1471, 1472, 1473, 1474, 1475, 1476, 1477, 1478, 1479, 1480, 1481, 1482, 1483, 1484, 1485, 1486, 1487, 1488, 1489, 1490, 1491, 1492, 1493, 1494, 1495, 1496, 1497, 1498, 1499, 1500, 1501, 1502, 1503, 1504, 1505, 1506, 1507, 1508, 1509, 1510, 1511, 1512, 1513, 1514, 1515, 1516, 1517, 1518, 1519, 1520, 1521, 1522, 1523, 1524, 1525, 1526, 1527, 1528, 1529, 1530, 1531, 1532, 1533, 1534, 1535, 1536, 1537, 1538, 1539, 1540, 1541, 1542, 1543, 1544, 1545, 1546, 1547, 1548, 1549, 1550, 1551, 1552, 1553, 1554, 1555, 1556, 1557, 1558, 1559, 1560, 1561, 1562, 1563, 1564, 1565, 1566, 1567, 1568, 1569, 1570, 1571, 1572, 1573, 1574, 1575, 1576, 1577, 1578, 1579, 1580, 1581, 1582, 1583, 1584, 1585, 1586, 1587, 1588, 1589, 1590, 1591, 1592, 1593, 1594, 1595, 1596, 1597, 1598, 1599, 1600, 1601, 1602, 1603, 1604, 1605, 1606, 1607, 1608, 1609, 1610, 1611, 1612, 1613, 1614, 1615, 1616, 1617, 1618, 1619, 1620, 1621, 1622, 1623, 1624, 1625, 1626, 1627, 1628, 1629, 1630, 1631, 1632, 1633, 1634, 1635, 1636, 1637, 1638, 1639, 1640, 1641, 1642, 1643, 1644, 1645, 1646, 1647, 1648, 1649, 1650, 1651, 1652, 1653, 1654, 1655, 1656, 1657, 1658, 1659, 1660, 1661, 1662, 1663, 1664, 1665, 1666, 1667, 1668, 1669, 1670, 1671, 1672, 1673, 1674, 1675, 1676, 1677, 1678, 1679, 1680, 1681, 1682, 1683, 1684, 1685, 1686, 1687, 1688, 1689, 1690, 1691, 1692, 1693, 1694, 1695, 1696, 1697, 1698, 1699, 1700, 1701, 1702, 1703, 1704, 1705, 1706, 1707, 1708, 1709, 1710, 1711, 1712, 1713, 1714, 1715, 1716, 1717, 1718, 1719, 1720, 1721, 1722, 1723, 1724, 1725, 1726, 1727, 1728, 1729, 1730, 1731, 1732, 1733, 1734, 1735, 1736, 1737, 1738, 1739, 1740, 1741, 1742, 1743, 1744, 1745, 1746, 1747, 1748, 1749, 1750, 1751, 1752, 1753, 1754, 1755, 1756, 1757, 1758, 1759, 1760, 1761, 1762, 1763, 1764, 1765, 1766, 1767, 1768, 1769, 1770, 1771, 1772, 1773, 1774, 1775, 1776, 1777, 1778, 1779, 1780, 1781, 1782, 1783, 1784, 1785, 1786, 1787, 1788, 1789, 1790, 1791, 1792, 1793, 1794, 1795, 1796, 1797, 1798, 1799, 1800, 1801, 1802, 1803, 1804, 1805, 1806, 1807, 1808, 1809, 1810, 1811, 1812, 1813, 1814, 1815, 1816, 1817, 1818, 1819, 1820, 1821, 1822, 1823, 1824, 1825, 1826, 1827, 1828, 1829, 1830, 1831, 1832, 1833, 1834, 1835, 1836, 1837, 1838, 1839, 1840, 1841, 1842, 1843, 1844, 1845, 1846, 1847, 1848, 1849, 1850, 1851, 1852, 1853, 1854, 1855, 1856, 1857, 1858, 1859, 1860, 1861, 1862, 1863, 1864, 1865, 1866, 1867, 1868, 1869, 1870, 1871, 1872, 1873, 1874, 1875, 1876, 1877, 1878, 1879, 1880, 1881, 1882, 1883, 1884, 1885, 1886, 1887, 1888, 1889, 1890, 1891, 1892, 1893, 1894, 1895, 1896, 1897, 1898, 1899, 1900, 1901, 1902, 1903, 1904, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1916, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1926, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1938, 1939, 1940, 1941, 1942, 1943, 1944, 1945, 1946, 1947, 1948, 1949, 1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025}
    10 diff languages: {'Japanese', 'French', 'Modern Korean', 'Korean', 'North Korean', 'Middle Korean', 'Spanish', 'English', 'Hanmun', 'Early Modern Korean'}
    8 diff scripts: {'Hanja, Hangeul', 'Old Hangeul', 'Hanja', 'Hanja, Old Hangeul', 'Hangeul', 'Kanji, Kana', 'Latin', 'Hanja, Latin'}
    27 diff source+corpus: {"'National Institute of Korean History'|'Gaksadeungnok'", "'National Institute of Korean History'|'Diaries of the Royal Secretariat (Seungjeongwon ilgi)'", "'Kyujanggak Institute for Korean Studies'|'The Records of Daily Reflections (Ilseongnok)'", "'Naver News Library & The Dong-A Ilbo'|'Naver News Library'", "'National Institute of Korean History'|'History of the Three Kingdoms (Samguk sagi)'", "'National Institute of Korean History'|'Gaksadeungnok (Modern)'", "'National Library of Korea'|'Korean Newspaper Archive'", "'National Institute of Korean History'|'History of Goryeo (Goryeosa)'", "'The Academy of Korean Studies'|'AKS Royal Court Documents (장서각 기록유산 DB / 왕실고문서)'", "'Naver News Library & The Hankyoreh'|'Naver News Library'", "'Kyujanggak Institute for Korean Studies'|'Kyujanggak Old Documents (규장각 / 고문서)'", "'Korea News Service (조선통신)'|'Korean Central News Agency'", "'The Academy of Korean Studies'|'AKS Hangeul Letters (한국고문서자료관 / 조선시대 한글편지)'", "'The Academy of Korean Studies'|'AKS Old Korean Books (옛한글 원문정보)'", "'Institute for the Translation of Korean Classics'|'Korean Literary Collections'", "'Naver News Library & The Chosun Ilbo'|'Naver News Library'", "'Kim Il Sung University'|'Journal of Kim Il Sung University'", "'National Institute of Korean History'|'Korean Modern and Contemporary Magazines (한국근현대잡지자료)'", "'The Academy of Korean Studies'|'AKS Collection of Old Documents (한국고문서자료관 / 수집고문서)'", "'National Hangeul Museum'|'National Hangeul Museum Archive / Hangeul Documents (국립한글박물관 / 한글 문헌)'", "'National Institute of Korean History'|'Records of the Japanese Legation and Residency-General in Korea (주한일본공사관기록·통감부문서)'", "'Naver News Library & Kyunghyang Shinmun'|'Naver News Library'", "'Kim Il Sung University'|'Kim Il Sung University / Research / Literary Works'", "'National Institute of Korean History'|'Records of the Border Defense Council (Bibyeonsa Deungnok)'", "'Naver News Library & Maeil Business Newspaper'|'Naver News Library'", "'Korea Copyright Commission'|'GongU Madang'", "'National Institute of Korean History'|'Veritable Records of the Joseon Dynasty'"}
    """
    directory = pathlib.Path("OKHC_converted/")

    years = set()
    languages = set()
    scripts = set()
    source_corpus = set()

    for file in directory.glob("*.jsonl"):
        print(f"Loading {file}...")
        with file.open("r", encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                entry = json.loads(line)

                years.add(entry.get("year"))
                languages.add(entry.get("language"))
                scripts.add(entry.get("script"))
                source_corpus.add(f"'{entry.get("source")}'|'{entry.get("corpus")}'")

    years.discard(None)
    print(f"range of {max(years) - min(years)} years from {min(years)} to {max(years)}: {years}")
    print(f"{len(languages)} diff languages: {languages}")
    print(f"{len(scripts)} diff scripts: {scripts}")
    print(f"{len(source_corpus)} diff source+corpus: {source_corpus}")

def make_data():
    SCRIPTS = ('Hanja, Hangeul', 'Old Hangeul', 'Hanja', 'Hanja, Old Hangeul', 'Hangeul')
    SOURCE_CORPUS = {
        "news": [
            ("Naver News Library & The Dong-A Ilbo", "Naver News Library"),
            ("Naver News Library & The Hankyoreh", "Naver News Library"),
            ("Naver News Library & The Chosun Ilbo", "Naver News Library"),
            ("Naver News Library & Kyunghyang Shinmun", "Naver News Library"),
            ("Naver News Library & Maeil Business Newspaper", "Naver News Library"),
            ("National Library of Korea", "Korean Newspaper Archive"),
            ("Korea News Service (조선통신)", "Korean Central News Agency"),
        ],
        "modern_magazines": [
            ("National Institute of Korean History", "Korean Modern and Contemporary Magazines (한국근현대잡지자료)"),
        ],
        "historical_records": [
            ("National Institute of Korean History", "Gaksadeungnok"),
            ("National Institute of Korean History", "Gaksadeungnok (Modern)"),
            ("National Institute of Korean History", "Diaries of the Royal Secretariat (Seungjeongwon ilgi)"),
            ("Kyujanggak Institute for Korean Studies", "The Records of Daily Reflections (Ilseongnok)"),
            ("National Institute of Korean History", "History of the Three Kingdoms (Samguk sagi)"),
            ("National Institute of Korean History", "History of Goryeo (Goryeosa)"),
            ("National Institute of Korean History", "Records of the Japanese Legation and Residency-General in Korea (주한일본공사관기록·통감부문서)"),
            ("National Institute of Korean History", "Records of the Border Defense Council (Bibyeonsa Deungnok)"),
            ("National Institute of Korean History", "Veritable Records of the Joseon Dynasty"),
        ],
        "premodern_documents": [
            ("The Academy of Korean Studies", "AKS Royal Court Documents (장서각 기록유산 DB / 왕실고문서)"),
            ("The Academy of Korean Studies", "AKS Collection of Old Documents (한국고문서자료관 / 수집고문서)"),
            ("The Academy of Korean Studies", "AKS Old Korean Books (옛한글 원문정보)"),
            ("The Academy of Korean Studies", "AKS Hangeul Letters (한국고문서자료관 / 조선시대 한글편지)"),
            ("Kyujanggak Institute for Korean Studies", "Kyujanggak Old Documents (규장각 / 고문서)"),
            ("National Hangeul Museum", "National Hangeul Museum Archive / Hangeul Documents (국립한글박물관 / 한글 문헌)"),
        ],
        "north_korean": [
            ("Kim Il Sung University", "Journal of Kim Il Sung University"),
            ("Kim Il Sung University", "Kim Il Sung University / Research / Literary Works"),
        ],
        "literature_classics": [
            ("Institute for the Translation of Korean Classics", "Korean Literary Collections"),
        ],
        "miscellaneous_archival": [
            ("Korea Copyright Commission", "GongU Madang"),
        ],
    }
    TO_CATEGORY = {}
    for k, l in SOURCE_CORPUS.items():
        for source_corpus in l:
            TO_CATEGORY[source_corpus] = k

    with open("../unihan/semanticvariants.json", "r", encoding="utf-8") as f:
        variant_to_hanja = json.load(f)

    directory = pathlib.Path("OKHC_converted/")

    out = {}
    for k in SOURCE_CORPUS.keys():
        out[k] = []

    for file in directory.glob("*.jsonl"):
        print(f"Loading {file}...")
        with file.open("r", encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                entry = json.loads(line)

                if entry["script"] not in SCRIPTS:
                    continue

                source_corpus = (entry.get("source"), entry.get("corpus"))
                if source_corpus not in TO_CATEGORY:
                    continue

                text = entry["text"]
                if text == "[TEXT REMOVED DUE TO COPYRIGHT]":
                    continue
                newtext = ""
                for c in text:
                    if c in variant_to_hanja:
                        newtext += variant_to_hanja[c]
                    else:
                        newtext += c

                out[TO_CATEGORY[source_corpus]].append({"text":newtext})

    os.makedirs("OKHC_processed", exist_ok=True)
    for category, obj in out.items():
        with open(f"OKHC_processed/{category}.jsonl", "w", encoding="utf-8") as f:
            json.dump(obj, f, ensure_ascii=False)
            f.write("\n")
            print(f"Wrote {category}.jsonl")


make_data()
