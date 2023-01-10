def str_reverse(p):
    s = input("请输入你想要反转的字符串：")
    print(s)
    for i in range(0, len(s)+1):
        s[i] = s[len(s)-i]
    print(s)

str_reverse("lin")