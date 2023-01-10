import math


class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r ** 2

    def zhouchang(self):
        return 2 * math.pi * self.r


# 创建半径为1~10的圆
for i in range(1, 11):
    circle = Circle(i)
    print(f"半径为{i}的圆，面积：{circle.area():.2f} 周长：{circle.zhouchang():.2f}")
