correct_login = "admin"
correct_password = "12345admin"
user_login = input("enter your login:  ")
user_password = input("enter your password:  ")

if correct_login == user_login and correct_password == user_password:
    print("[ACCESS GRANTED] Успешный вход в систему. Доступ к настройкам Wi-Fi\
открыт!")
else:
    print("[AUTH FAILED] Неверный логин или пароль!")



isp1_status = input("enter your status isp1(online or offline):  ")
isp2_status = input("enter your status isp2(online or offline):  ")
isp2_type = input("enter your type connect(mobile or unlimited):  ")
critical_mode = int(input("enter on or off your economy(1 or 0):  "))

if isp1_status == "offline" and isp2_status == "offline":
    print("[ALERT] Полный блекаут! Связь отсутствует!")
elif isp1_status == "offline" and isp2_type == "unlimited" and isp2_status == "online":
    print("[BACKUP] Переключено на резервный проводной канал.")
elif isp1_status == "offline" and isp2_type == "mobile" and critical_mode == 0:
    print("[WARNING] Основной канал упал. Переключено на дорогой мобильный трафик!")
elif isp1_status == "offline" and isp2_type == "mobile" and critical_mode == 1:
    print("[STOP] Основной канал упал. Мобильный резерв заблокирован режимом экономии!")
elif isp1_status == "online":
    print("[OK] Работаем на основном канале.")
else:
    print("[ERROR] Ошибка конфигурации системы")
