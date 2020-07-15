
class State:
    """状态父类"""

    def scan(self):
        """调频"""
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0
        print("Scanning... Station is {} {}".format(
            self.stations[self.pos], self.name))


class AmState(State):
    """中波状态"""

    def __init__(self, radio):
        self.radio = radio
        self.stations = ["1250", "1380", "1510"]
        self.pos = 0
        self.name = "AM"

    def toggle_amfm(self):
        print("Switching to FM")
        self.radio.state = self.radio.fmstate


class FmState(State):
    """短波状态"""

    def __init__(self, radio):
        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.pos = 0
        self.name = "FM"

    def toggle_amfm(self):
        print("Switching to AM")
        self.radio.state = self.radio.amstate


class Radio:

    """一个收音机. 有一个调频按钮和AM/FM切换按钮."""

    def __init__(self):
        """可以收听中波和短波, 初始化为中波"""
        self.amstate = AmState(self)
        self.fmstate = FmState(self)
        self.state = self.amstate

    def toggle_amfm(self):
        # 切换波段
        self.state.toggle_amfm()

    def scan(self):
        # 调频
        self.state.scan()


# 新建一个收音机, 并进行调频和切换波段
radio = Radio()
actions = [radio.scan] * 2 + [radio.toggle_amfm] + [radio.scan] * 2
actions *= 2
for action in actions:
    action()
