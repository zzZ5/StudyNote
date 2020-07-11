#!usr/bin/python3
# -*- coding: utf-8 -*-
# author zzZ5


import random


class PetShop:
    '''一个宠物商店'''

    def __init__(self, animal_factory=None):
        # 宠物工厂只是一个抽象工厂, 我们可以在未来使其实例化
        self.pet_factory = animal_factory

    def show_pet(self):
        # 使用抽象工厂创建和展示宠物
        pet = self.pet_factory()
        print("We have a lovely {}, it says {}.".format(pet, pet.speak()))


class Dog:
    # Dog工厂
    def speak(self):
        return "woof"

    def __str__(self):
        return "Dog"


class Cat:
    # Cat工厂
    def speak(self):
        return "meow"

    def __str__(self):
        return "Cat"


# 额外的工厂:
def random_animal():
    # 创建一个随机动物
    return random.choice([Dog, Cat])()


# 创建一个猫店
cat_shop = PetShop(Cat)
cat_shop.show_pet()
# 输出结果: We have a lovely Cat, it says meow.

# 售卖随机动物的商店
shop = PetShop(random_animal)
for i in range(3):
    shop.show_pet()
'''输出结果:
We have a lovely Dog, it says woof.
We have a lovely Dog, it says woof.
We have a lovely Cat, it says meow.
