#!/usr/bin/python 3.7.2

# 1.Ծրագիրը որոշում է ներմուծված ջերմաստիճանի եղանակային պայմանը։
print("-------------- Task 1 -----------------")
a = input("Nermuceq jermastichan: ")
a = float(a)
if (a < 15.5):
  print('curt e')
elif (a > 33):
  print('shog e')
else:
  print('normal e')

# 2.Ծրագիրը ստուգում է ներմուծված գաղտնաբառի սինվոլների քանակը 8 մեծ,
# համեմատում է երկու անգամ ներմուծված գախտնաբառի նմանությունը։
print("-------------- Task 2 -----------------")
a = input('Nermucek gaxtnabar: ')
b = input('Krknek gaxtnabar@: ')
if (len(a) < 8):
  print('Gaxtnabar@ karch e')
elif (a != b):
  print('Gaxtnabarer@ nuyn@ chen:')
else:
  print('Gaxnabar@ aktiv e')

# 3.Ծրագիրը թույլ է տալիս ներմուծել տեքստ այնքան ժամանակ քանի դեռ չի ներմուծվել դատարկություն։
print("-------------- Task 3 -----------------")
a = "text"
while (a != ""):
  a = input("Nermuceq text: ")
print("finish")

# 4.Ծրագիրը հաշվում է ներմուծված թվի ֆակտորիալը։
print("-------------- Task 4 -----------------")
a = input('Nermuceq tiv: ')
b = abs(int(float(a)))
c = 1
for i in range(1, b + 1):
  c = c * i
print(c)

# 5.Ծրագիրը հաշվում է ներմուծված թվի խորանարդ աստիճանը։
print("-------------- Task 5 -----------------")
a = input('Nermuceq tiv: ')
b = abs(int(float(a)))
for i in range(1, b + 1):
  print("%d tvi xoranard@ havasar e %d" % (i, pow(i, 3)))
