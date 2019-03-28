# NUMBERS
numbers = []
for i in range(5):
    number = int(input("Please enter "))
    numbers.append(number)
print("The first numbers is ",numbers[0])
print("The last numbers is ",numbers[-1])
print("The smallest numbers is ", min(numbers))
print("The largest numbers is ", max(numbers))
print("The average of the numbers is ", sum(numbers) / len(numbers))


#  WOEFULLY

user_names = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("Enter username: ")
if username in user_names:
    print("Access granted")
else:
    print("Access denied")


