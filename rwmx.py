# rwmx.py - 角色 AI 决策（Android 适配版，使用随机选择）
import random as rd

class Rw:
    def __init__(self, name, prompt, api_url=None):
        self.name = name
        self.prompt = prompt
        self.api_url = api_url  # 预留，未来可接远程 API
        self.history = []

    def think_and_act(self, world, available_actions):
        """
        让角色根据当前世界状态选择一个行动。
        当前为随机降级版，未来可替换为 requests 调用远程 API。
        """
        # 简单随机选择（1 ~ 动作总数）
        choice = rd.randint(1, len(available_actions))
        chosen = available_actions[choice - 1]
        self.history.append(f"[第{world.round}轮] {self.name} 选择了: {chosen}")
        return choice