# 数据结构 - list

listA = [1, 3, 5]
listB = ['a', 'b']
listA.append('a')
listA.append(listB)
print(listA)

listC = [1, 5, 1, 3]
listC.sort()
print(listC)

# 列表当做堆栈使用 -- 后进先出，速度快
def duizhan():
  listA = [1, 2, 5, 6, 2]
  listA.pop()
  print('pop一次：', listA)
  listA.pop()
  print('pop二次：', listA)
  return
duizhan()

# 列表当队列使用 -- 先进先出，效率低 （不举例）
print('-----------------------------------------------')
# 列表推到式
def tuidao1():
  listA = [1, 3, 5]
  print([3*x for x in listA])
  return
tuidao1()

def tuidao2():
  listA = [1, 3, 5]
  print([[3*x, x**2] for x in listA if x <= 5])
  return
tuidao2()

print('-----------------------------------------------')
# 元组和序列
def yuanzu():
  t = 'sdad', 'sdadadf', 12345, 12345
  print('元组：', t)
  return
yuanzu()


print('-----------------------------------------------')
# 集合,是一个无序不重复的集
def jihe():
  j = set('112256546456')
  j2 = {'a', 'df', 'a', 'dfasdfa'}
  print('j中唯一的字母：', j)
  print(j2)
  return
jihe()

# 集合之间的操作
def jihecaozuo():
  j1 = set('sadafaasadfasy')
  j2 = set('oasdadpoasdfajd')
  print('j1集合：',j1)
  print('j2集合：',j2)

  print('在j1中但不在j2中：', j1-j2)
  print('在j1或者j2中的字母：', j1 | j2)
  print('在j1和j2中的字母：', j1 & j2)
  print('在j1或j2中的字母，但不同时在j1、j2中：', j1 ^ j2)
  return
jihecaozuo()


print('-----------------------------------------------')
# 字典，字典以关键字为索引，关键字必须是唯一。序列以整数为索引。
def ziduan():
  zi = {
    'name': 430,
    'phone': 18824869177,
    'address': 5620
  }
  print('字典：', zi)
  print('字典key换成列表：', list(zi.keys()))
  print('切换value换成列表：', list(zi.values()))
  return
ziduan()

# 字典推到式
def ziduantuidao():
  print('字典推导式：', dict([('name', 2324), ('phone', 18824869177), ('address', 5421)]))
  return
ziduantuidao()

def tuidaoshi():
  print({x: x**2 for x in (2, 4, 6)})
  return
tuidaoshi()

def jianbai():
  dict1 = dict(name='MrYuan', phone=18824869177, address='深色的海面布满白月的月光')
  print('超级简单的字典录入法：', dict1)
  return
jianbai()

print('-------------------------------------')
def bianlijiqiao():
  dict1 = dict(name='MrYuan', phone=18824869177, address='深色的海面布满白月的月光')
  for k, v in dict1.items():
    print('使用items()遍历key value: ', k, v)
  return
bianlijiqiao()

def enumareted():
  for i,v in enumerate(['name', 'phone', 'address']):
    print(i, v)
  return
enumareted()

def duozuhe():
  question = ['name', 'phone', 'address']
  mid = ['说不得', '说不得', '说不得']
  answers = ['MrYuan', '18824869177', '深色的海面布满白色的月光']
  for q, m, a in zip(question, mid, answers):
    print('同时遍历多个数组：', 'what is your {0}? It is {1}'.format(q, m, a))
  return
duozuhe()

def xulie():
  xu = range(1, 10, 2)
  for i in range(1, 10, 2):
    print(i)
  return
xulie()