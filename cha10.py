# 迭代器从集合的第一个元素开始，只会往前，不会后退

import sys

list1 = [1,2,3,4]
tuple1 = (1,2,3,4)
it1 = iter(list1)  # 把一个列表制成一个迭代器
it2 = iter(tuple1)
print(next(it1))
print(type(it1))

print(type(it2))

for a in it2:
  print('迭代器：', a)
for b in list1:
  print("列表元素:", b)

# 使用sys服务
print("path is:", sys.argv[0])

print('------------------------------')

# 生成器是一个函数，该函数返回迭代器
# 来一个生成器（即来个函数）
def fibonacci(n):
  a, b, counter = 0, 1, 0
  while True:
    if (counter > n):
      return
    yield a
    a, b = b, a+b
    counter += 1

# 来一个迭代器，由生成器生成
f = fibonacci(10)

while True:
  try:
    print(next(f), end='  ')
  except StopIteration:
    sys.exit()
