#!/usr/bin/python 3.7.2
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
