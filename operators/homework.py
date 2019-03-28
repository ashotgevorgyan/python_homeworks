#!/usr/bin/python

""" 1. Իրականացրե՛ք Date դասը, որի նմուշները սկզբնարժեքավորման ժամանակ ընդունում են ամիսը և օրը։
Ամսաթվերը հանելու (d1 - d2) դեպքում պետք է վերադարձվի d1-ի և d2-ի միջև օրերի քանակը։
Օրերի քանակը պետք է լինի հավասար զրոյի, եթե d1-ը և d2-ը միևույն ամսաթիվն են, լինի զրոյից մեծ, եթե
d1-ը d2-ից ուշ է, լինի զրոյից փոքր, եթե d1-ը d2-ից շուտ է։ Համարեք, որ բոլոր ամսաթվերը նշված են
միևնույն ոչ նահանջ տարվա (փետրվարը 28 օր ունի) սահմաններում։
"""


class Date:
  def __init__(self, m, d):
    self.m = m
    self.d = d

  def __sub__(self, other):
    m1 = self.m - other.m
    d1 = self.d - other.d
    d1 = m1 * 30 + d1
    if (self.m < 2 < other.m or other.m < 2 < self.m):
      if (d1 > 0):
        d1 -= 2
      else:
        d1 += 2
    return Date(m1, d1)

  def __str__(self):
    return "{}".format(self.d)


""" 2.Սահմանեք Point դասը։
Սկզբնարժեքավորման ժամանակ նմուշին փոխանցվում են x և y կոորդինատները։
Երկու նմուշների համեմատության ժամանակ == օպերատորը պետք է վերադարձնի True, եթե կետերի
կոորդինատները հավասար են և False, եթե՝ ոչ։
!= օպերատորով համեմատելու դեպքում պետք է վերադարձվի True, եթե կետերի կոորդինատները հավասար
չեն և False, եթե հավասար են։
"""


class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __eq__(self, other):
    return self.x == other.x and self.y == other.y


""" 3. Պարբերաբար որոշ խնդիրներում նոսր զանգվածների օգտագործման անհրաժեշտություն է առաջանում։ Նոսր
զանգվածը բնութագրվում է նրանով, որ նրանում արժեքների ճնշող մեծամասնությունը զրոներ են, հետևաբար
կարելի է պահել միայն ոչ զրոյական արժեքները։
Դա թույլ է տալիս ստեղծել շատ մեծ չափի նոսր զանգվածներ առանց հիշողության ավելորդ ծախսի։
"""


class SparseArray:
  def __init__(self):
    self.l = [0 for i in range(1000)]

  def __getitem__(self, item):
    return self.l[item]

  def __setitem__(self, key, value):
    self.l[key] = value


def main():
  jan5 = Date(1, 5)
  jan1 = Date(1, 1)
  print(jan5 - jan1)
  print(jan1 - jan5)
  print(jan1 - jan1)
  print(jan5 - jan5)

  mar5 = Date(10, 5)
  jan1 = Date(9, 15)
  print(mar5 - jan1)
  print(jan1 - mar5)
  print(jan1 - jan1)
  print(mar5 - mar5)

  p1 = Point(1, 2)
  p2 = Point(5, 6)
  if p1 == p2:
    print("Equal True")
  else:
    print("Equal False")
  if p1 != p2:
    print("Not equal True")
  else:
    print("Not equal False")

  p1 = Point(0, 0)
  p2 = Point(0, 0)
  if p1 == p2:
    print("Equal True")
  else:
    print("Equal False")
  if p1 != p2:
    print("Not equal True")
  else:
    print("Not equal False")

  arr = SparseArray()
  arr[1] = 10
  arr[8] = 20
  for i in range(10):
    print("arr[{}] = {}".format(i, arr[i]))

  arr = SparseArray()
  arr[10] = 123
  for i in range(8, 13):
    print("arr[{}] = {}".format(i, arr[i]))

  def print_elem(array, ind):
    print("arr[{}] = {}".format(ind, arr[ind]))

  arr = SparseArray()
  index = 100000000
  arr[index] = 123
  print_elem(arr, index - 1)
  print_elem(arr, index)
  print_elem(arr, index + 1)


if __name__ == "__main__":
  main()
