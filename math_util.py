#!/usr/bin/python
# 1. Math simple actions
"""
  :input a, b
  :output: a+b, a-b, a*b, a/b
"""
def mathActions(a, b):
  add = a + b
  minus = a - b
  mult = a * b
  div = a / b
  return ('Addition is ' + str(add), 'Subtraction is ' + str(minus),
          'Multiplication ' + str(mult), 'Division is ' + str(div))

print('\n'.join(mathActions(10, 5)))

# 2. Summary
"""
  :input numbers list
  :output: summary of numbers
"""
def sum(*a):
  s = 0
  for i in a:
    s += int(i)
  return s

print(sum(1, 3, '5', 6))

# 3. Power of number
"""
  :input a, b
  :output: pow(a, b)
"""
def myPower(a, b):
  p=1
  for i in range(b):
    p*=a
  return p

print(myPower(2,5))

# 4. Factorial of number
"""
  :input a
  :output: a!
"""
def myFactorial(a):
  b=1
  for i in range(1,a+1):
    b=b*i
  return b

print(myFactorial(5))

# 5. Fibonacci sequence
"""
  :input number of Fibonacci sequence 
  :output: list of numbers from Fibonacci sequence 
"""
def myFibonacci(a):
  list = []
  for i in range(a):
    if (i == 0 or i == 1):
      list.append(i)
    else:
      list.append(list[i - 1] + list[i - 2])
  return list

print(myFibonacci(20))
