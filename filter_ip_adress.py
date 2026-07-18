def is_suspicious(ip):
    if ip[:4] == "127.":
        return True
    else:
        return False


ip_list = ["192.168.1.1", "127.0.0.1", \
           "10.0.0.5", "127.0.0.254", "185.22.4.5"]
print(ip_list)
fake_name = []
true_name = []

for n in range(len(ip_list)):
    ip = ip_list[n]
    if is_suspicious(ip):
        true_name.append(ip)
    else:
        fake_name.append(ip)
    print(f"{n+1}: {ip} = {is_suspicious(ip)}")

print(f"\n---Проверено {len(ip_list)} адресов---")
print(f"\n---Из них оказалось в порядке {len(true_name)}, а подозрительных \
{len(fake_name)}---")

input("Нажмите Enter для завершения программы")
