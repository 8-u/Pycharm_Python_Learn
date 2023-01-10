# 作业1
"""
#字符串的格式化问题

name = 15
print("age = %10.2f" % name)
# 10控制宽度，.2控制小数点位数，进行四舍五入操作

print(f"age = {name}")
# f 代表格式化 format

"""

# 作业2
"""
# 综合作业：股价计算小程序

growth_day = int (input("input the growth_day:"))
name = "传智播客"
stock_price = 19.999
stock_code = "003032"
stock_price_daily_growth_factor = 1.2

print(f"公司：{name}，股票代码：{stock_code}，当前股价：{stock_price}\n"
      f"每日增长系数是：{stock_price_daily_growth_factor}，经过7天的增长后，股价达到了："
      f"{stock_price * (stock_price_daily_growth_factor ** growth_day) }")

print("\n")

print("公司：%s，股票代码：%s，当前股价：%.2f\n"
      "每日增长系数是：%.2f，经过7天的增长后，股价达到了：%.2f"
      % (name, stock_code, stock_price, stock_price_daily_growth_factor,
         stock_price * (stock_price_daily_growth_factor ** growth_day))
      )
"""

# 作业三
"""
user_name = input("请输入您的用户名：")
user_type = input("请输入您的用户类型：")
print(f"您好：{user_name},您是尊贵的：{user_type}用户，欢迎您的光临。")
"""

# 作业四
"""
result = 10 > 5
# result = int(result)
print(f"{result}   {type(result)}")
"""

# 作业五
"""
# 练习案例：语句判断
height = int(input("请输入您的身高："))
vip_level = int(input("请输入您的等级："))
if height <= 120:
    print("身高小于120，可以免费游玩。")
elif vip_level >= 3:
    print("等级满足条件，可以免费游玩。")
else:
    print("不可以免费游玩。")
    
# 改进

if int(input("请输入您的身高：")) <= 120:
    print("身高小于120，可以免费游玩。")
elif int(input("请输入您的等级：")) >= 3:
    print("等级满足条件，可以免费游玩。")
else:
    print("不可以免费游玩。")
    
"""

# 作业六

"""
# 利用循环实现1到100的和
number = 0
i = 1
while i < 101:
    number += i
    i += 1
print(number)
"""

# 作业六
"""
# 利用循环实现猜数字的案例
import random
num = random.randint(1, 10)
guess_num = int(input("请输入您猜测的数字："))
count = 1
while 1:
    if guess_num > num:
        guess_num = int(input("猜大了，请重新输入吧："))
        count += 1
    elif guess_num == num:
        print(f"congratulations，the true answer is {num},totally counts is {count}")
        break
    else:
        guess_num = int(input("猜小了，请重新输入吧："))
        count += 1
"""

# 作业七
"""
# 利用循环实现九九乘法表
i = 1
while i < 10:
    j = 1
    while j <= i:
        print(f"{j} * {i} = {i * j}", end='\t')
        j += 1
    print("\n")
    i += 1
"""

# 作业八
"""
# 数一数有几个a
count = 0
name = "ahfuiehkjahjkfahuifak"
for i in name:
    if i == 'a':
        count += 1
print(count)
"""

# 作业九
"""
# 发工资案例
import random
total_money = 10000
for i in range(1,21):
    scor_i = random.randint(1, 11)
    if scor_i < 5:
        print(f"员工{i}，绩效分{scor_i}，低于5，不发工资，下一位")
        continue
    else:
        if total_money != 0:
            total_money -= 1000
            print(f"向员工{i}发放工资1000元，账户余额还剩余{total_money}")
        else:
            print("工资发完了，下个月再领取吧")
            break
"""

# 作业十
"""
# 综合案例：黑马ATM
money = 5000000
name = input("请输入您的名字：")


def main():
    while 1:
        main_card()
        n = int(input("please chose the function that you want reality:"))
        if n == 1:
            cheek()
        elif n == 2:
            deposit()
        elif n == 3:
            out_deposit()
        elif n == 4:
            break
        else:
            print("您输入的数字有误，程序退出")
            break


def main_card():
    print("————————黑马ATM————————")
    print("——————余额查询功能——————chose 1")
    print("——————存款功能—————————chose 2")
    print("——————取款功能—————————chose 3")
    print("——————退出功能—————————chose 4")


def cheek():
    print(f"——————您的余额为：{money}元——————")
    print()
    print()


def deposit():
    global money
    in_put = int(input("请输入您想要存入的款目："))
    money += in_put
    print(f"——————成功存入{in_put}元———————")
    cheek()


def out_deposit():
    global money
    out_put = int(input("请输入您想要取出的款目："))
    money -= out_put
    print(f"——————成功取出{out_put}元———————")
    cheek()


main()
"""

# 作业十一
"""
# 列表常用功能练习
list1 = [21, 25, 21, 23, 22, 20]
list2 = ["聊城大学"]
list1.append(31)
print(f"列表{list1}")
list1.extend(list2)
print(list1)
print(list1[0])
print(list1[-1])
print(list1.index(31))
print(list1.index(21))
"""

# 作业十二
"""
# 取出列表内的偶数
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = []
new_list2 = []
i = 0
while list1[i] % 2 == 0:
    # 思路有问题，一开始i=0，list【0】=1，不进入循环就直接打印new_list了
    new_list.append(list1[i])
    i += 1
print(new_list)
print()
# for x in range(0, len(list1)):
#     if list1[x] % 2 == 0:
#         new_list2.append(list1[x])
# print(new_list2)
"""

# 作业十三
"""
# 元组的基本操作
ti = ("周杰伦", 11, ["football", "music"])
print(ti.index(11))
print(ti[0])
del ti[2][0]
ti[2].append("coding")
print(ti)
"""

# 作业十四
"""
name = "deckcedsdeed"
# new = name.strip("ed")
new = name.split("e")
print(new)
print(name.index('e'))
name1 = name.replace('e', '好')
print(f"原本字符串是{name}，修改后字符串为{name1}")
"""

# 作业十五
"""
# 分割字符串
case = "itheima itcast boxuegu"
count1 = case.count("it")
print(count1)
new_case = case.replace(" ", "|")
print(new_case)
new_case2 = new_case.split("|")
print(new_case2)
"""

"""
t1 = ["a", "n", 12, "u"]
t1 = t1[0:]
print(t1)

str = "ajfkljslkfj"
new_str = str[::2]
print(type(new_str))

jihe = set()
print(type(jihe))
"""

# 作业十六
"""
# 信息去重
my_list = ['黑马程序员', '传智播客', '黑马程序员', '传智播客', 'itheima', 'itcast', 'itheima', 'itcast', 'best']
my_set = set()
for element in my_list:
    my_set.add(element)
    # 注意！！！add没有返回值，不用赋值操作 
print(my_set)
"""

# 作业十七
"""
# 文件读取并计数操作
with open("E:/word.txt", "r", encoding="UTF-8") as f:
    # print(type(f.read()))
    # 上面那行如果执行了，f.read()，那么文件中的指针就会指向最后，从而计算错误
    print(f.read().count("it"))
"""

# 作业十八
"""
需求分析
f = open("E:/bill.txt", 'r', encoding="UTF-8")
f1 = open("E:/bill.txt.bak", "w", encoding="UTF-8")
for line in f:
    if line[-1:] == "测试":
        continue
    else:
        f1.write(f.readline())
f.close()
f1.close()

"""

# 作业十九
"""
openai测试
import turtle
import random

# 设置画布
turtle.setup(400, 600)
turtle.bgcolor("black")

# 设置画笔
pen = turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.pensize(2)
pen.hideturtle()


# 绘制烟花
def draw_firework(x, y):
    pen.goto(x, y)
    pen.dot(random.randint(10, 30), random.choice(["red", "orange", "yellow", "white"]))

    for i in range(random.randint(8, 20)):
        pen.forward(random.randint(10, 50))
        pen.dot(random.randint(10, 30), random.choice(["red", "orange", "yellow", "white"]))
        pen.backward(random.randint(10, 50))
        pen.left(random.uniform(10, 180))


# 生成随机坐标
for i in range(10):
    x = random.randint(-200, 200)
    y = random.randint(-300, 300)
    draw_firework(x, y)

# 保持窗口打开
turtle.done()
"""

# 作业二十
"""
类的构造以及面向对象
class naozhong:
    id = None
    price = None

    def ring(self):
        import winsound
        winsound.Beep(2000, 3000)


naozhong1 = naozhong()
naozhong1.id = 30012
naozhong1.price = 19.99
naozhong1.ring()
"""

# 作业二十一
"""
类的构造方法

class student:

    def __init__(self, name, id):
        self.name = name
        self.id = id


student1 = student("wangzechao", "2021400387")
print(student1.name)
"""

# 作业二十二
"""
系统录入信息

class Student:

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


for i in range(1, 10):
    print(f"当前录入第{i}位学生的信息，总共需要录入10位学生信息")
    a = input("请输入学生姓名：")
    b = input("请输入学生年龄：")
    c = input("请输入学生地址：")
    stu = Student(a, b, c)
    print(f"学生1信息录入完成，信息为：【学生姓名：{stu.name}，年龄：{stu.age}，地址：{stu.address}】")
"""

# 作业二十三
"""
设计带有私有成员的手机
class phone:
    __is_5g_enable = True

    def __check_5g(self):

        if self.__is_5g_enable:
            print("5g open")
        else:
            print("5g close,use 4g")

    def call_by_5g(self):
        self.__check_5g()
        print("calling")


phone1 = phone()
phone1.call_by_5g()
"""



