import socket

def scan_ports(target_ips, ports):
    # Проходим по каждому IP адресу из списка
    for target_ip in target_ips:
        print(f"Сканирование портов для {target_ip}:")
        # Проходим по каждому порту
        for port in ports:
            # Создаем сокет
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # Устанавливаем таймаут 1 секунда

            # Пытаемся подключиться к порту
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                print(f"Порт {port} открыт")
            else:
                print(f"Порт {port} закрыт")
            sock.close()  # Закрываем сокет

# Задаем список целей и портов для сканирования
targets = ["192.168.1.150", "192.168.1.151"]
ports_to_scan = [22, 80, 443]

# Запускаем сканирование
scan_ports(targets, ports_to_scan)

Данный код реализует сканер открытых портов для списка IP адресов. Указаны IP адреса и порты, которые будут просканированы. Внутри цикла мы пробуем установить соединение с каждым портом и выводим результат.
