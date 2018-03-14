# dictionary = dict 字典的使用   类似JavaScript里面的对象
d = {'name': 'huawei', 'phone': '18824869177', 6: 23, 'tup':(1,2,3,3)}
print(d['name'])
print(d[6])

# 修改字典的值
d['name'] = 'Mr.yuan'
print(d)

# 删除字典元素
#del d['name']
#print(d)

# 清空字典
# d.clear()
# print(d)

# 删除字典
# del d

# 字典长度
print('字典长度：', len(d))

# 输出类型
print(type(d))

# 字典复制
print(d.copy())

# 字典取得键值
print(d.get('name'))

# 判断
if 'name' in d:
  print('true')

# 返回字典中的元组
print(d.keys())

# 更新字典
d2 = {'a': 25, 'b': 33, 'c': 28}
d.update(d2)
print(d)

print('---------------------------')
dd = {}
print(dd)
dd['guangzhou'] = ['广州', '深圳', '珠海', '佛山', '东莞', '河源']
# dd['guangzhou'].reverse()
print(dd)

print('------------------------------------')
# end关键字是使用输出结果在同一行
for i in dd['guangzhou']:
  print(i, end=',')

