def convert_cel_to_far():
    """Конвертирует Цельсий в Фаренгейт"""
    fahrenheit = float(C * 9 / 5 + 32)
    return fahrenheit

def convert_far_to_cel():
    """Конвертирует Фаренгейт в Цельсий"""
    celcius = float((F -32) * 5 / 9)
    return celcius

def check_input_C():
    """Проверка введенного Ц"""
    if type(C) != float:
        print("Please relaunch programm and enter num!!!")
    else:
        print(convert_cel_to_far())

def check_input_F():
    """Проверка введенного F"""
    if type(F) != float:
        print("Please relaunch programm and enter num!!!")
    else:
        print(convert_far_to_cel())

F_or_C = input("Please select a conversion(C to F or F to C):  ").upper()

#Перевод из С в Ф
if F_or_C == "C TO F":
    C = float(input("Please enter C: "))
    print(check_input_C())
    
#Перевод из Ф в С
elif F_or_C == "F TO C":
    F = float(input("Please enter F: "))
    print(check_input_F())
    
# Защита от дураков
else:
    print("Incorrectly entered data. Try again.")
