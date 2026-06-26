## 5.4. Когда Python говорит неправду
## В этой подглаве описывается погрешность при употреблении мелких
## значений таких как: 0.1; 0.2; 0.3 ... и так далее


##5.5. Математические функции и числовые методы
##1) round() для округления чисел до заданной точности;
##    Чтобы функция round() округлила до определенного значения нужно
##    после запятой передать 2 аргумент к примеру round(3.14159, 3)
##    Выведет 3.142

##2) abs() для получения абсолютного значения (модуля) числа;
## к примеру abs(-5) - 5; abs(3) - 3

##3) pow() для возведения числа в степень.
## К примеру pow(2, 3) - 8 (2 в степени 3)
## Так же можно добавить 3-ий аргумент, что приведет к проверке на остаток от деления
##пример: pow(2, 3, 2) - 0; очно так же можно представить в виде: 2**3%2 - 0

## Mетод .is_integer(), который возвращает True, если число является целым,
## то есть не имеет дробной части.
##num = 2.5
##print(num.is_integer())#False
##num = 2.0
##print(num.is_integer())#True
##

## exercise
##num_user_input = float(input("Введите число для округления:  "))
##print(f"{num_user_input} rounded to 2 demical place {round(num_user_input, 2)}")
##
##user_num = float(input("Enter num for abs"))
##print(f"The absolute value of {user_num} is {abs(user_num)}.")

##user_num_input_1 = float(input("Enter 1 num for integer check after subtraction"))
##user_num_input_2 = float(input("Enter 2 num for integer check after subtraction"))
##subtractions_nums = user_num_input_1 - user_num_input_2
##print(f"The difference between {user_num_input_1} and {user_num_input_2} is an integer?  {subtractions_nums.is_integer()}!")
