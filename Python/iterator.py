
# def get_pairs(listA, listB):
#     """在listA和listB范围中生成索引对"""
#     for i in listA:
#         for j in listB:
#             yield i, j


# for i, j in get_index(listA, listB):
#     if i == j:
#         break


class NumberWords:
    """数数, 从start到stop的英文数字迭代"""

    _WORD_MAP = (
        'one',
        'two',
        'three',
        'four',
        'five',
    )

    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        # 该方法使得这个类可以迭代
        return self

    def __next__(self):
        # 该方法使得这个类成为迭代器, 每次迭代会调用该方法
        if self.start > self.stop or self.start > len(self._WORD_MAP):
            raise StopIteration
        current = self.start
        self.start += 1
        return self._WORD_MAP[current - 1]


for number in NumberWords(start=1, stop=5):
    print(number)
