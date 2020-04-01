# 01:随机输入一个字符串（5 个以上字符）并为其每个字符的 ASCII 码形成列表并输出。
# 参考运行结果如下： 
# 请输入一个字符串：daecb 
# 字符串的 ASCII 为：[100,97 ,101 ,99 , 98] 
# text = input("请输出一个字符串：")
# result = []
# for t in text:
#     result.append(ord(t))
# print("字符串的ASCII为：",result)

# 02:统计输入的字符串（6 个以上单词）中单词的个数，单词之间用空格分隔。 
# 参考运行结果如下: 
# 请输入字符串：python is easy! 
# 单词个数为：3 
# text = (input("请输入字符串："))
# x = 1
# for t in text:
#     if t == ' ':
#         x += 1
# print("单词个数为：",x)

# 03:输入一行字符（20 个以上字符），分别统计出其中英文字母、空格、数字和其它字符的个数。 
# 运行结果如下： 
# 请输入一个字符串：45se r,d5d~   s58*
# 英文字母=6 个,空格=4 个,数字=5 个,其他=3 个
# string = (input("请输入一个字符串："))
# letters = 0
# space = 0
# digit = 0
# others = 0
# for t in string:
#     if t.isalpha():
#         letters += 1
#     elif t.isspace():
#         space +=1
#     elif t.isdigit():
#         digit +=1
#     else:
#         others +=1
# print("英文字母=%d 个，空格=%d 个，数字=%d 个，其他=%d 个" %(letters,space,digit,others))
    
# 04:有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？ 
# 参考运行结果如下： 
# 1 2 3 ，1 2 4 ，1 3 2 ，1 3 4 ，1 4 2 ，1 4 3 ， 
# 2 1 3 ，2 1 4 ，2 3 1 ，2 3 4 ，2 4 1 ，2 4 3 ， 
# 3 1 2 ，3 1 4 ，3 2 1 ，3 2 4 ，3 4 1 ，3 4 2 ， 
# 4 1 2 ，4 1 3 ，4 2 1 ，4 2 3 ，4 3 1 ，4 3 2 ，

numberList=[1,2,3,4]
complexList=[]
def permutationNum():
    for i in numberList:
        for j in numberList:
                for k in numberList:
                    if i!=j and k!=j and i!=k:
                        complexList.append(str(i)+" "+str(j)+" "+str(k))
    print("共有{}种组合，分别为{}".format(len(complexList),complexList))

permutationNum()
