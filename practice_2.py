port_status = input("Enter your status port(open,closed):  ").lower()
os_version = input("Enter is your os version('ubuntu_old;''ubuntu_current;'\
'windows'):  ").lower()
aunt_attempts = int(input("Enter is your lose entering:  "))
is_encrypted = int(input("Is on encrypted?(1, 0):  "))

if is_encrypted not in (1, 0):
    print("Please enter ecrypted of correct! (1 or 0)")
else:
# Проверка взлом старой системы и открытый порт без шифрования
    if port_status == "open" and is_encrypted == 0 or os_version == "ubuntu_old" and aunt_attempts >= 10:
        print("[CRITICAL]: Критическая уязвимость! Срочно принять меры!")

# Проверка на кол-во ошибок ввода, версию, порт, шифрование для оповещения средней опасности
    elif (5 <= aunt_attempts <=9) or (port_status == "closed" and is_encrypted == 0) or (port_status == "open" \
         and (os_version == "ubuntu_current" or os_version == "windows") and is_encrypted == 1):
        print("[WARNING]: Обнаружены средние риски безопасности.")

# Проверка порта, шифрования и ошибок ввода, для оповещения целостности безопасности
    elif port_status == "closed" and is_encrypted == 1 and aunt_attempts <= 5:
        print("[SAFE]: Система в безопасности. Сканирование завершено.")

#Если введены неверные данные
    else:
        print("[ERROR]: Ошибка сканирования. Некорректные параметры.")
