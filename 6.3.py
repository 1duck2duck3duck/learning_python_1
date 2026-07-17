##x = "Hello World"
##def func():
##    x = 2
##    print(f"Inside 'func', x has the value {x}")
##
##func()
##print(f"Outside 'func', x has the value {x}")


#Игра сейф

correct_pin = 4626
attempts_left = 3

while attempts_left > 0:
    user_pin = int(input("Your password:  "))
    if user_pin != correct_pin :
        attempts_left -=1
        if attempts_left > 0:
            print(f"Try again. Left: {attempts_left}")
    else:
        print("Сейф открыт")
        break
else:
    print("safe is closed")
