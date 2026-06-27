##5.6. Оформление чисел при выводе
##n = 7.937
##print(f" The value of n is {n}")
# Что бы округлить число до определенного значения следует поставить ":"
# а после точку и цифру до какого значения нужно округлить
# В данном случае это 2, так же ставится "f" для того что бы было 2 знака после запятой даже если их было меньше
##print(f" The value of n is {n:.2f}")#Выведет 7.93
##print(f" The value of n is {n:.6f}")#Выведет 7.937000

##Если мы хотим отформатировать большое число так, чтобы разряды в нем
##разделялись запятыми, то нужно добавить запятую внутрь фигурных скобок
##n = 12864521875418292864189
##print(f"The value of n is {n:,}")

# Что бы сдалать и то и другое то нужно использовать два метода:
##n = 432364.8372862386
##print(f"The value of n is {n:,.2f}")

# Пример использования:
##balance = 2000.0
##spent = 256.35
##remaining = balance - spent
##print(f"After spending ${spent:.2f}, I was left with ${remaining:,.2f}")


## exercise
##n = pow(3, .125)
##print(f"n = {n:.3f}")
##cash = 150000
##print(f"Your cash: ${cash:,.2f}")
##persone_wins = 2/10
##print(f"The our team wins persone: {persone_wins:.0%}")
##


# exercise ai
hash_1 = "a1b2c3d4"
hash_input = input("Please entering your hash:  ").strip()

if hash_1 == hash_input:
    print(f"[SUCCESS]: Your hach \"{hash_input}\" is secure!")
else:
    print(f"[ERROR]: Your hash \"{hash_input}\" changed!")



distance_to_swith = 42.3
allowance = 2.7
pc = 9

print(f"Required cable length: {(distance_to_swith * pc):.2f}m., and length is allowance: {(allowance * pc):.2f} m.")
