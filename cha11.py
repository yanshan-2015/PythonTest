# 定义一个加法函数 def
# def add(a, b):
#   sum = a + b
#   return sum
#
# a1 = int(input('请输入a:'))
# b1 = int(input('请输入b:'))
# print('a+b =', add(a1, b1))

# 定义一个输出打印函数
def printMe(str):
  print(str)
  return
printMe('一道高墙，两世相隔')


# 匿名函数 lambda
# sum = lambda arg1, arg2: arg1 + arg2
# print(sum(10,30))

# print('----------------------------')
# def test():
#   now = 'local 作用域'
# print(now)

print('------------ 关键字global和nonlocal ----------------')
# num = 1
# def fun1():
#   global num
#   print('global:', num)
#   num = 123
#   print(num)
# fun1()

# 函数内要想使用全局定义的变量，得使用global关键字

# nonlocal改变嵌套作用域，使其无嵌套的可能（outer内的变量和inner内的变量同级，但不能与全局变量）
num1 = 10
def outer():
  num1 = 11
  def inner():
    global num1
    num1 = 12
    print('inner：', num1)
  inner()
  print('outer: ', num1)
outer()

print('global:', num1)
