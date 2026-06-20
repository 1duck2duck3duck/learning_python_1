##name = "Picard"
##print(name.upper())
##print(name)
##name  = name.upper()
##print(name)


##starship = "Enterprise"
##word_1 = "Animals"
##word_2 = "Badger"
##word_3 = "HoneyBee"
##word_4 = "HoneyBadger"
##print(word_1.lower(), word_2.lower(), word_3.lower(), word_4.lower(), sep = '\n')
##print(word_1.upper(), word_2.upper(), word_3.upper(), word_4.upper(), sep = '\n')
##
##
##string1 = "   Filet Mignon"
##string2 = "Brisket   "
##string3 = "  Cheeseburger  "
##print(string1.lstrip(), string2.rstrip(), string3.strip(), sep = '\n')
##
##string1 = "Becomes"
##string2 = "becomes"
##string3 = "BEAR"
##string4 = "bEautiful"
##print(string1.startswith("be"), string2.startswith("be"), string3.startswith("be"), \
##      string2.startswith("be"))
##string1 = string1.lower()
##string2 = string2.lower()
##string3 = string3.lower()
##string4 = string4.lower()
##print(string1.startswith("be"), string2.startswith("be"), string3.startswith("be"), \
##      string2.startswith("be"))


##secret_message = input("Сообщение:  ")
##secret_message = secret_message.strip()
##secret_message = secret_message.lower()
##if secret_message.find("секрет") != -1:
##    print("Возможно наличие конфендициальной информации!")
##else:
##    print("Всё в порядке")


message_user = input("Cообщение:  ")
if message_user.startswith("//http") or message_user.startswith("//htpps"):
    print("message have is spam")
else:
    message_user = message_user.replace("?", "").replace("!", "")
    print(message_user)
