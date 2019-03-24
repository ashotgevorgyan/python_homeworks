#!usr/bin/python

# 1. Գրե&#39;լ BigBell դասը, որը sound մեթոդի կանչի ժամանակ տպում է փոխ առ փոխ ding և dong բառերը,
# սկսելով ding-ից։

class BigBell:
  def __init__(self):
    self.count = 0

  def sound(self):
    self.count += 1
    if (self.count % 2 == 0):
      print("dong")
    else:
      print("ding")


# 2. Գրել MinMaxWordFinder դասը։ Այն պետք է կարողանա վերլուծել տեքստը և գտնել նրանում
# ամենամեծ և ամենափոքր երկարությամբ բառերը։ Տեքստը բաղկացած է նախադասություններից, որոնք
# ավելացվում են մշակման համար add_sentence մեթոդով։ shortest words մեթոդը վերադարձնում է
# տվյալ պահին ամենակարճ, longest_words մեթոդը՝ ամենաերկար, բառերի ցուցակը։ shortest_words-ի և
# longest_words-ի վերադարձրած բառերը պետք է տեսակավորված լինեն այբբենական կարգով։
# Եթե ամենակարճ բառերից մեկը հանդիպել է տրված նախադասություններում մի քանի անգամ, այն պետք է
# նույնքան անգամ կրկնվի ամենակարճ բառերի ցուցակում։ Ամենաերկար բառերն, ընդհակառակը, պետք է
# ցուցակի մեջ մտնեն առանց կրկնությունների։

class MinMaxWordFinder:
  def __init__(self):
    self.list = []

  def add_sentence(self, a):
    self.list.extend(a.split())

  def shortest_words(self):
    min = len(self.list[0])
    for i in range(len(self.list)):
      if (len(self.list[i]) < min):
        min = len(self.list[i])
    b = filter(lambda x: len(x) == min, self.list)
    return list(b)

  def longest_words(self):
    max = len(self.list[0])
    for i in range(len(self.list)):
      if (len(self.list[i]) > max):
        max = len(self.list[i])
    c = filter(lambda x: len(x) == max, self.list)
    return set(c)


def main():
  bell = BigBell()
  bell.sound()
  bell.sound()
  bell.sound()

  finder = MinMaxWordFinder()
  finder.add_sentence("hello abc the world asdfg")
  finder.add_sentence("def asdf the qwert asdfg")
  print(" ".join(finder.shortest_words()))
  print(" ".join(finder.longest_words()))

if __name__ == "__main__":
  main()
