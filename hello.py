#print("hello world")

#print("The beautiful girl","looks","well")

#输入名字，并打招呼
#name=input("please enter your name: ")
#print('Hello,',name)

#转义字符
#print("I\'m ok")
#print("I\'m learning \npython")
#print("\\\n\\")
#python中允许r''，表示''内部的字符串默认不转义
#print(r'\\\n\\')

#.py文件中用以下输入方法
print('''line1
line2
line3''')
#python命令行直接输入
#print('''line1
#...line2
#...line3''')

#age=float(input("请输入你的年龄："))
#if age>=18:
#    print("adult")
#else:
#    print("teenager")

#输入某门课程成绩，将其转换成五级制（优、良、中、及格、不及格）的评定等
score=float(input("请输入你的成绩："))
if score>=90:
    grade='优秀'
elif score>=80:
    grade='良'
elif score>=70:
    grade='中'
elif score>=60:
    grade='及格'
else:
    grade='不及格'
print("对应的等级是：",grade)

n=123
print(n)
# 123

f=456.789
print(f)
# 456.789

s1='Hello,world'
print(s1)
# Hello,world

s2='Hello,\'Adam\''
print(s2)
# Hello,'Adam'

s3=r'Hello,"Bart"'
print(s3)
# Hello,"Bart"

s4=r'''Hello,
Lisa！'''
print(s4)
#hello
#Lisa!
