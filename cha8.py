# name = input('请输入一个数字：')
a = 0
b = 1
print('-------- start ---------')
while b < 10:
  print(b, end=',')
  a, b = b, a+b
