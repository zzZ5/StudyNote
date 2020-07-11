#!usr/bin/python3
# -*- coding: utf-8 -*-
# author zzZ5

class Order:

    # 建立订单时必须设定价格, 可以选择折扣方式, 若不选择则为原价
    def __init__(self, price, discount_strategy=None):
        self.price = price
        self.discount_strategy = discount_strategy

    # 可以临时更改折扣方式
    def set_strategy(self, discount_strategy: function):
        self.discount_strategy = discount_strategy

    # 计算价格, 若无折扣, 则按原价, 若有折扣则减去折扣
    def price_after_discount(self):
        if self.discount_strategy:
            discount = self.discount_strategy(self)
        else:
            discount = 0

        # 若折扣超过原价, 则返回0
        return self.price - discount if self.price > discount else 0

    # 格式化tostring()方法
    def __str__(self):
        fmt = "<Price: {}, price after discount: {}>"
        return fmt.format(self.price, self.price_after_discount())


# 打九折, 即减去原价的10%
def ten_percent_discount(order):
    return order.price * 0.10


# 打75折再加20的优惠券
def on_sale_discount(order):
    return order.price * 0.25 + 20


print(Order(100))
print(Order(100, discount_strategy=ten_percent_discount))
print(Order(100, discount_strategy=on_sale_discount))
