# 列表使用

list1 = ['1', '2', '3', '2', '5']
list2 = ['a', 'b', 'c', 'd']
del list1[0]
print(
  '第一个元素值：', list1[0], '\n'
  '截取列表元素,截出来的依然是列表：', list1[2:3], '\n'
  '列表长度：', len(list1), '\n'
  '列表最大值：', max(list1), '\n'
  '列表最小值：', min(list1), '\n'
  )
print('\f')

print(
  '组合：', list1+list2, '\n'
  '重复：', list1*3, '\n'
  '检查存在：', 3 in list1)


# 列表插入新元素
list1.append('a')
print(list1)

# 计算元素在列表中出现的个数
print(list1.count("2"))

# 计算元素的第一个匹配索引
print(list1.index('2'))

# 将对象插入列表
list1.insert(0, [1, 2, 3])
print("新数组：", list1)
print(list1[0][0])

# 创建二维列表
list_2d = [[1 for i in range(4)] for i in range(3)]
print('二维列表：', list_2d)

# 列表转元组
print('列表转元组：', tuple(list1))
