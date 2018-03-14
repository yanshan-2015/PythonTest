a = 10
if a:
  print(a)
else:
  print("goodBye!")

print("--------------------------------")

age = int(input("请输入狗狗的年龄:"))
if age < 0:
  print("你是在逗我吗？")
elif age == 1:
  print('相当于14岁的人吧')
elif age == 2:
  print("相当于22岁的人")
elif age > 2:
  human = 22 + (age-2)*5
  print("对应人类年龄：", human)
print("---------------------------------")

account = 1
n = 10
sum = 0
while account<=n:
  sum = sum + n
  account +=1
  print(sum)
