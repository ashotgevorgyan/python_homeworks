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
# - Հաշվել դրա տառերի քանակը /առանց օգտվելու տողի որևիցե ֆունկցիայից/
def getString(a):
  c = 0
  for i in a:
    if i in ('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'):
      c += 1
  return c


# - Տպել նախադսությունը, ամբողջությամբ մեծատառերով։
def myUpp(a):
  s = ""
  for i in a:
    i1 = i.upper()
    s += i1
  return s


# - Տպել նախադասությունը, որի յուրաքանչյուր բառի վերջին տառը մեծատառ է
def upperLastLetter(a):
  b = a.split()
  d = []
  for i in b:
    c = i[::-1].capitalize()
    d.append(c[::-1])
  return " ".join(d)


# - Ստանալ լիստ, որի էլեմենտները տվյալ նախադասության կենտ երկարություն ունեցող բառերն են
def kentBar(a):
  lis = a.split()
  lis2 = []
  for i in lis:
    if len(i) % 2 == 1:
      lis2.append(i)
  return lis2


# - Վերադարձնել նախադասությունում ամենաշատ և ամենաքիչ հանդիպող տառերը/1ական/
def qanakMaxMin(a):
  di = {}
  for i in a:
    if i in ('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'):
      di[i] = a.count(i)

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
  return min_key + " : " + str(min), max_key + " : " + str(max)


# 	- Դասավորել բառերը ֆայլի մեջ այբբենական կարգով, որոնց դիմաց գրել համապատասխան հակադարձ բառերը /օր․ այո - ոյա/
def writeInfile(a):
  li = a.split()
  li1 = sorted(li)
  fayl = open('text.txt', 'w')
  for i in li1:
    fayl.write(i + ':' + i[::-1] + '\n')
  fayl = open('text.txt', 'r')
  rf = fayl.read()
  fayl.close()
  return rf


def main():
  a = input('nermuceq naxadasutyun: ')
  print('tareri qanakn e: ' + str(getString(a)))
  print('naxadasutyun mecatarerov: ' + myUpp(a))
  print('nax bareri vergin tar mecatar:' + upperLastLetter(a))
  print('naxad kent barer:' + str(kentBar(a)))
  print('naxad tareri qanak:' + str(qanakMaxMin(a)))
  print(writeInfile(a))


if __name__ == "__main__":
  main()
