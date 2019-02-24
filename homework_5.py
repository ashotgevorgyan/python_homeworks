#!/usr/bin/python 3.7.2

# 1. Գրեք ծրագիր, որը յուրաքանչյուր ներածված տողից արտածում է տրված համարով տառը։ Դա կարող է
# օգտագործվել, օրինակ, հապավումների կառուցման կամ ակրոստիքոսներ կարդալու համար։ Եթե ինչ-որ տողեր
# շատ կարճ են, և նրանցում տվյալ համարով սիմվոլ չկա, ապա այդպիսի տողերը արտածման ժամանակ
# պարզապես պետք է բաց թողնել։

a = int(input("nermuceq toxeri qanak@: "))
m = []
for i in range(a):
  bar = input('greq bar: ')
  m.append(bar)
b = int(input('nermuceq index: '))
n = ''
for i in m:
  n += i[b]
print(n)

# 2. Դուք պատրաստվում եք գնալ խանութ և գրի եք առնում, թե ինչ և որքան պետք է գնել։ Գրեք ծրագիր, որը
# նախ կարդում է գնումների քանակը, ապա հերթով յուրքանաչյուր գնվող ապրանքի անվանում և քանակը
# (ամբողջ թիվ) առանձին տողերում, ապա արտածում է դրանք հակառակ կարգով, արտածելով յուրաքանչյուր
# ապրանքի անունը և քանակը մեկ տողում իրարից անջատելով մեկ բացատով։

a = int(input('greq gnumneri qanak: '))
m = []
for i in range(a):
  bar = input('apranqi anun: ')
  qan = input('apranqi qanak: ')
  m.append(bar + " " + qan)
m.reverse()
# print('\n'.join(m))
for i in m:
  print(i)

# 3. Կադրերի բաժնի պետը ուզում է իմանալ, թե նույն ազգանունն ունեցող քանի տղամարդ է աշխատում
# կազմակերպությունում։ Նա ունի ազգանունների ցուցակ, և այդ ցուցակի հիման վրա պետք է հաշվել այլ
# ազգանունների հետ համընկնող ազգանունների քանակը։

list = ["Ivanov", "Sidorov", "Petrov", "Ivanov", "Petrov", "Petrov", "Gevorgyan", "Gevorgyan"]
mySet = set()
c = 0
for i in list:
  mySet.add("%s : %d" % (i, list.count(i)))
print(mySet)

for i in mySet:
  if (int(i[-1]) > 1):
    c += int(i[-1])
print(c)

# 4. Գրեք «Ցուլեր և կովեր» խաղի մեկ փուլը մշակող ծրագիր: Օգտատերը մուտքագրում է երկու տող: Պետք է
# երաշխավորվի, որ այդ տողերը նույն երկարության են և որ տողերից յուրաքանչյուրի բոլոր նիշերը տարբեր
# են: Անհրաժեշտ է առանձին արտածել ցուլերի քանակը, այն է` երկու տողերում առկա և նույն դիրքը
# զբաղեցնող սիմվոլների քանակը, և կովերի քանակը, այն է` երկու տողերում առկա, սակայն տարբեր դիրք
# զբաղեցնող սիմվոլների քանակը:

a = input('greq bar: ')
b = input('greq bar: ')
cul = 0
kov = 0
if (len(a) == len(b)):
  for i in range(len(a)):
    for j in range(len(b)):
      if (i == j and a[i] == b[j]):
        cul += 1
      elif (a[i] == b[j]):
        kov += 1
  print(cul)
  print(kov)
else:
  print('nermuceq havasarachap barer')

# 5. Շատ ինտերնետային սերվիսներում գրանցման ժամանակ պետք է նշել օգտատիրոջ ցանակլի անունը, ընդ
# որում անվան մեջ թույլատրվում է օգտագործել միայն լատինական տառեր, թվեր և «_» նշանը։
# Գրեք ծրագիր, որը կստուգի համապատասխանում է, արդյո՞ք, տողը այդպիսի սերվիսում որպես օգտատիրոջ
# անուն ծառայելու պահանջներին։

a = input()
m = ''
for i in a:
  if (i.isdigit() or i.isalpha() or i == "_"):
    m = "username is ok"
  else:
    m = "username is invalid"
    break
print(m)


# String Functions

def mylen(mstr):
  """

  :param mstr:
  :return:
  """
  count = 0
  for i in mstr:
    count += 1
  return count


def myreverse(mstr):
  """

  :param mstr:
  :return:
  """
  new_str = ""
  for i in range(mylen(mstr) - 1, -1, -1):
    new_str += mstr[i]
  return new_str


def containl(mstr, let):
  """

  :param mstr:
  :param let:
  :return:
  """
  for i in mstr:
    if (i == let):
      return True
  return False


def myfirstindex(mstr, let):
  """

  :param mstr:
  :param let:
  :return:
  """
  for i in range(mylen(mstr)):
    if (mstr[i] == let):
      return i


def ispolindrom(mstr):
  """

  :param mstr:
  :return:
  """
  if (mstr == myreverse(mstr)):
    return True
  return False


# Own string functions
def myIsSpace(mstr):
  """

  :param mstr:
  :return:
  """
  for i in mstr:
    if (i != ' '):
      return False
  return True


def myJoin(symbol, list):
  """

  :param symbol:
  :param list:
  :return:
  """
  s = ''
  for i in range(len(list)):
    if (i == len(list) - 1):
      symbol = ""
    s += list[i] + symbol
  return s


def mylstrip(mstr, symbol):
  """

  :param mstr:
  :param symbol:
  :return:
  """
  new_mstr = ''
  for i in range(mylen(mstr)):
    if (mstr[i] == symbol):
      continue
    else:
      break
  new_mstr += mstr[i] + mstr[i + 1:]
  return new_mstr


def myrstrip(mstr, symbol):
  """

  :param mstr:
  :param symbol:
  :return:
  """
  new_mstr = ''
  for i in range(mylen(mstr) - 1, -1, -1):
    if (mstr[i] == symbol):
      continue
    else:
      break
  new_mstr += mstr[:i] + mstr[i]
  return new_mstr


def mystrip(mstr, symbol):
  """

  :param mstr:
  :param symbol:
  :return:
  """
  new_mstr = ''
  for i in range(mylen(mstr) - 1, -1, -1):
    if (mstr[i] == symbol):
      continue
    else:
      break
  for j in range(mylen(mstr)):
    if (mstr[j] == symbol):
      continue
    else:
      break
  new_mstr += mstr[j:i + 1]
  return new_mstr


def mystripAll(mstr, symbol):
  """

  :param mstr:
  :param symbol:
  :return:
  """
  new_mstr = ''
  for i in mstr:
    if (i == symbol):
      continue
    new_mstr += i
  return new_mstr


a = input()
b = list(input())
print(myIsSpace(a))
print(myJoin(a, b))
print(mylstrip("---Hello --- world---", '-'))
print(myrstrip("---Hello --- World---", '-'))
print(mystrip("---Hello --- World---", '-'))
print(mystripAll("---Hello --- World---", '-'))
