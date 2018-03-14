# 元组(tuple)使用, 元组不能修改
item = '3', '4', '5'
print(item)
print(item[0:2])

item1 = ('google', 'nice', '华为')
print(item1[0])

# 拼接元组
print(item+item1)

# 元组元素个数
print(len(item1))

# 元组和列表互转
print(list(item))

# 输出类型
print(type(item))