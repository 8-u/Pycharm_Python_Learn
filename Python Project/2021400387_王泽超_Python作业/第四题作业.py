# 定义父类 A
class A:
    x = 1

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def A_fangfa_1(self):
        print("666")

    def A_fangfa_2(self):
        print("777")


# 定义父类 B
class B:
    def __init__(self, d, e):
        self.d = d
        self.e = e

    def B_fangfa_1(self):
        print("888")

    def B_fangfa_2(self):
        print("999")


# 定义子类 C，继承父类 A 和 B
class C(A, B):
    def __init__(self, a, b, c, d, e):
        A.__init__(self, a, b, c)
        B.__init__(self, d, e)

    def A_fangfa_1(self):
        print("101010")
    A.x = 3

    def C_fangfa(self):
        print(f"x = {A.x}")
        print(f"a = {self.a}, b = {self.b}, c = {self.c}, d = {self.d}, e = {self.e}")


# 创建子类的实例
obj = C(1, 2, 3, 4, 5)

# 调用子类的方法
obj.A_fangfa_1()
obj.A_fangfa_2()
obj.B_fangfa_1()
obj.B_fangfa_2()
obj.C_fangfa()

