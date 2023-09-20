# -*- coding: utf-8 -*-
"""
Задание 17.1

Создать функцию write_dhcp_snooping_to_csv, которая обрабатывает вывод
команды show dhcp snooping binding из разных файлов и записывает обработанные
данные в csv файл.

Аргументы функции:
* filenames - список с именами файлов с выводом show dhcp snooping binding
* output - имя файла в формате csv, в который будет записан результат

Функция ничего не возвращает.

Например, если как аргумент был передан список с одним файлом sw3_dhcp_snooping.txt:
MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
------------------  ---------------  ----------  -------------  ----  --------------------
00:E9:BC:3F:A6:50   100.1.1.6        76260       dhcp-snooping   3    FastEthernet0/20
00:E9:22:11:A6:50   100.1.1.7        76260       dhcp-snooping   3    FastEthernet0/21
Total number of bindings: 2

В итоговом csv файле должно быть такое содержимое:
switch,mac,ip,vlan,interface
sw3,00:E9:BC:3F:A6:50,100.1.1.6,3,FastEthernet0/20
sw3,00:E9:22:11:A6:50,100.1.1.7,3,FastEthernet0/21

Первый столбец в csv файле имя коммутатора надо получить из имени файла,
остальные - из содержимого в файлах.

Проверить работу функции на содержимом файлов sw1_dhcp_snooping.txt,
sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt.

"""
import re
import csv
import glob


def write_dhcp_snooping_to_csv(filenames, output):
    regex = r"(\S+) +(\S+) +\d+ +\S+ +(\S+) +(\S+)"
    with open(output, "w") as pu:
        wr=csv.writer(pu)
        wr.writerow(["switch","mac", "ip","vlan", "interface"])
        for files in filenames:
            sw_name = re.search("(\S+)_dhcp_snooping.txt",files).group(1)
            with open (files) as f:
                for line in f:
                    match = re.search(regex,line)
                    if match:
                        wr.writerow((sw_name,)+match.groups())

if __name__=="__main__":
    sh_dhcp_snoop_files = glob.glob("*_dhcp_snooping.txt")
    write_dhcp_snooping_to_csv(sh_dhcp_snoop_files,"test_test.csv")















