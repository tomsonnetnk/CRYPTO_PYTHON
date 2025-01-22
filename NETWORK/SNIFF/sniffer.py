# В данном коде реализован простой сканер открытых портов. Мы создаём список IP-адресов для сканирования и диапазон портов. С помощью циклов for проходим по каждому IP и порту, проверяя его доступность с помощью метода connect_ex() сокета. При успешном соединении выводим сообщение о том, что порт открыт.
import socket

def scan_ports(targets, port_range):
    for target in targets:  # Итерация по списку целей
        print(f"Сканирование {target}...")
        for port in port_range:  # Итерация по диапазону портов
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Создаем сокет
            sock.settimeout(1)  # Устанавливаем время ожидания
            result = sock.connect_ex((target, port))  # Проверяем подключение к порту
            if result == 0:  # Порт открыт
                print(f"Порт {port} открыт на {target}")
            sock.close()  # Закрываем сокет

# Спецификация целей и диапазона портов
targets = ["192.168.1.1", "192.168.1.2"]
port_range = range(1, 1025)  # Сканируем порты с 1 по 1024

# Запуск сканера
scan_ports(targets, port_range)
