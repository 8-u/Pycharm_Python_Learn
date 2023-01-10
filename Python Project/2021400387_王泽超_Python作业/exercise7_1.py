f = open("D:\\Desktop application\\Pycharm\\Python Project\\2022学年上学期python编程作业\\exercise7_1.txt", "w")

i = 0
j = 0
for i in range(1, 10):
    for j in range(1, i+1):
        f.write(f"{i}* {j} ={i * j}      ")
    f.write("\n")

f.close()


