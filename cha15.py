# 读取键盘输入值
# def enter():
#   a = input('请输入：')
#   print('你输入的内容是：', a)
#   f = open('./open/hello.txt', 'w')
#   f.write(a)
#   f.close()
#   return
# enter()

def openthis():
  f = open('./open/hello.txt', 'w')
  f.write('曲肖冰是个唱歌的女孩，她美吗？\n我不是很清楚，她的歌还不错')
  f.close()
  return
openthis()

def read():
  f = open('./open/hello.txt', 'r')
  str = f.read()
  print('把写入的文字读取出来：', str)
  f.close()
  return
read()

# def diedaimeiyihang():
#   f = open('./open/hello.txt', 'r')
#   for line in f:
#     print(line)
#   return
# diedaimeiyihang()

def suiyi():
  f = open('./open/hello.txt', 'w')
  val = '你好啊', '中国'
  str1 = str(val)
  f.write(str1)
  print(f.tell())
  f.close()
  return
suiyi()



