from scapy.all import IP, TCP, sr1

# Список целевых IP адресов для сканирования
target_ips = ["192.168.211.172", "192.168.211.173"]  # Замените на ваши IP адреса
# Список портов для сканирования
port_range = [22, 80, 443, 8080]  

# Цикл по каждому целевому IP адресу
for target_ip in target_ips:
    print(f"Scanning {target_ip}...")  # Сообщение о начале сканирования

    # Цикл по каждому порту
    for port in port_range:
        # Создаем TCP пакет с флагом SYN
        ip_packet = IP(dst=target_ip)
        tcp_packet = TCP(dport=port, flags="S")

        # Отправляем пакет и получаем ответ
        response = sr1(ip_packet / tcp_packet, timeout=0.5, verbose=0)

        # Проверяем ответ на наличие флага TCP SYN-ACK
        if response:
            if response.haslayer(TCP) and response[TCP].flags == 18:  # Флаг 18 означает SYN-ACK
                print(f"Port {port} on {target_ip} is open")
            else:
                print(f"Port {port} on {target_ip} is closed")
        else:
            print(f"Port {port} on {target_ip} is filtered")
