#!usr/bin/python3
# -*- coding: utf-8 -*-
# author zzZ5

def singleton(cls):
    # 函数装饰器实现单例模式
    _instance = {}

    def inner():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]
    return inner


@singleton
class Test():
    def __init__(self):
        pass


test1 = Test()
test2 = Test()
print(id(test1) == id(test2))

# =====================================分割线=====================================

# class Singleton():
#     # 类装饰器实现单例模式
#     def __init__(self, cls):
#         self._cls = cls
#         self._instance = {}

#     def __call__(self):
#         # 类被调用时会触发此方法
#         if self._cls not in self._instance:
#             self._instance[self._cls] = self._cls()
#         return self._instance[self._cls]


# @Singleton
# class Test():
#     def __init__(self):
#         pass


# test1 = Test()
# test2 = Test()
# print(id(test1) == id(test2))

# =====================================分割线=====================================

# class Singleton():
#     # new关键字实现单例模式
#     _instance = None

#     def __new__(cls, *args, **kw):
#         # 在新建类实例时调用该方法
#         if cls._instance is None:
#             cls._instance = object.__new__(cls, *args, **kw)
#         return cls._instance

#     def __init__(self):
#         pass


# singleton1 = Singleton()
# singleton2 = Singleton()
# print(id(singleton1) == id(singleton2))

# =====================================分割线=====================================

# class Singleton(type):
#     # metaclass实现单例模式
#     _instances = {}

#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             cls._instances[cls] = super(
#                 Singleton, cls).__call__(*args, **kwargs)
#         return cls._instances[cls]


# class Test(metaclass=Singleton):
#     pass


# test1 = Test()
# test2 = Test()
# print(id(test1) == id(test2))
