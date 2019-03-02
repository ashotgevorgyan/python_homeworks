#!/usr/bin/python

# 1. Registration form
"""
  :input username, password, confirm password
  :output: success or error on registration process
"""
print("--------1-----------")

data = {"tiko": "1234", "radik": "23456", "ashot": "56789", "ani": "456", "astxik": "789456", "narine": "123456"}
myusername = input("Please enter an username: ")
if myusername in data:
  mypassword = input("Please enter an password: ")
  if mypassword == data[myusername]:
    print("Hello", myusername)
  else:
    print("Invalid password")
else:
  acc = input("Would you like to register(Y/N): ")
  if (acc == "N" or acc == "n"):
    print("Good luck to you!!!")
  if (acc == "Y" or acc == "y"):
    mypassword = input("Please enter an password: ")
    mypassword1 = input("Please re-enter an password: ")
    if (mypassword == mypassword1):
      data[myusername] = mypassword
      print("You are registred.")
    else:
      print("The passwords are not equal. PLease try again.")

print(data)

# 2. Sentence to Morse. Յուրաքանչյուր տառ փոխարինվում է կետերի և գծիկների հաջորդականությունով։ Որպես գծիկ օգտագործեք «-»,
# իսկ որպես կետ՝ «.» սիմվոլները։ Օրինակ, «g» տառը կվերածվի երեք սիմվոլանոց «--.» տողի։
# Կոդավորված տառերի միջև պետք է դնել ճիշտ մեկ բացատ։ Օրինակ, «Help» բառը կվերածվի «.... . .-.. .--.» տողի։
# Ուշադրություն դարձրեք, որ փոքրատառերը և մեծատառերը նույն կերպ են կոդավորվում։

"""
  :input sentence
  :output: morse code
"""
print("--------2-----------")

sentence = "Mary and Samantha arrived at the bus station early but waited until noon for the bus."
morse_data = {
  'a': '.-',
  'b': '-...',
  'c': '-.-.',
  'd': '-..',
  'e': '.',
  'f': '..-.',
  'g': '--.',
  'h': '....',
  'i': '..',
  'j': '.---',
  'k': '-.-',
  'l': '.-..',
  'm': '--',
  'n': '-.',
  'o': '---',
  'p': '.--.',
  'q': '--.-',
  'r': '.-.',
  's': '...',
  't': '-',
  'u': '..-',
  'v': '...-',
  'w': '.--',
  'x': '-..-',
  'y': '-.--',
  'z': '--..',
}

words = sentence.split()
for i in words:
  for j in i:
    if(j.lower() in morse_data):
      i = i.replace(j, morse_data[j.lower()] + ' ')
  print(i)

# 3.Տրված է բառերից և բացատներից բաղկացած տեքստ։ Բառը տառերի հաջորդականություն է, բառերն իրարից անջատված են մեկ կամ մի քանի բացատներով։
# Տեքստի յուրաքանչյուր բառի համար պարզե՛ք տեքստում այդ բառի տեղի կարգահամարը՝ հենց նույն տեսքով, ինչպես որ տրված է բառը։
# Բառի առաջին գտնված տեղի համար արտածեք «1», նույն բառի երկրորդ գտնված տեղի համար արտածեք «2» և այլն։

print("--------3-----------")

s = "Test test Test Test I can hear test test test Repeat Repeat"
d = {}
w = s.split()
for i in w:
  if(i in d):
    d[i] +=1
  else:
    d[i] = 1
  s = s.replace(i, str(d[i]), 1)
print(s)

# 4. Վասյան ունի N համադասարանցի։ Չկարողանալով հիշել նրանց ծննդյան օրերը Վասյան
# կազմել է դասարանցիների ծննդյան օրերի օրացույցը։:Ունենալով բոլորի ծննդյան օրերի ցուցակը պարզեք,
# թե ում ծննդյան օրն է տրված ամսին։

print("--------4-----------")

friends = {}
list = []
infoCount = int(input("Enter count of rows: "))
for i in range(infoCount):
  info = input("Input name and dob:")
  s = info.split()
  if (s[2] in friends):
    friends[s[2]].append(s[0])
  else:
    friends[s[2]] = [s[0]]
print(friends)
questionsCount = int(input("Questions count: "))
for i in range(questionsCount):
  monthName = input("Enter month name: ")
  if (monthName in friends):
    list.append(friends[monthName])
  else:
    list.append("")

print(list)