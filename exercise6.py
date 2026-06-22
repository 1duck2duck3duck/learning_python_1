# 4.7 Упрощение команд вывода
##weight = 0.2
##animal = "newt"
##print(str(weight) + " kg is the weight of the " + animal + ".")
##print("{} kg is the weight of the {}.".format(weight, animal))
##print(f"{weight} kg is the weight of the {animal}.")

user_name = "dack1dack2dack3"
status = "Технически готов"
current_chapter = 4.7
dog_name = "Pickachu"
learning_times = 15
target_senior_hours = 5000
learn_in_day = 3
junior_hours = 500
print(f"Если в день заниматься {learn_in_day}, то статуса \"Junior\"(\
{junior_hours} часов) можно достичь за {round((junior_hours / learn_in_day), 1)} дней, \
а \"Senior\" за {round((target_senior_hours / learn_in_day), 1)} дней. Надеюсь {dog_name} \
придаст мне сил")


print(f"Пользователь: {user_name} | Статус: {status} | Глава в книге: {current_chapter} |")
