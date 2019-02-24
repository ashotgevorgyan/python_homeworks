#!/usr/bin/python 3.7.2

# 1.Ծրագիրը տպում է արժեքները հակառակ դիրքով, առանց ծրագրում օգտագործելով երրորդ փոփոխական։
print("-------------------")

a = 54
b = 45
print(a, b)
a = a + b
b = a - b
a = a - b
print(a, b)

# 2.Ծրագիրը ստուգում է ներմուծված բառի վերջին երեք սինվոլը,տպում է կա այդ սինվոլը թե ոչ։
print("-------------------")

w = input("Please type word:  ")
if (w[-3:] == "ard"):
  print("yes")
else:
  print("no")

# 3. Ծրագիրը թույլ է տալիս ներմուծել անուն,ազգանուն,ծննդյան տարեթիվ։
# Տպում է անուն,ազգանուն,տարիքը և չափահաս է թէ ոչ։
print("-------------------")

name = input("Please enter your name\n")
surname = input("Please enter your surname\n")
date = input("Please enter your date of birth\n")
age = 2019 - int(date)
if (age > 17):
  print("%s %s your are adult, your age is %d" % (name, surname, age))
else:
  print("%s %s your are not adult, your age is %d" % (name, surname, age))


# 5. 6.Ծրագիրը գտնում է ներմուծված երեք արժեքների մեծը,փոքրը և միջինը
print("-------------------")

a = int(input())
b = int(input())
c = int(input())

max = a
min = a
middle = a
if (b < min):
  min = b
if (c < min):
  min = c
if (b > max):
  max = b
  if (a > c):
    middle = a
  else:
    middle = c
if (c > max):
  max = c
  if (a > b):
    middle = a
  else:
    middle = b
if (a == max):
  if (b > c):
    middle = b
  else:
    middle = c

# 5 - difference of min and max
print(max - min)
# 6 - sorted variables
print(min, middle, max)
