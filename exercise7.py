# 4.8 Поиск подстроки в строке

# .find() Находит подстроку в подстроке
# Выводит индекс найденого(В данном случае 4)
##phrase = "the surprise is in here somewhere"
##print(phrase.find("surprise"))

# .find() выведет -1 при том случае если ничего не найдет
##print(phrase.find("dbbiewidb"))

# .replace - Заменяет каждое вхождение подстроки новой строкой
##my_story = "I'm telling you the truth; nothing but the truth!"
##print(my_story.replace("the truth", "lies"))

# Строки являются НЕИЗМЕННЫМИ объектами, что бы изменить переменную,
# нужно присвоить значение с строковым методом(.find(); .replace()) в переменную.
##print(my_story)
##my_story = my_story.replace("the truth", "lies")
##print(my_story)


# exercise
##char = "AAA"
##print(char.find("a"))
##
##string = "Somebody said something to Samantha"
##new_string = (string.replace("s", "x")).replace("S", "X") 
##print(new_string)
##
##user_input = input("Прошу введите любую фразу:  ")
##print(user_input.find("п"))


## 4.9 Задача: преобразование текста
##phrase = input("Enter some text:  ")
##cipher_phrase = ((((((phrase.replace("a", "4")).replace("b", "8")).replace("e", "3"))\
##                .replace("l", "1")).replace("o", "0")).replace("s", "5")).replace("t", "7")
##print(cipher_phrase)
