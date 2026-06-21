# 4.4 Взаимодействие с пользовательским вводом

##user_input = input("Hey Honey, what do you like? ")
##response = user_input
##print("You said: " + response)
### Выводим в нижнем регистре
##print("He said it again, but quietly; " + response.lower())
### Выводим колво символов в строке
##print(len(response))


## 4.5 Задача: разбор пользовательского ввода
##
##user_password = input("Tell me your password: ")
##
## Забираем первый символ и выводим его в верхнем регистре
##letter_1 = user_password[0:2]
##print(letter_1.upper())
##if letter_1.upper == "NO":
##    print("You entered \"no\"! ")
##
##
##
## 4.6 Работа со строками и числами
##
##num = input("Enter a namber to be doubled: ")
##doubled_num = float(num) * 2
##print(doubled_num)

num = "10"
num_int = int(num)
num_mult = num_int * 20
print(num_mult)

num_2 = "3"
num_float = float(num_2)
num_mult_2 = num_float * 3
print(num_mult_2)

num_3 = 4
string = "tickets"
print(str(num_3) + " " + string)

num_4 = input("please enter number 1: ")
num_5 = input("please enter number 1: ")
print("The product of" + num_4 + " and " + num_5 + " is " + str(int(num_4) * float(num_5)))
