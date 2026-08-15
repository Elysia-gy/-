import random as rd

class Rw:
    def __init__(self, name, prompt, api_url=None):
        self.name = name
        self.prompt = prompt
        self.api_url = api_url
        self.history = []

    def think_and_act(self, world, available_actions):
        choice = rd.randint(1, len(available_actions))
        chosen = available_actions[choice - 1]
        self.history.append(f"[第{world.round}轮] {self.name} 选择了: {chosen}")
        return choice
