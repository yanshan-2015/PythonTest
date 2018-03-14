# 模块，是一个包含所有你定义好的函数和变量的文件
import sys
print('------------------------------------')
def diyi():
  for i in sys.argv:
    print('命令行参数：', i)
  return
diyi()

def lujing():
  print('Python的路径：', sys.path)
  return
lujing()

