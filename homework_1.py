#!/usr/bin/python 3.7.2

# Ծրագիրը թույլ է տալիս ներմուծել անուն,ազգանուն,ծննդյան տարեթիվ։
# Տպում է անուն,ազգանուն,տարիքը։
name = input("Please enter your name\n")
surname = input("Please enter your surname\n")
date = input("Please enter your birth of date\n")
age = 2019 - int(date)
print(name + ' ' + surname + ' ' + 'You are ' + str(age) + ' years old')