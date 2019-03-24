# !usr/bin/python
import datetime


class Time:
  def __init__(self, h, m, s):
    self.h = h
    self.m = m
    self.s = s

  def add_hours(self, hours):
    self.h += hours % 24
    if (self.h > 24):
      self.h = hours % 24

  def add_minutes(self, minutes, add_from_second=False):
    if (not add_from_second):
      self.m += minutes
    if (self.m > 60):
      self.h += self.m // 60
      self.m = self.m % 60
    self.add_hours(self.h)

  def add_seconds(self, seconds):
    self.s += seconds
    if (self.s > 60):
      self.m += self.s // 60
      self.s = self.s % 60
    self.add_minutes(self.m, True)

  def decrease_hours(self, hours):
    self.h -= hours % 24
    if (self.h < 0):
      self.h += 24

  def decrease_minutes(self, minutes, decrease_from_seconds=False):
    if (not decrease_from_seconds):
      self.m -= minutes
    if (self.m < 0):
      self.h -= (abs(self.m) // 60) + 1
      self.m = 60 - (abs(self.m) % 60)

  def decrease_seconds(self, seconds):
    self.s -= seconds
    if (self.s < 0):
      self.m -= (abs(self.s) // 60) + 1
      self.s = 60 - (abs(self.s) % 60)
    self.decrease_minutes(self.m, True)

  def __str__(self):
    return "%d:%d:%d" % (self.h, self.m, self.s)


def main():
  d = datetime.datetime.now()
  t = Time(d.hour, d.minute, d.second)
  print(t)
  q1 = input("What do you want to do(add(a)/decrease(d))? ")
  if (q1 == "a"):
    q2 = input("What do you want to add(h/m,s)? ")
    if (q2 == "h"):
      t.add_hours(int(input("Enter hours here: ")))
    elif (q2 == "m"):
      t.add_minutes(int(input("Enter minutes here: ")))
    elif (q2 == "s"):
      t.add_seconds(int(input("Enter seconds here: ")))
    else:
      print("Invalid option")
  elif (q1 == "d"):
    q2 = input("What do you want to decrease(h/m,s)? ")
    if (q2 == "h"):
      t.decrease_hours(int(input("Enter hours here: ")))
    elif (q2 == "m"):
      t.decrease_minutes(int(input("Enter minutes here: ")))
    elif (q2 == "s"):
      t.decrease_seconds(int(input("Enter seconds here: ")))
    else:
      print("Invalid option")
  print(t)


if __name__ == "__main__":
  main()
