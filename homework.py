#!/usr/bin/python 3.7.2
from math_util import myFactorial


# 1. Գրել ֆունկցիա, որը կընդունի 1 պարամետր՝ n, և կվերադարձնի բառարան, որի key-երն են 1-ից մինչև n֊ը, իսկ value֊ները
# դրանց համապատասխան ֆակտորիալները։

def getDict(n):
  myDict = {}
  for i in range(1, n + 1):
    myDict[i] = myFactorial(i)
  return myDict


# 2. Կատարել հետևյալ քայլերը․
# 	- Մուտքագրել նախադասություն
# 	- Հաշվել դրա տառերի քանակը /առանց օգտվելու տողի որևիցե ֆունկցիայից/
# 	- Տպել նախադսությունը, ամբողջությամբ մեծատառերով։
# 	- Տպել նախադասությունը, որի յուրաքանչյուր բառի վերջին տառը մեծատառ է
# 	- Ստանալ լիստ, որի էլեմենտները տվյալ նախադասության կենտ երկարություն ունեցող բառերն են
# 	- Վերադարձնել նախադասությունում ամենաշատ և ամենաքիչ հանդիպող տառերը/1ական/
# 	- Դասավորել բառերը ֆայլի մեջ այբբենական կարգով, որոնց դիմաց գրել համապատասխան հակադարձ բառերը /օր․ այո - ոյա/

def getString():
  a = input("nermucek axadasutyun: ")
  c = 0
  s = ''
  for i in a:
    if i in ('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'):
      # - Հաշվել դրա տառերի քանակը /առանց օգտվելու տողի որևիցե ֆունկցիայից/
      c += 1
    i1 = i.upper()
    # - Տպել նախադսությունը, ամբողջությամբ մեծատառերով։
    s += i1
  lis = a.split()
  listSorted = sorted(lis)
  lis2 = []
  lis3 = []
  for i in lis:
    iReverse = i[::-1].capitalize()
    # - Տպել նախադասությունը, որի յուրաքանչյուր բառի վերջին տառը մեծատառ է
    lis2.append(iReverse[::-1])
    if len(i) % 2 == 1:
      # - Ստանալ լիստ, որի էլեմենտները տվյալ նախադասության կենտ երկարություն ունեցող բառերն են
      lis3.append(i)
  di = {}
  for i in a:
    if i in ('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'):
      di[i] = a.count(i)
  # 	- Վերադարձնել նախադասությունում ամենաշատ և ամենաքիչ հանդիպող տառերը/1ական/
  max = 0
  min = len(a)
  min_key = ""
  max_key = ""
  for k, v in di.items():
    if (max < v):
      max = v
      max_key = k
    if (min > v):
      min = v
      min_key = k
  return str(c), str(s), " ".join(lis2), str(lis3), min_key + " : " + str(min), max_key + " : " + str(max), str(
    listSorted)


def main():
  print(getDict(10))
  print('\n'.join(getString()))


if __name__ == "__main__":
  main()
