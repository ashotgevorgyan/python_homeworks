#!/usr/bin/python 3.7.2

s = "Shares of IDBI Bank (up 2.32 per cent), Punjab National BankNSE 0.71 % (up 0.92 per cent), Bank of Baroda " \
    "(up 0.63 per cent) and Syndicate Bank (up 0.61 per cent) were the top gainers in the index"

# 1.Ծրագիրը վերադարձնում է տեքստում եղած թվանշանների քանակը։
n = [i for i in s if i.isdigit()]
print("------------------------------")
print(len(n))

# 2.Ծրագիրը վերադարձնում է տեքստում եղած տառերի քանակը։
l = [i for i in s if i.isalpha()]
print("------------------------------")
print(len(l))

# 3.Ծրագիրը վերադարձնում է տեքստում եղած սինվոլների քանակը։
a = [i for i in s if (not i.isnumeric() and not i.isalpha())]
print("------------------------------")
print(len(a))

# 4.Ծրագիրը վերադարձնում է տեքստում եղած ձայնավորների քանակը։
vs = "aeiou"
v = [i for i in s if (i in vs)]
print("------------------------------")
print(len(v))

# 5.Ծրագիրը վերադարձնում է տեքստում եղած ներմուծված տառի քանակը։
l = input("Your letter here:  ")
k = [i for i in s if (i.upper() == l.upper())]
print("------------------------------")
print(len(k))

# 6 Ծրագիրը պետք է փոխարինի ներմուծված բառը աստղանիշերով տեքստում։
word1 = input("Type word which you want to encode:  ")
sp = word1.split()
s = [s.replace(i, "*" * len(i)) for i in sp if (i in s)]
print("------------------------------")
print(s)
