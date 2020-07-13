#!usr/bin/python3
# -*- coding: utf-8 -*-
# author zzZ5

class RemoteControl():
    '''
        遥控器类, 用于注册命令和触发命令.
    '''

    def __init__(self):
        self.buttons = {}
        self.records = []

    def set_command(self, button, command):
        # 注册命令到遥控器按键上
        self.buttons[button] = command

    def button_on_click(self, button):
        # 当按键被触发时执行命令, 并记录该命令
        self.buttons[button].execute()
        self.records.append(button)

    def undo_on_click(self):
        # 当用户点击撤销时按顺序撤销命令
        if len(self.records) > 0:
            button = self.records.pop()
            self.buttons[button].undo()


class Command():
    # 命令父类
    def execute(self):
        pass

    def undo(self):
        pass


class LightOnCommand(Command):
    # 开灯命令
    def execute(self):
        # 执行
        print("Light on!")

    def undo(self):
        # 撤销
        print("Light off!")


class LightOffCommand(Command):
    # 关灯命令
    def execute(self):
        # 执行
        print("Light off!")

    def undo(self):
        # 撤销
        print("Light on!")


# 新建遥控器类和命令类
remote_control = RemoteControl()
light_on_command = LightOnCommand()
light_off_command = LightOffCommand()
# 将命令类注册到遥控器按键上
remote_control.set_command(0, light_on_command)
remote_control.set_command(1, light_off_command)
# 点击按键
remote_control.button_on_click(1)
remote_control.button_on_click(0)
# 点击撤销按键
remote_control.undo_on_click()
remote_control.undo_on_click()
