import random as rd
import typing as tp

class World:
    """世界状态"""
    def __init__(self):
        self.round = 0      # 当前轮数
        self.external = False       # 外部事件
        self.internal = False       # 内部事件
        self.black_tide_triggered = False       # 黑潮触发
        self.memory = False     # 内存事件
        self.data_integrity = 1.0       # 数据完整性
        self.anomaly = 0        # 异常等级
        self.ended = False      # 是否结束
        self.end_reason = None      # 结束原因
        self.game_over = False      # 铁幕是否诞生
        self.triggered_nodes = set()    # 已触发的事件

    def apply_effect(self, effect):
        """应用效果，根据属性类型决定是加法还是直接赋值"""
        for key, value in effect.items():
            if hasattr(self, key):
                current = getattr(self, key)
                # 数值类型（int/float）用加法，其他类型（bool, str, None）直接覆盖
                if isinstance(current, (int, float)):
                    setattr(self, key, current + value)
                else:
                    setattr(self, key, value)

    def is_game_over_run(self): 
        if self.game_over == True: 
            self.anomaly = 1000
            print("[系统提醒] 铁幕已诞生！异常等级已锁定为 1000！")

class StoryNode:
    """故事节点"""
    def __init__(self, name, condition, story_text, effects=None, next_nodes=None):
        self.name = name
        self.condition = condition
        self.story_text = story_text
        self.effects = effects if effects else {}
        self.next_nodes = next_nodes if next_nodes else []

    def can_trigger(self, world):
        return self.condition(world)

    def apply_effect(self, effect):
        for key, value in effect.items():
            if hasattr(self, key):
                current = getattr(self, key)
                if isinstance(current, (int, float)):
                    setattr(self, key, current + value)
                else:
                    setattr(self, key, value)

def always_true(world): return True
def has_external(world): return world.external
def no_external(world): return not world.external
def has_internal_break(world): return world.internal
def black_tide_active(world): return world.black_tide_triggered
def memory_sealed(world): return world.memory
def data_low(world): return world.data_integrity < 0.005
def anomaly_high(world): return world.anomaly >= 1000
def is_round(world, target_round): return world.round == target_round
def is_game_over(world): return world.game_over

def random_success(world):
    base = 0.08   
    chance = base
    if world.external: chance += 0.005   
    if world.internal: chance += 0.005    
    if world.memory: chance -= 0.002      
    return rd.random() < chance

def is_success(world):
    return random_success(world) and not is_game_over(world)