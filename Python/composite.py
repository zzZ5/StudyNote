class Graphic():
    """绘图父类 """

    def render(self):
        raise NotImplementedError("You should implement this!")


class CompositeGraphic(Graphic):
    # 绘制复杂图像

    def __init__(self):
        self.graphics = []

    def render(self):
        for graphic in self.graphics:
            graphic.render()

    def add(self, graphic):
        self.graphics.append(graphic)

    def remove(self, graphic):
        self.graphics.remove(graphic)


class Ellipse(Graphic):
    # 绘制椭圆图像

    def __init__(self, name):
        self.name = name

    def render(self):
        print("Ellipse: {}".format(self.name))


# 三个椭圆
ellipse1 = Ellipse("1")
ellipse2 = Ellipse("2")
ellipse3 = Ellipse("3")
# 两个复杂图像
graphic1 = CompositeGraphic()
graphic2 = CompositeGraphic()
# 将三个椭圆添加到这两个复杂图像中
graphic1.add(ellipse1)
graphic1.add(ellipse2)
graphic2.add(ellipse3)
# 再将这两个复杂图像再添加到新的复杂图像中
graphic = CompositeGraphic()
graphic.add(graphic1)
graphic.add(graphic2)
# 所有图像都可以任意组合, 输出只需要使用render()方法即可
graphic.render()
