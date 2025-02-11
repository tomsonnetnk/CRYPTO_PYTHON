# Для отслеживания только TCP SYN пакетов с использованием BPF, мы можем использовать следующий фильтр: tcp[tcpflags] == tcp-syn. В данном фильтре мы проверяем значения флагов TCP, чтобы отфильтровать только пакеты с флагом SYN, который устанавливается в 1, когда осуществляется начало TCP-соединения.

#Используем Scapy для создания сетевого сниффера. Вот пример кода:

from scapy.all import *

# Функция для обработки захваченных пакетов

def process_packet(packet):
    if TCP in packet and packet[TCP].flags == 'S':
        print(f"SYN пакет от {packet[IP].src} к {packet[IP].dst}")

# Устанавливаем фильтр для захвата только TCP SYN пакетов

sniff(filter="tcp[tcpflags] == tcp-syn", prn=process_packet, store=0)

# В этом коде:
# Мы используем функцию sniff для захвата пакетов.
# Фильтр tcp[tcpflags] == tcp-syn гарантирует, что будут перехвачены только SYN пакеты.
# Функция process_packet обрабатывает каждый найденный пакет и выводит IP-адреса отправителя и получателя.
# Не забудьте запускать скрипт с правами администратора, чтобы получить доступ к сети.
