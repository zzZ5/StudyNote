#!usr/bin/python3
# -*- coding: utf-8 -*-
# author zzZ5


# class Human():
#     # 人类类, 会speak()
#     def speak(self):
#         print("Hello")


# class Dog():
#     # 狗狗类, 会bark()
#     def bark(self):
#         print("woof")


# class AdapterHuman(Human):
#     # 让狗狗套进人皮套, 学会speak()
#     def __init__(self, dog):
#         self.dog = dog

#     def speak(self):
#         self.dog.bark()


# dog = Dog()
# human = Human()
# dogman = AdapterHuman(dog)

# dogman.speak()
# human.speak()


class Dog:
    def __init__(self):
        self.name = "Dog"

    def bark(self):
        return "woof!"


class Adapter():
    """通过替代方法来适配对象.
    Usage
    ------
    dog = Dog()
    dog = Adapter(dog, make_noise=dog.bark)
    """

    def __init__(self, obj, **adapted_methods):
        """我们在dict中设置适配方法."""
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        """所有未适配的调用也都传递给对象."""
        return getattr(self.obj, attr)

    def original_dict(self):
        """返回原始对象的dict."""
        return self.obj.__dict__


dog = Dog()
dog_adapter = Adapter(dog, make_noise=dog.bark)

print(dog.name)
print(dog_adapter.name)
print(dog.bark())
print(dog_adapter.make_noise())
print(dog_adapter.bark())
