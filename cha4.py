var1 = "hello world"
var2 = "0MrYuan"

print("var1[0]", var1[0])
print("var2[1:5]", var2[1:])

print("已经更新字符串：", var1[:6]*2 + 'MrYuan')

if ('e' in var1):
  print(" e 在 var1中")
else:
  print('e不在var1中')