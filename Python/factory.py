#!usr/bin/python3
# -*- coding: utf-8 -*-
# author zzZ5

class ChineseLocalizer:
    '''简单为几个单词中文本地化'''

    def __init__(self):
        self.translations = {"dog": "狗", "cat": "猫"}

    def localize(self, msg):
        '''如果没有该单词的翻译则返回原词'''
        return self.translations.get(msg, msg)


class EnglishLocalizer:
    '''简单重复该单词'''

    def localize(self, msg):
        return msg


def get_localizer(language="English"):
    '''语言工厂'''
    localizers = {
        "English": EnglishLocalizer,
        "Chinese": ChineseLocalizer,
    }

    return localizers[language]()


# 使用工厂模式创建本地化类
eng = get_localizer(language="English")
ch = get_localizer(language="Chinese")

print(eng.localize('dog'), ch.localize('dog'))
print(eng.localize('cat'), ch.localize('cat'))
print(eng.localize('pig'), ch.localize('pig'))
