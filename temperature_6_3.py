def convert_cel_to_far(celcius):
    """Конвертирует Цельсий в Фаренгейт"""
    fahrenheit = float(celcius * 9 / 5 + 32)
    return fahrenheit

def convert_far_to_cel(fahrenheit):
    """Конвертирует Фаренгейт в Цельсий"""
    celcius = float((fahrenheit -32) * 5 / 9)
    return celcius


#Запрашиваем у пользователя фаренгейт чтоб перевести в цельсий
fahrenheit = int(input("Enter a temperature in degrees F:  "))
print(f"{fahrenheit} degrees F = {convert_far_to_cel(fahrenheit):.2f} \
degrees C")


#Запрашиваем у пользователя цельсий чтоб перевести в фаренгейт
celcius = int(input("Enter a temperature in degrees C:  "))
print(f"{celcius} degress C = {convert_cel_to_far(celcius):.2f} \
degrees F")
