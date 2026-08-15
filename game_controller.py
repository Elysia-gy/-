import world as w
import if_fz as fz
import random as rd
import rwmx as rw
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

is_bj = os.path.join(BASE_DIR, "背景.txt")
is_name_list = [
    "阿格莱雅", "阿那克萨戈拉斯", "丹恒", "海列屈拉", "卡厄斯兰那", "刻律德菈",
    "迈德漠斯", "赛法利娅", "缇里西庇俄丝", "昔涟", "瑕蝶", "雅辛忒丝",
    "长月夜", "长老院", "来古士", "民众"
]

ACTIONS_REGISTRY = {
    "探索奥赫玛废墟": lambda w: {"anomaly": 5, "data_integrity": -0.02},
    "与黄金裔交谈": lambda w: {**({"memory": True} if w.internal else {}), "anomaly": 3},
    "研究黑潮的源头": lambda w: {"anomaly": 10, **({"black_tide_triggered": True} if w.anomaly > 50 else {})},
    "尝试打破轮回": lambda w: {"internal": True, "anomaly": 20, "data_integrity": -0.05},
    "守护民众": lambda w: {"data_integrity": 0.2, "anomaly": -10},
    "寻找权杖的线索": lambda w: {"memory": True, "anomaly": 8},
    "向天外发出信号": lambda w: {**({"external": True} if not w.external else {}), "anomaly": 15},
    "重启世界引擎": lambda w: {"data_integrity": 0.4, "anomaly": 10, "internal": True},

    "修复古代终端": lambda w: {"data_integrity": 0.05, "anomaly": -2},
    "净化污染区": lambda w: {"anomaly": -10, "data_integrity": -0.03},
    "安抚恐慌的难民": lambda w: {"data_integrity": 0.08, "anomaly": -3},
    "收集黑潮样本": lambda w: {"anomaly": 7, **({"data_integrity": 0.02} if w.external else {})},
    "搜刮废弃补给站": lambda w: {"data_integrity": 0.04, "anomaly": 2},
    "建立临时避难所": lambda w: {"data_integrity": 0.1, "anomaly": -1, **({"data_integrity": -0.05} if w.anomaly > 80 else {})},

    "审问黑潮信徒": lambda w: {"memory": True, "anomaly": 6, **({"data_integrity": -0.05} if w.data_integrity < 0.5 else {})},
    "潜入深渊实验室": lambda w: {"anomaly": 12, "memory": True, **({"black_tide_triggered": True} if w.anomaly > 70 else {})},
    "摧毁异常信标": lambda w: {"anomaly": -15, "data_integrity": -0.04},
    "拦截黑潮先锋": lambda w: {"anomaly": -8, "data_integrity": -0.06, **({"data_integrity": 0.02} if w.memory else {})},
    "引爆能量核心": lambda w: {"anomaly": 30, "data_integrity": -0.15, "black_tide_triggered": True},

    "破解加密日志": lambda w: {"memory": True, "data_integrity": -0.01},
    "启动防御矩阵": lambda w: {"data_integrity": 0.15, "anomaly": 5},
    "追踪时空裂缝": lambda w: {"anomaly": 18, "memory": True, **({"external": True} if w.internal else {})},
    "校准重力发生器": lambda w: {"anomaly": -4, "data_integrity": 0.03},
    "逆向解析黑潮代码": lambda w: {"memory": True, "anomaly": 12, **({"internal": True} if w.data_integrity > 0.8 else {})},

    "与AI核心辩论": lambda w: {"internal": True, "anomaly": 8, **({"data_integrity": 0.05} if w.memory else {})},
    "进入休眠舱冥想": lambda w: {"internal": True, "anomaly": -5, "data_integrity": 0.03},
    "直视深渊之眼": lambda w: {"anomaly": 25, "internal": True, "data_integrity": -0.1, **({"memory": True} if w.anomaly < 20 else {})},
    "献祭自身数据": lambda w: {"data_integrity": -0.2, "anomaly": -30, "memory": True, "black_tide_triggered": False},

    "贿赂黑市商人": lambda w: {"data_integrity": -0.05, "anomaly": 2, **({"memory": True} if w.data_integrity > 0.6 else {})},
    "加入机械飞升教派": lambda w: {"internal": True, "anomaly": 12, "data_integrity": -0.08},
    "向反抗军提供情报": lambda w: {"data_integrity": 0.1, "anomaly": -6, "memory": True},
    "暗杀教派领袖": lambda w: {"anomaly": 20, "data_integrity": -0.12, "black_tide_triggered": True},

    "潜入遗忘之海": lambda w: {"anomaly": 15, **({"external": True} if w.memory else {"data_integrity": -0.05})},
    "唤醒沉睡的旧神": lambda w: {"anomaly": 35, "data_integrity": -0.2, "black_tide_triggered": True},
    "破解创世者遗书": lambda w: {"memory": True, "internal": True, "data_integrity": 0.05},
    "穿越镜像迷宫": lambda w: {"anomaly": 10, **({"internal": True} if w.anomaly > 40 else {})},

    "吞噬黑潮结晶": lambda w: {"anomaly": 12, "data_integrity": -0.08, "memory": True},
    "燃烧记忆换取力量": lambda w: {"anomaly": -10, "data_integrity": -0.25, "memory": False},
    "启动自毁协议": lambda w: {"data_integrity": -0.4, "anomaly": -100, "black_tide_triggered": False},
    "与深渊意志交易": lambda w: {"external": True, **({"memory": True} if w.data_integrity < 0.3 else {"data_integrity": -0.1})},

    "篡改过去的自己": lambda w: {"internal": True, "anomaly": 30, "data_integrity": -0.15},
    "观测平行宇宙": lambda w: {"anomaly": 18, "memory": True, "external": True},
    "重置局部时间线": lambda w: {"anomaly": -15, "data_integrity": 0.1, "memory": False},
    "锚定当前现实": lambda w: {"data_integrity": 0.15, "anomaly": -10, "internal": False},

    "在酒馆听吟游诗人": lambda w: {"data_integrity": 0.05, "anomaly": -2},
    "修理同伴的机械臂": lambda w: {"data_integrity": 0.08, "anomaly": 1},
    "仰望人造星空": lambda w: {"internal": True, "anomaly": -3},
    "记录今日见闻": lambda w: {"memory": True, "data_integrity": 0.02},
    "星神诞生的时刻": lambda w: {"memory": True, "anomaly": 8},
}
GLOBAL_ACTIONS = list(ACTIONS_REGISTRY.keys())


class GameController:
    def __init__(self, callback=None):
        self.world = w.World()
        self.callback = callback
        self.ended = False
        self.agent = {}

        char_folder = os.path.join(BASE_DIR, "characters")
        character_data = {}

        for dirpath, dirnames, filenames in os.walk(char_folder):
            for filename in filenames:
                name = os.path.splitext(filename)[0]
                matched = next((n for n in is_name_list if n == name or name.startswith(n)), None)
                if matched:
                    full_path = os.path.join(dirpath, filename)
                    with open(full_path, "r", encoding="utf-8") as f:
                        content = f.read().strip()
                        character_data.setdefault(matched, []).append(content)

        with open(is_bj, "r", encoding="utf-8") as f:
            global_background = f.read().strip()

        for name, contents in character_data.items():
            prompt = global_background + "\n\n" + "\n\n".join(contents)
            self.agent[name] = rw.Rw(name=name, prompt=prompt)

        self.actions_registry = ACTIONS_REGISTRY
        self.global_actions = GLOBAL_ACTIONS

        self.all_story_nodes = [
            fz.track, fz.tramd,
            fz.internal_1, fz.internal_2, fz.internal_3, fz.internal_4, fz.internal_5,
            fz.tide_1, fz.tide_2, fz.tide_3, fz.tide_4, fz.tide_5,
            fz.data_1, fz.data_2, fz.data_3, fz.data_4, fz.data_5,
            fz.external_1, fz.external_2, fz.external_3, fz.external_4, fz.external_5,
            fz.external_6, fz.external_7, fz.external_8, fz.external_9, fz.external_10,
            fz.internal_6, fz.internal_7, fz.internal_8, fz.internal_9, fz.internal_10,
            fz.tide_6, fz.tide_7, fz.tide_8, fz.tide_9, fz.tide_10,
            fz.data_6, fz.data_7, fz.data_8, fz.data_9, fz.data_10,
            fz.main_1, fz.main_2, fz.main_3, fz.main_4, fz.main_5,
            fz.main_6, fz.main_7, fz.main_8, fz.main_9, fz.main_10, fz.main_30, fz.custom_event
        ]

    def get_active_agents(self):
        golden_ones = [
            "阿格莱雅", "阿那克萨戈拉斯", "卡厄斯兰那", "刻律德菈", "海列屈拉",
            "迈德漠斯", "赛法利娅", "缇里西庇俄丝", "昔涟", "瑕蝶", "雅辛忒丝"
        ]
        constants = ["来古士", "长老院", "民众"]
        candidates = []
        for name in golden_ones:
            if name in self.agent:
                candidates.append(name)
        for name in constants:
            if name in self.agent:
                candidates.append(name)
        if self.world.external:
            if "长月夜" in self.agent:
                candidates.append("长月夜")
            if "丹恒" in self.agent:
                candidates.append("丹恒")
        if not candidates:
            return []
        return [rd.choice(candidates)]

    def step(self):
        if self.ended:
            return None

        self.world.round += 1
        self.world.data_integrity = min(1.0, self.world.data_integrity + 0.01)
        self.world.anomaly = max(0, self.world.anomaly - 1)

        log_lines = []
        log_lines.append(f"--- 第 {self.world.round} 轮 ---")
        log_lines.append(
            f"异常: {self.world.anomaly} | 数据: {self.world.data_integrity:.2f} | 内部: {self.world.internal} | 外部: {self.world.external} | 黑潮: {self.world.black_tide_triggered} | 记忆: {self.world.memory}")

        active = self.get_active_agents()
        if active:
            log_lines.append("【角色行动阶段】")
        for name in active:
            rw_agent = self.agent[name]
            choice = rw_agent.think_and_act(self.world, self.global_actions)
            chosen_action = self.global_actions[choice - 1]
            effect = self.actions_registry[chosen_action](self.world)
            if effect:
                log_lines.append(f"  {name} 行动: {chosen_action}")
                self.world.apply_effect(effect)
            else:
                log_lines.append(f"  {name} 行动: {chosen_action}（无实质影响）")

        rd.shuffle(self.all_story_nodes)
        triggered = False
        for node in self.all_story_nodes:
            if node.can_trigger(self.world):
                log_lines.append(f"【事件触发】{node.name}")
                log_lines.append(f"【事件描述】{node.story_text}")
                self.world.triggered_nodes.add(node.name)
                self.world.apply_effect(node.effects)
                self.world.is_game_over_run()
                triggered = True
                break
        if not triggered:
            log_lines.append("【事件】风平浪静的一轮。")

        if self.world.ended:
            self.ended = True
            log_lines.append("\n=== 游戏结束 ===")
            log_lines.append(f"结局原因: {self.world.end_reason}")

        full_log = "\n".join(log_lines)
        if self.callback:
            self.callback(full_log, self.ended)
        return full_log
