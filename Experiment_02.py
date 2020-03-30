# 01:求三角形面积

# 02:输入某门课程成绩，将其转换成五级制（优、良、中、及格、不及格）的评定等级。

# 03:编写程序实现输入不小于 0 的数 x 作为一名员工一个月工资数额，求应交税款y并输出。设应交税款的计算公式如下： 
# 运行结果如下： 
# 请输入工资：40025 
# 应交税款为：982.500000

# score = float(input("请输入工资："))
# if score > 144000:
#     grade = (score-5000)*0.2-16920
# elif score > 36000:
#     grade = (score-5000)*0.1-2520
# elif score >5000:
#     grade = (score-5000)*0.03
# else:
#     grade = 0
# print("应交税款为：%.6f" %grade)    

# 04：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母
# 运行结果如下：
#   请输入字母：s
# 请输入第二个字母：
# a 星期六

score = (input("请输入字母："))
if score[0]=='M':
    print("星期一")
elif score[0]=='T':
    x=(input("请输入第二个字母："))
    if x[0]=='u':
        print("星期二")
    elif x[0]=='h':
        print("星期四")
elif score[0]=='W':
    print("星期三")
elif score[0]=='F':
    print("星期五")
elif score[0]=='S':
    x=(input("请输入第二个字母："))
    if x[0]=='a':
        print("星期六")
    elif x[0]=='u':
        print("星期天")
else:
    print("输出有误")