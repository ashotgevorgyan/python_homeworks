#!/usr/bin/python 3.7.2

s = "Shares of IDBI Bank (up 2.32 per cent), Punjab National BankNSE 0.71 % (up 0.92 per cent), Bank of Baroda " \
    "(up 0.63 per cent) and Syndicate Bank (up 0.61 per cent) were the top gainers in the index"

# 1.Ծրագիրը վերադարձնում է տեքստում եղած թվանշանների քանակը։
n = 0
for a in s:
  if (a.isnumeric()):
    n += 1
print("------------------------------")
print(n)

# 2.Ծրագիրը վերադարձնում է տեքստում եղած տառերի քանակը։
l = 0
for a in s:
  if (a.isalpha()):
    l += 1
print("------------------------------")
print(l)

# 3.Ծրագիրը վերադարձնում է տեքստում եղած սինվոլների քանակը։
sy = 0
for a in s:
  if (not a.isnumeric() and not a.isalpha()):
    sy += 1
print("------------------------------")
print(sy)

# 4.Ծրագիրը վերադարձնում է տեքստում եղած ձայնավորների քանակը։
vs = "aeiou"
v = 0
for a in s:
  if (a in vs):
    v += 1
print("------------------------------")
print(v)

# 5.Ծրագիրը վերադարձնում է տեքստում եղած ներմուծված տառի քանակը։
i = input("Your letter here:  ")
k = 0
for d in s:
  if (d.upper() == i.upper()):
    k += 1
print("------------------------------")
print(k)

# 6 Ծրագիրը պետք է փոխարինի ներմուծված բառը աստղանիշերով տեքստում։
word1 = input("Type word which you want to encode:  ")
sp = word1.split()
for i in sp:
  if (i in s):
    s = s.replace(i, "*" * len(i))
print("------------------------------")
print(s)


