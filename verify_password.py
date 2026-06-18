

import string

def check_strenght(password):
    score = 0



    if len(password) >=12:
        score +=2
        print("Is amazing: (len char 12+)")
    elif len(password) >=8:
        score += 1
        print("Длина пароля:(8+ символов)")
    
    else:
        print("Длина пароля: Плохо(Слишком короткий)")
    ##Проверка длины пароля

        

    if any(char.isdigit() for char in password):
        score += 1
        print("Цифры присутсвуют")
    else:
        print("Добавьте хоть одну цифру")

        
    ##Проверка цифрверхний регистр
    if any(apper_case.isupper() for apper_case in password):
        score += 1
        print("Заглавная буква есть!")
    else:
        print("Добавьте заглавную букву!")
    

    ## Проверка спец символов
    if any(spec_char in string.punctuation for spec_char in password):
        score += 1
        print("character is here")
    else:
        print("Characters in not here") 
    

    print(score)
user_password = input("Please, enter your password \
to verify:")
check_strenght(user_password)


