import world as w

my_world = w.World()

track = w.StoryNode(
    name="世界崩溃",
    condition=lambda state: w.is_round(state, 33550337),
    story_text="天空裂开漆黑的缝隙，权杖的轰鸣声震碎了奥赫玛的穹顶。第33550337次轮回，世界终究还是崩溃了...",
    effects={"ended": True, "end_reason": "铁幕诞生了！！！"}
)

tramd = w.StoryNode(
    name="铁幕诞生",
    condition=lambda state: w.is_game_over(state),
    story_text="无首的巨人！！！\n智识的克星！！！\n荒谬的造物！！！\n毁灭智识的绝灭大君！！！\n诞生了！！！",
    effects={"ended": True, "end_reason": "铁幕诞生了！！！"}
)

internal_1 = w.StoryNode(
    name="白厄的顿悟",
    condition=lambda state: w.no_external(state) and w.random_success(state),
    story_text="在又一次推动巨石时，卡厄斯兰那突然停下了。他回头望向你，眼神中第一次有了疑问：‘我们为何要这么做？’",
    effects={"internal": True, "anomaly": 5}  # 原10
)

internal_2 = w.StoryNode(
    name="黄金裔的猜忌",
    condition=lambda state: state.internal and w.random_success(state),
    story_text="你的觉醒引起了其他黄金裔的警惕。他们开始疏远你，认为你是导致轮回不稳定的异类。",
    effects={"internal": False, "anomaly": 8}  # 原15
)

internal_3 = w.StoryNode(
    name="那刻夏的预言",
    condition=lambda state: w.no_external(state) and w.random_success(state),
    story_text="那刻夏在神悟树庭中对你低语：‘我预见了一个没有巨人的未来，但那未来也意味着我们的终结。’",
    effects={"internal": True, "anomaly": 3}  # 原5
)

internal_4 = w.StoryNode(
    name="万敌的狂怒",
    condition=lambda state: state.internal and w.random_success(state),
    story_text="万敌感受到了世界的异常，他将此归咎于你的干涉，向你发起了不死不休的挑战。",
    effects={"internal": False, "anomaly": 10, "data_integrity": -0.02}  # 原30, -0.1
)

internal_5 = w.StoryNode(
    name="赛飞儿的低语",
    condition=lambda state: w.random_success(state),
    story_text="赛飞儿悄悄告诉你，她记得上一次轮回发生的事。记忆的连锁反应开始了。",
    effects={"internal": True, "memory": True, "anomaly": 10}  # 原20
)

tide_1 = w.StoryNode(
    name="黑潮的预兆",
    condition=lambda state: not w.black_tide_active(state) and w.random_success(state),
    story_text="天空的颜色变得更加晦暗，风中传来了不属于这个世界的嘶吼。黑潮正在逼近。",
    effects={"anomaly": 8}  # 原15
)

tide_2 = w.StoryNode(
    name="黑潮的侵蚀",
    condition=lambda state: w.black_tide_active(state) and w.random_success(state) and state.anomaly > 30,  # 增加条件，避免早期触发
    story_text="黑潮的触须已经蔓延到了奥赫玛的城墙下，数据开始被疯狂地吞噬和扭曲。",
    effects={"data_integrity": -0.05, "anomaly": 10}  # 原 -0.3, 20
)

tide_3 = w.StoryNode(
    name="主动的献祭",
    condition=lambda state: (not w.black_tide_active(state) and w.random_success(state) and state.anomaly > 150 and state.round > 30),  # 提高门槛
    story_text="为了获得打破轮回的力量，你主动引导了一丝黑潮入体。你感受到了力量，也感受到了疯狂。",
    effects={"black_tide_triggered": True, "anomaly": 20, "data_integrity": -0.05}  # 原50, -0.2
)

tide_4 = w.StoryNode(
    name="铁幕的投影",
    condition=lambda state: w.anomaly_high(state) and w.random_success(state),
    story_text="天空中浮现出无首巨人的虚影，仅仅是注视，就让你的数据完整性急剧下降。",
    effects={"game_over": True, "data_integrity": -0.1}  # 原 -0.5
)

tide_5 = w.StoryNode(
    name="绝望的浪潮",
    condition=lambda state: w.data_low(state) and w.random_success(state),
    story_text="世界的数据结构已经脆弱不堪，黑潮如决堤的洪水般涌入，一切都在崩解。",
    effects={"ended": True, "end_reason": "被黑潮彻底吞噬"}
)

data_1 = w.StoryNode(
    name="记忆的碎片",
    condition=lambda state: w.memory_sealed(state) and w.random_success(state),
    story_text="你捡到了一片发光的碎片，上面记录着上一次轮回的某个瞬间。记忆的封印松动了。",
    effects={"memory": True, "anomaly": 3}  # 原5
)

data_2 = w.StoryNode(
    name="数据的自我修复",
    condition=lambda state: w.data_low(state) and w.random_success(state),
    story_text="世界似乎意识到了自己的危机，开始自动修复受损的数据。你感到一阵轻松。",
    effects={"data_integrity": 0.2, "anomaly": -5}  # 原 -10
)

data_3 = w.StoryNode(
    name="逻辑的悖论",
    condition=lambda state: w.anomaly_high(state) and w.random_success(state),
    story_text="你向一个黄金裔提出了一个关于轮回的逻辑悖论，他的思维瞬间宕机，引发了小范围的数据崩溃。",
    effects={"data_integrity": -0.05, "anomaly": 10}  # 原 -0.2, 25
)

data_4 = w.StoryNode(
    name="权杖的低语",
    condition=lambda state: w.random_success(state),
    story_text="权杖δ-me13在你耳边低语，它告诉你，它正在记录一切，包括你的每一次尝试。",
    effects={"anomaly": 5}  # 原10
)

data_5 = w.StoryNode(
    name="虚假的和平",
    condition=lambda state: state.anomaly < 50 and w.random_success(state),  # 放宽条件
    story_text="这一轮轮回异常平静，没有任何灾难的迹象。但这平静本身，就是最大的异常。",
    effects={"anomaly": 8}  # 原15
)

external_1 = w.StoryNode(
    name="远方的信号",
    condition=lambda state: w.no_external(state) and w.random_success(state),
    story_text="在无尽的杂音中，你捕捉到了一段规律的信号。它来自翁法罗斯之外，微弱但坚定。是星穹列车吗？",
    effects={"external": True, "anomaly": 3}  # 原5
)

external_2 = w.StoryNode(
    name="虚假的希望",
    condition=lambda state: w.no_external(state) and w.random_success(state),
    story_text="你看到地平线上有光点闪烁，以为是列车的车灯。但当你靠近时，那只是黑潮涌动的反光。",
    effects={"anomaly": 5, "data_integrity": -0.02}  # 原10, -0.05
)

external_3 = w.StoryNode(
    name="记忆中的旅人",
    condition=lambda state: w.memory_sealed(state) and w.random_success(state),
    story_text="在记忆的碎片里，你看到了一个粉发少女的身影，她似乎在向你招手，但你看不清她的脸。",
    effects={"memory": True, "anomaly": 8}  # 原15
)

external_4 = w.StoryNode(
    name="被拒绝的来客",
    condition=lambda state: w.has_external(state) and w.random_success(state),
    story_text="当星穹列车试图进入时，翁法罗斯的法则本能地排斥了它。列车被弹开了，你必须找到方法稳定世界。",
    effects={"external": False, "anomaly": 10, "data_integrity": -0.05}  # 原20, -0.1
)

external_5 = w.StoryNode(
    name="天外陨石",
    condition=lambda state: "天外陨石" not in state.triggered_nodes and w.random_success(state),
    story_text="一颗不属于这个世界的陨石坠落，砸穿了悬锋城的一角。卡厄斯兰那的巨石也被波及。",
    effects={"anomaly": 10, "data_integrity": -0.05}  # 原25, -0.15
)

external_6 = w.StoryNode(
    name="列车长的馈赠",
    condition=lambda state: w.has_external(state) and w.random_success(state),
    story_text="帕姆从列车上探出头，扔给你一个神秘的包裹。里面似乎装着能稳定世界的数据核心。",
    effects={"external": False, "data_integrity": 0.25, "anomaly": -10}  # 原0.3, -20
)

external_7 = w.StoryNode(
    name="不速之客",
    condition=lambda state: w.has_external(state) and w.random_success(state),
    story_text="从列车上走下来的不是帮手，而是一个对翁法罗斯充满好奇的星核猎手。他的存在本身就是巨大的异常。",
    effects={"anomaly": 20, "data_integrity": -0.05}  # 原40, -0.1
)

external_8 = w.StoryNode(
    name="信号的真相",
    condition=lambda state: w.has_external(state) and w.random_success(state),
    story_text="你终于破解了那段信号，发现它并非求救，而是星穹列车发出的警告：‘不要试图离开翁法罗斯！’",
    effects={"memory": True, "anomaly": 15}  # 原25
)

external_9 = w.StoryNode(
    name="被遗弃的星槎",
    condition=lambda state: w.no_external(state) and w.random_success(state),
    story_text="一艘仙舟的星槎残骸坠落在奥赫玛附近，上面空无一人，只有一份关于‘丰饶’的残缺日志。",
    effects={"anomaly": 8, "data_integrity": -0.02}  # 原15, -0.05
)

external_10 = w.StoryNode(
    name="宇宙的尘埃",
    condition=lambda state: w.random_success(state),
    story_text="宇宙背景辐射中夹杂着不属于这个模拟世界的信息素，它们在侵蚀着翁法罗斯的边界。",
    effects={"anomaly": 5}  # 原10
)

internal_6 = w.StoryNode(
    name="阿格莱雅的织机",
    condition=lambda state: state.internal and w.random_success(state),
    story_text="阿格莱雅向你展示了她的织机，上面编织的不是命运，而是翁法罗斯一次又一次轮回的代码。",
    effects={"memory": True, "anomaly": 15}  # 原30
)

internal_7 = w.StoryNode(
    name="海瑟音的歌声",
    condition=lambda state: state.internal and w.random_success(state),
    story_text="海瑟音的歌声中充满了悲伤，她说她记得每一个在轮回中死去的黄金裔，包括你。",
    effects={"memory": True, "anomaly": 10}  # 原20
)

internal_8 = w.StoryNode(
    name="白厄的决裂",
    condition=lambda state: state.internal and w.random_success(state) and state.round > 25 and state.anomaly > 150,  # 增加延迟
    story_text="卡厄斯兰那彻底觉醒了，他决定不再推巨石，而是要亲手砸碎翁法罗斯的穹顶。",
    effects={"internal": False, "black_tide_triggered": True, "anomaly": 30}  # 原50
)

internal_9 = w.StoryNode(
    name="那刻夏的牺牲",
    condition=lambda state: state.internal and w.random_success(state),
    story_text="那刻夏用自己的生命为代价，为你换取了一段至关重要的世界底层代码。",
    effects={"internal": False, "memory": True, "data_integrity": 0.4}
)

internal_10 = w.StoryNode(
    name="黄金裔的审判",
    condition=lambda state: w.anomaly_high(state) and w.random_success(state) and state.round > 30,  # 增加轮次限制
    story_text="所有黄金裔联合起来，将你视为世界的毒瘤，对你发起了最终的审判。",
    effects={"ended": True, "end_reason": "被黄金裔处决"}
)

tide_6 = w.StoryNode(
    name="黑潮的低语",
    condition=lambda state: not w.black_tide_active(state) and w.random_success(state),
    story_text="你开始能听懂黑潮的嘶吼，它们在诉说着一个关于‘铁幕’的古老预言。",
    effects={"anomaly": 10, "memory": True}  # 原20
)

tide_7 = w.StoryNode(
    name="与潮共舞",
    condition=lambda state: state.black_tide_triggered and w.random_success(state),
    story_text="你学会了引导黑潮的力量，用它来修复受损的数据，但这让你离疯狂更近了一步。",
    effects={"data_integrity": 0.2, "anomaly": 15}  # 原30
)

tide_8 = w.StoryNode(
    name="绝灭的序曲",
    condition=lambda state: w.black_tide_active(state) and w.anomaly_high(state),
    story_text="天空被彻底染黑，无首巨人的虚影再次出现，这次它向你伸出了手。",
    effects={"game_over": True, "anomaly": 50}  # 原100
)

tide_9 = w.StoryNode(
    name="数据黑洞",
    condition=lambda state: w.black_tide_active(state) and w.random_success(state) and state.anomaly > 50,  # 增加条件
    story_text="黑潮制造了一个数据黑洞，吞噬了悬锋城的一部分，连同那里的历史和人物一起消失了。",
    effects={"data_integrity": -0.08, "anomaly": 15}  # 原 -0.4, 35
)

tide_10 = w.StoryNode(
    name="最后的防线",
    condition=lambda state: w.data_low(state) and w.black_tide_active(state),
    story_text="奥赫玛的最后一道数据防火墙正在崩溃，黑潮的先锋已经踏上了广场。",
    effects={"ended": True, "end_reason": "奥赫玛陷落"}
)

data_6 = w.StoryNode(
    name="存档损坏",
    condition=lambda state: w.random_success(state),
    story_text="你感到一阵剧烈的头痛，一段不属于你的记忆强行插入。你看到了上一次轮回中，你自己崩溃的样子。",
    effects={"memory": True, "anomaly": 15, "data_integrity": -0.03}  # 原40, -0.1
)

data_7 = w.StoryNode(
    name="NPC的觉醒",
    condition=lambda state: w.memory_sealed(state) and w.random_success(state),
    story_text="一个路边的NPC突然抓住你的手，眼神惊恐地对你说：‘救救我，我不想再重复今天的话了！’然后他就自毁了。",
    effects={"memory": True, "anomaly": 25}  # 原50
)

data_8 = w.StoryNode(
    name="代码的雨",
    condition=lambda state: w.anomaly_high(state) and w.random_success(state),
    story_text="天空开始下起绿色的代码雨，翁法罗斯的物理法则开始失效，石头飘向空中，水流向上奔腾。",
    effects={"anomaly": 30, "data_integrity": -0.08}  # 原60, -0.3
)

data_9 = w.StoryNode(
    name="权杖的真相",
    condition=lambda state: state.memory and w.random_success(state) and state.round > 25,  # 增加轮次限制
    story_text="权杖δ-me13向你揭示了最终真相：你并非救世主，你才是导致这一切轮回的‘异常’本身。",
    effects={"anomaly": 50, "game_over": True}  # 原100
)

data_10 = w.StoryNode(
    name="系统重置",
    condition=lambda state: state.data_integrity < 0.1 and w.random_success(state) and state.round > 20,  # 增加轮次限制
    story_text="世界无法再维持下去，权杖启动了强制重置程序。一切都将归零。",
    effects={"ended": True, "end_reason": "系统强制重置"}
)

main_1 = w.StoryNode(
    name="推石头的青年",
    condition=lambda state: w.no_external(state) and not w.has_internal_break(state) and state.round < 25,  # 延长至25轮
    story_text=(
        "你走在奥赫玛的街道上，看着那个名叫卡厄斯兰那的青年，第无数次推着巨石走向山顶。\n"
        "没有星穹列车，没有奇迹。黑潮在远方低吼，世界正在缓慢地死去。"
    ),
    effects={"anomaly": 3}  # 原5
)

main_2 = w.StoryNode(
    name="撕裂苍穹的轰鸣",
    condition=lambda state: w.has_external(state) and not w.has_internal_break(state) and state.round < 5,  # 延长出现窗口
    story_text=(
        "伴随着震耳欲聋的轰鸣，一辆不属于这个世界的列车砸穿了翁法罗斯的穹顶！\n"
        "星穹列车降临了。卡厄斯兰那停下了推石的手，他抬起头，眼中燃起了久违的火焰。"
    ),
    effects={"anomaly": 10}  # 原20
)

main_3 = w.StoryNode(
    name="破局的誓言",
    condition=lambda state: w.has_external(state) and w.has_internal_break(state) and not w.black_tide_active(state) and state.round < 5,
    story_text=(
        "在开拓者的见证下，白厄终于斩断了命运的枷锁。\n"
        "阿格莱雅、万敌、那刻夏……十二黄金裔齐聚一堂。他们决定不再做命运的傀儡，而是向神明拔剑。"
    ),
    effects={"anomaly": 15}  # 原30
)

main_4 = w.StoryNode(
    name="铁幕的阴影",
    condition=lambda state: w.has_internal_break(state) and not w.black_tide_active(state) and w.anomaly_high(state),
    story_text=(
        "你们的觉醒触怒了权杖。天空瞬间被漆黑的浓雾吞噬，绝灭大君「铁幕」的虚影在云端凝聚。\n"
        "系统启动了强制清洗程序，黑潮如海啸般涌来！"
    ),
    effects={"black_tide_triggered": True, "anomaly": 20, "data_integrity": -0.05}  # 原50, -0.3
)

main_5 = w.StoryNode(
    name="再创世的倒计时",
    condition=lambda state: (
        w.black_tide_active(state)
        and not w.data_low(state)
        and state.round > 40          # 提高到40轮
        and state.anomaly > 300
        and state.memory
    ),
    story_text=(
        "黑潮已经淹没了半个奥赫玛。白厄浑身是血，死死顶住即将落下的铁幕。\n"
        "三月七的影子在虚空中哭泣，那刻夏的身体正在消散。\n"
        "你站在了控制台前，必须做出最后的抉择！"
    ),
    effects={}
)

main_6 = w.StoryNode(
    name="灰白黎明",
    condition=lambda state: (
        w.black_tide_active(state)
        and state.memory
        and state.data_integrity > 0.85
        and state.round > 60          # 提高到60轮
        and state.internal
    ),
    story_text=(
        "你启动了‘再创世’程序，将所有的记忆与希望注入权杖。\n"
        "铁幕在光芒中瓦解，翁法罗斯的穹顶彻底碎裂。灰白色的黎明洒在废墟上，英雄们微笑着化为光点。\n"
        "他们终于有机会恢复，并开始新的生活。\n"
    ),
    effects={"ended": True, "end_reason": "True End: 灰白黎明"}
)

main_7 = w.StoryNode(
    name="沉重的代价",
    condition=lambda state: (
        w.black_tide_active(state)
        and not state.memory
        and state.data_integrity > 0.3
        and state.round > 40          # 提高到40轮
    ),
    story_text=(
        "你强行关闭了权杖，铁幕被封印，但翁法罗斯也失去了所有的记忆。\n"
        "世界得救了，但没有人记得那些为了救世而牺牲的黄金裔。你成了唯一背负过去的人。"
    ),
    effects={"ended": True, "end_reason": "Normal End: 沉重的代价"}
)

main_8 = w.StoryNode(
    name="铁幕的诞生",
    condition=lambda state: state.data_integrity < 0.01,
    story_text=(
        "太迟了……世界的数据已经彻底崩溃。\n"
        "铁幕从废墟中站起，它无情地碾碎了列车与黄金裔。第33550337次轮回，以绝对的毁灭告终。"
    ),
    effects={"ended": True, "end_reason": "Bad End: 铁幕的诞生"}
)

main_9 = w.StoryNode(
    name="永恒的守望者",
    condition=lambda state: (
        w.black_tide_active(state)
        and state.anomaly >= 100
        and state.memory
        and state.round > 35          # 增加轮次限制
    ),
    story_text=(
        "你吸收了所有的黑潮与记忆，用自己的灵魂替换了权杖的核心。\n"
        "铁幕消失了，但你也永远被困在了这台机器里。你成为了翁法罗斯新的神明，在无尽的岁月中孤独地守望。"
    ),
    effects={"ended": True, "end_reason": "Hidden End: 永恒的守望者"}
)

main_10 = w.StoryNode(
    name="虚无的深渊",
    condition=lambda state: (
        w.memory_sealed(state)
        and w.anomaly_high(state)
        and state.round > 30          # 增加轮次限制
    ),
    story_text=(
        "你试图用记忆封印来逃避现实，却被长夜月的幻梦彻底吞噬。\n"
        "你在虚假的欢愉中微笑着，身体却化作了黑潮的一部分。"
    ),
    effects={"ended": True, "end_reason": "Bad End: 虚无的深渊"}
)

# ===== 自定义事件（自动添加） =====
main_30 = w.StoryNode(
    name="有人就是不一样",
    condition=w.has_external,
    story_text="列车组摇来了他们所有的人脉，让铁幕加冕失败",
    effects={"external": True, "anomaly": 10}
)

# ===== 自定义事件（自动添加） =====
custom_event = w.StoryNode(
    name="星神诞生的时刻",
    condition=w.has_internal_break,
    story_text="在某一刻的轮回中，小小的种子在不断的成长下，因外界数据传入导致的彻底升格，让我们恭迎新神的诞生！！！",
    effects={"memory": True, "anomaly": 8}
)
