# В этом коде мы создаем список целевых IP-адресов и используем цикл for для перебора каждого из них. Для каждого IP-адреса мы отправляем ICMP запрос и обрабатываем ответ, обрабатывая разные типы сообщений, чтобы определить доступность целевого IP.

from scapy.all import IP, ICMP, sr1

# Список целевых IP-адресов
target_ips = ["192.168.211.172", "192.168.211.173", "192.168.211.174"]

# Перебираем каждый IP-адрес в списке
for target_ip in target_ips:
    # Создаем ICMP запрос
    icmp = IP(dst=target_ip)/ICMP()

    # Отправляем пакет и получаем ответ
    response = sr1(icmp, timeout=0.1, verbose=0)

    # Обрабатываем полученный ответ
    if response:
        if response.haslayer(ICMP):
            if response[ICMP].type == 0:  # ICMP Echo Reply
                print(f"IP адрес {target_ip} доступен")
            elif response[ICMP].type == 3:  # ICMP Destination Unreachable
                print(f"IP адрес {target_ip} недоступен (Destination Unreachable)")
    else:
        print(f"IP адрес {target_ip} не ответил на ICMP запрос")
