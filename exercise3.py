## exercise 3
##sTring = "This is exercise three"
##string_2 = "I also learning python"
##print(len(sTring))
##print(sTring + " " + string_2)
##string_3 = "bazinga"
##print(string_3[2:-1])


## exercise for ai

##word = input("word... please:  ")
##
##if word[0].lower() == word[-1].lower():
##    print("буквы совпали!")
##else:
##    print("Буквы не совпали!")


##number = input("ведите номер телефона:  ")
##if number and number[0] == "+" and len(number) >= 12:
##    print("Ваш код страны:" + number[:2])
##else:
##    print("Пожалуйста введите номер начиная с \"+\"; \
##Либо введите номер полностью")


##word_1 = "Питон"
##word_2 = "Кипарис"
##word_3 = "Словарь"
### Нужно составить слово "Писарь"
##find_word = word_1[:2] + word_2[-1] + word_3[-3:]
##print(find_word)

word_user = input("Please enter secret word: ")
if word_user and word_user.lower() == word_user[::-1].lower():
    print(word_user + " this word is palindrom")
else:
    print(word_user + " This word is not polindrom")

