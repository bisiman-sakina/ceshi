''' 调用函数

# 取绝对值
print(abs(-90))
# 取最大的值
print(max(2,27))

#数据类型转换
print(int(158.99))
print(str(292.09))
print(float(19.880))
print(bool(1))
print(bool())

#变量a指向函数
a=abs
print(a(-1.09))


X = abs(-100)
Y = abs(-3)
print(X,Y)
print('max(1,2,3)=',max(1,2,3))
print('sum([1,2,3])=',sum([1,2,3]))
print('min(-1,26,-9,20)=',min(-1,26,-9,20))

a=max(1,2,3)   #取最大值
b=sum([1,2,3])   #求和
c=min(-1,26,-9,20) #取最小值
print(sum([X,Y,a,b,c,]))  #求和

a1=X%Y  #去余数
print('X除以Y的余数是'+str(a1))
a2 = X*Y
print('X乘以Y的值是'+str(a2))
a3 = X//Y
print('X除以Y的商是'+str(a3))

my = "A B C"
print(my.replace(" ","")) #replace
mi = "A B C"
print(mi.split())  #字符串按照空格进行分割
print("".join(mi.split()))  #使用一个空字符串合成列表内容生成新的字符串
'''


#定义函数
# def abs(x):
#     if x>=0:
#        return x
#     else:
#        return -x
# print(abs(-90))

# age=19
# if  age>=18:    #pass可以用来做占位符
#     pass

x='yyyy'
def myabs(x):
    if not isinstance(x,(int,float)):
      print('true')
    if x>=0:
        return x
    else:
        return -x










