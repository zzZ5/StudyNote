#!usr/bin/python3
# -*- coding: utf-8 -*-
# author zzZ5

'''
python自带的装饰器
'''

# import time


# def time_it(func):
#     # 创建一个时间装饰器, 用于计算函数运行的时间.

#     def call_func():
#         start_time = time.time()
#         func()
#         stop_time = time.time()
#         print("运行时间是{}".format(stop_time-start_time))

#     return call_func


# # 用@方法的方式使用装饰器
# @time_it
# def test():
#     print("----test----")
#     for i in range(1000):
#         pass


# test()


'''
在店里买咖啡, 需要选择咖啡容量(罗老师, 别这样), 选择是否添加牛奶, 摩卡等, 这时就可以使用装饰者模式.
'''


class Beverage():
    '''
    饮料父类
    '''

    def __init__(self):
        self._description = "Unknown beverage"
        self._cost = 0

    def get_description(self):
        # 获取饮料的描述
        return self._description

    def get_cost(self):
        # 获取饮料的价格
        return self._cost


class Condiment(Beverage):
    '''
    调料父类, 继承自Beverage并不是为了继承行为, 而是为了类型匹配
    '''

    def get_description():
        pass

    def get_cost():
        pass


class DarkRoast(Beverage):
    # 深焙咖啡类, 并初始化描述和价格
    def __init__(self):
        self._description = "DarkRoast"
        self._cost = 12.5


class Espresso(Beverage):
    # 浓缩咖啡类, 并初始化描述和价格
    def __init__(self):
        self._description = "Espresso"
        self._cost = 13.8


class Mocha(Condiment):
    # 配料摩卡, 并初始化描述和价格
    def __init__(self, beverage):
        self.beverage = beverage
        self._cost = 2.5

    def get_description(self):
        return self.beverage.get_description() + ", Mocha"

    def get_cost(self):
        return round(self.beverage.get_cost() + self._cost, 2)


class Whip(Condiment):
    # 配料奶泡, 并初始化描述和价格
    def __init__(self, beverage):
        self.beverage = beverage
        self._cost = 1.4

    def get_description(self):
        return self.beverage.get_description() + ", whip"

    def get_cost(self):
        return round(self.beverage.get_cost() + self._cost, 2)


# 新建一个深焙咖啡, 并添加摩卡和奶泡
beverage1 = DarkRoast()
beverage1 = Mocha(beverage1)
beverage1 = Whip(beverage1)

# 新建一个浓缩咖啡, 并添加两次奶泡
beverage2 = Espresso()
beverage2 = Whip(beverage2)
beverage2 = Whip(beverage2)

print(beverage1.get_description(), " ￥", beverage1.get_cost())
# 输出结果: DarkRoast, Mocha, whip  ￥ 16.4
print(beverage2.get_description(), " ￥", beverage2.get_cost())
# 输出结果: Espresso, whip, whip  ￥ 16.6
