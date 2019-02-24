#!/usr/bin/python 3.7.2
# 1. Ծրագիրը պետք է թույլ տա մուտքագրել թիվ և բառ։ Որից հետո այն պետք է թույլ տա մուտքագրել այդ թվի քանակությամբ
# նախադասություններ և պետք է տպի, թե քանի անգամ է այդ բառը հանդիպել նախադասություններում

a = int(input('nermucek naxabasutyuneri qanak: '))
b = []
c = input('nermucek stugvox bar: ')
for i in range(a):
  ms = input('nermucek naxadasutyun: ')
  d = ms.count(c)
  b.append(ms + ":" + str(d))
print('\n'.join(b))

#  2. Ծրագիրը պետք է թույլ տա մուտքագրել թիվ, որից հետո այդ թվի քանակությամբ տողեր։
#  Պետք է արտածել մուտքագրված տողերը հակառակ ուղությամբ։

a = int(input('nermucek naxabasutyuneri qanak: '))
b = []
for i in range(a):
  ms = input('nermucek naxadasutyun: ')
  b.append(ms)
b.reverse()
print('\n'.join(b))

# 3.Ծրագրում ունենք տող։ Պետք է ունենանք հնարավորություն մուտաքագրել թվեր այնքան ժամանակ քանի դեռ չենք մուտքագրել End բառը
# ։ Պետք է տպի նախադասությունում տվյալ թվի դիրքում եղած բառը։Պետք է տպի նախադասությունում տվյալ թվի դիրքում եղած բառի
# եղած տառը, եթե կա այդպիսին, եթե ոչ "No":

a = 'A new report on the state of American youth says teenagers are very ' \
    'concerned about the direction their nation is taking.'
l = a.split()
b = input('nernucek tiv: ')
if (int(b) < len(l) and int(b) < len(l[int(b)])):
  while (b != "end" and b != 'End'):
    print(l[int(b)][int(b)])
    b = input()
else:
  print('nermucvac tiv mec e')
print('finish')
