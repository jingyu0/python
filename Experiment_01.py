# #01：汇率兑换，输入一定数额的人民币，根据相应汇率，自动算出能够兑换的美元金额。
# x = float(input("请输入人民币金额："))
# #汇率 y
# y = 6.7
# #换算后的美元金额
# z = x / y
# print('美元金额:{0:.2f}%'.format(z))

# #02
# name = input("请输入您的姓名：")
# gender = input("请输入您的性别：")
# age = input("请输入您的年龄：")
# # 通过字典设置姓名、性别、年龄的参数
# dict = {"name":name, "gender":gender, "age":age}
# print("您的姓名是: {name}, {gender}, 年龄{age}岁".format(**dict))

#03：输入一个三位正整数，求各位数的立方之和。
x = int(input("请输入一个三位正整数："))
# x1是百位数；x2是十位数；x3是个位数
x1 = x//100
x2 = x//10%10
x3 = x%10
#立方和y
sum = x1*x1*x1+x2*x2*x2+x3*x3*x3
print("各位数的立方和是：%d" %sum)