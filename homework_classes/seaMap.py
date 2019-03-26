#!/usr/bin/python
# Դիման սիրում է ծովամարտ խաղալ։ Ցավոք, նա շատ ցրված է և մշտապես քարտեզի վրա ճիշտ չի նշում
# այն վանդակները, որոնց վրա արդեն կրակել է։ Գրե’ք դաս, որը Դիմայի փոխարեն կկառուցի քարտեզը։
# SeaMap դասը պետք է ունենա հետևյալ մեթոդները (sm-ը SeaMap-ի նմուշ է).
# sm.shoot(row, col, result) — ավելացնել քարտեզի վրա կրակելու արդյունքը։
# row-ն քարտեզի վրա տողի ինդեքսն է։
# col-ը քարտեզի վրա սյան ինդեքսն է։
# result-ը “miss” (վրիպում), “hit” (խոցում), “sink” (նավի խորտակում) տողերից մեկն է։
# sm.cell(row, col)
# Վերադարձնում է ‘.’, եթե row, col կոորդինատներով վանդակում կարող է նավ լինել։
# Վերադարձնում է ‘*’, եթե այդ վանդակի վրա արդեն կրակել են կամ այն գտնվում է խորտակված նավի կողքին։
# Վերադարձնում է ‘x’, եթե այդ վանդակում նավ է խոցվել։
# cell մեթոդը կկանչվի միայն այն ժամանակ, երբ քարտեզի վրա հայտնաբերված բոլոր նավերը խորտակված
# կլինեն։
# Այսինքն, պետք չէ ‘*’-ով նշել այնպիսի նավի կողքի վանդակները, որը խոցվել է, բայց դեռ մինչև վերջ չի
# խորտակվել։

class SeaMap:
  def __init__(self):
    self.list1 = []
    self.r = []

  def shoot(self, row, col, result):
    if (result == "miss"):
      self.list1.append([row, col, "*"])
    elif (result == "hit"):
      self.list1.append([row, col, "X"])
    elif (result == "sink"):
      self.list1.append([row, col, "X"])
      self.list1.append([row, col + 1, "*"])
      self.list1.append([row, col - 1, "*"])
      self.list1.append([row + 1, col, "*"])
      self.list1.append([row + 1, col + 1, "*"])
      self.list1.append([row + 1, col - 1, "*"])
      self.list1.append([row - 1, col, "*"])
      self.list1.append([row - 1, col - 1, "*"])
      self.list1.append([row - 1, col + 1, "*"])
    return

  def cell(self, row, col):
    for i in self.list1:
      if (i[0] == row and i[1] == col):
        return i[2]
    return "."


def main():
  # sm = SeaMap()
  # sm.shoot(2, 0, "miss")
  # sm.shoot(6, 9, "miss")
  # sm.shoot(4, 9, "hit")
  # for row in range(10):
  #   for col in range(10):
  #     print(sm.cell(row, col), end=" ")
  #   print()

  sm = SeaMap()
  sm.shoot(0, 0, "sink")
  sm.shoot(0, 9, "sink")
  sm.shoot(9, 0, "sink")
  sm.shoot(9, 9, "sink")
  for row in range(10):
    for col in range(10):
      print(sm.cell(row, col), end=" ")
    print()


if __name__ == '__main__':
  main()
