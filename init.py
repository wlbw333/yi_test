# 定义五行类
class WuXing:
    def __init__(self, name):
        self.name = name

# 定义天干类
class TianGan:
    def __init__(self, name, yin_yang, wu_xing):
        self.name = name        # 天干名称（甲、乙、丙、丁等）
        self.yin_yang = yin_yang  # 阴阳（阳、阴）
        self.wu_xing = wu_xing    # 五行（金、木、水、火、土）

# 定义地支类
class DiZhi:
    def __init__(self, name, yin_yang, wu_xing):
        self.name = name        # 地支名称（子、丑、寅等）
        self.yin_yang = yin_yang  # 阴阳（阳、阴）
        self.wux_ing = wu_xing    # 五行（金、木、水、火、土）

# 创建五行实例列表
wu_xing_list = [
    WuXing("木"),
    WuXing("火"),
    WuXing("土"),
    WuXing("金"),
    WuXing("水")
]

# 创建天干实例
tian_gan_list = [
    TianGan("甲", "阳", "木"), TianGan("乙", "阴", "木"),
    TianGan("丙", "阳", "火"), TianGan("丁", "阴", "火"),
    TianGan("戊", "阳", "土"), TianGan("己", "阴", "土"),
    TianGan("庚", "阳", "金"), TianGan("辛", "阴", "金"),
    TianGan("壬", "阳", "水"), TianGan("癸", "阴", "水")
]

# 创建地支实例
di_zhi_list = [
    DiZhi("子", "阳", "水"), DiZhi("丑", "阴", "土"),
    DiZhi("寅", "阳", "木"), DiZhi("卯", "阴", "木"),
    DiZhi("辰", "阳", "土"), DiZhi("巳", "阴", "火"),
    DiZhi("午", "阳", "火"), DiZhi("未", "阴", "土"),
    DiZhi("申", "阳", "金"), DiZhi("酉", "阴", "金"),
    DiZhi("戌", "阳", "土"), DiZhi("亥", "阴", "水")
]

# 定义五行相生关系
wu_xing_sheng_map = {
    "木": "火",  # 木生火
    "火": "土",  # 火生土
    "土": "金",  # 土生金
    "金": "水",  # 金生水
    "水": "木"   # 水生木
}
wu_xing_beisheng_map = {v: k for k, v in wu_xing_sheng_map.items()}

# 定义五行相克关系
wu_xing_ke_map = {
    "木": "土",  # 木克土
    "土": "水",  # 土克水
    "水": "火",  # 水克火
    "火": "金",  # 火克金
    "金": "木"   # 金克木
}
wu_xing_beike_map = {v: k for k, v in wu_xing_ke_map.items()}

# 定义天干之间的合关系（例如：甲和己合）
tian_gan_he_map = {
    "甲": "己", "己": "甲",
    "乙": "庚", "庚": "乙",
    "丙": "辛", "辛": "丙",
    "丁": "壬", "壬": "丁",
    "戊": "癸", "癸": "戊"
}

# 定义地支之间的冲、刑、害、合关系
di_zhi_chong_map = {
    "子": "午", "丑": "未", "寅": "申", "卯": "酉", "辰": "戌", "巳": "亥",
    "午": "子", "未": "丑", "申": "寅", "酉": "卯", "戌": "辰", "亥": "巳"
}
di_zhi_he_map = {
    "子": "丑", "寅": "亥", "卯": "戌", "辰": "酉", "巳": "申", "午": "未",
    "丑": "子", "亥": "寅", "戌": "卯", "酉": "辰", "申": "巳", "未": "午"
}
di_zhi_xing_map = {
    "子": "卯", "丑": "戌", "寅": "巳", "卯": "子",
    "辰": "辰", "巳": "申", "午": "午", "未": "丑",
    "申": "寅", "酉": "酉", "戌": "未", "亥": "亥"
}
di_zhi_beixing_map = {v: k for k, v in di_zhi_xing_map.items()}
di_zhi_hai_map = {
    "子": "未", "丑": "午", "寅": "巳", "卯": "辰", "辰": "卯", "巳": "寅",
    "午": "丑", "未": "子", "申": "亥", "酉": "戌", "戌": "酉", "亥": "申"
}
di_zhi_po_map = {
    "子": "酉", "丑": "辰", "寅": "亥", "卯": "午", "戌": "未", "申": "巳",
    "酉": "子", "辰": "丑", "亥": "寅", "午": "卯", "未": "戌", "巳": "申"
}
di_zhi_sanhe_map = {
    "申": ("水", "申", "子", "辰"),
    "子": ("水", "申", "子", "辰"),
    "辰": ("水", "申", "子", "辰"),
    "水": ("水", "申", "子", "辰"),
    "寅": ("火", "寅", "午", "戌"),
    "午": ("火", "寅", "午", "戌"),
    "戌": ("火", "寅", "午", "戌"),
    "火": ("火", "寅", "午", "戌"),
    "亥": ("木", "亥", "卯", "未"),
    "卯": ("木", "亥", "卯", "未"),
    "未": ("木", "亥", "卯", "未"),
    "木": ("木", "亥", "卯", "未"),
    "巳": ("金", "巳", "酉", "丑"),
    "酉": ("金", "巳", "酉", "丑"),
    "丑": ("金", "巳", "酉", "丑"),
    "金": ("金", "巳", "酉", "丑")
}

# 五行拼音映射表
wu_xing_pinyin_to_zi_map = {
    "mu": "木", "huo": "火", "tu": "土", "jin": "金", "shui": "水"
}
wu_xing_zi_to_pinyin_map = {v: k for k, v in wu_xing_pinyin_to_zi_map.items()}
# 天干拼音映射表
tian_gan_pinyin_to_zi_map = {
    "jia": "甲", "yi": "乙", "bing": "丙", "ding": "丁",
    "wu": "戊", "ji": "己", "geng": "庚", "xin": "辛",
    "ren": "壬", "gui": "癸"
}
tian_gan_zi_to_pinyin_map = {v: k for k, v in tian_gan_pinyin_to_zi_map.items()}
# 地支拼音映射表
di_zhi_pinyin_to_zi_map = {
    "zi": "子", "chou": "丑", "yin": "寅", "mao": "卯",
    "chen": "辰", "si": "巳", "wu": "午", "wei": "未",
    "shen": "申", "you": "酉", "xu": "戌", "hai": "亥"
}
di_zhi_zi_to_pinyin_map = {v: k for k, v in di_zhi_pinyin_to_zi_map.items()}