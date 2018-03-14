# 输入输出的格式控制
# 用户易读的表达式 str()
# 解释器易读的表达式 repr()

def strFrepr():
  # 字符串
  s = 'hello, name'
  print(str(s))
  print(repr(s))

  # 数值
  val = 1/7
  print(val)
  print(str(val))
  print(repr(val))

  # 转义特殊字符
  spe = 'hello, name\n'
  print(spe)
  print(repr(spe))

  # 数字补充0
  print('12'.zfill(4))
  print('0.12'.zfill(4))
  print('-3.12'.zfill(4))

  return
strFrepr()

print('-------------------格式化输出----------------------')
# 格式化输出 rjust() ljust() center()
def geshi():
  # 格式化输出
  for i in range(1, 11):
    print(repr(i).ljust(2), repr(i * i).ljust(3), end=' ')
    print(repr(i * i * i).ljust(4))
  return
geshi()

# 格式化输出 字符串str.format
def strFormat():
  print("{}: {}".format('菜鸟教程', 'www.runoob.com'))
  print('{}, {name}, {site}'.format('dkjda', name='菜鸟教程', site='www.runoob.com'))
  print('站点列表 {0}, {1} 和 {other}'.format('Google', 'Runoob', other='ahhha'))

  return
strFormat()

import math
print('----------------更好地格式化----------------')
def xiaoshudian():
  print('常量PI的近似值：{0:.4f}'.format(math.pi))
  return
xiaoshudian()