#以浮点数格式输出三角形三边，并输出三角形的面积

a=float(input("请输入三角形的边长a:"))
b=float(input("请输入三角形的边长b:"))
c=float(input("请输入三角形的边长c:"))
if a+b>c and a-b<c:
    p=(a+b+c)/2
    area=(p*(p-a)*(p-b)*(p-c)) ** 0.5
    print('三角形的三边长分别为：a=%0.1f,'%a,'b=%0.1f,'%b,'c=%0.1f'%c)
    print('三角形的面积=',round(area,15))
else:
    print('不能构成三角形')