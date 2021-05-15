import os
import json

##################################################
"""
1. Написать функцию, которая получает в виде параметра имя файла названия интернет доменов (domains.txt)
и возвращает их в виде списка строк (названия возвращать без точки).
"""


def take_data(filename):
    with open(filename, "r") as txt_file:
        data = txt_file.read()
        data = data.split("\n")
    return data


def create_list_data(filename):
    res_list = [names[1:] for names in take_data(filename)]
    return res_list


##################################################
"""
2. Написать функцию, которая получает в виде параметра имя файла (names.txt)
и возвращает список всех фамилий из него.
Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
Разделитель - символ табуляции "\t"
"""


def take_data_surname(filename):
    with open(filename, "r") as txt_file:
        data = txt_file.readlines()
    return data


def create_surname_list(filename):
    res_list = [surname.split("\t")[1] for surname in take_data_surname(filename)]
    return res_list


##################################################
"""
3. Написать функцию, которая получает в виде параметра имя файла (authors.txt) и возвращает список
словарей вида {"date_original": date_original, "date_modified": date_modified}
в которых date_original - это дата из строки (если есть),
а date_modified - эта же дата, представленная в формате "dd/mm/yyyy" (d-день, m-месяц, y-год)
Например [{"date_original": "8th February 1828", "date_modified": 08/02/1828},  ...]
"""


def take_data_date(filename):
    with open(filename, "r") as txt_file:
        data = txt_file.read()
        data = data.split("\n")
    return data


def create_dict(filename):
    res_list = []
    for date in take_data_date(filename):
        res_list.append(date[])
    return res_list


file_name_1 = "Homework9_files/domains.txt"
file_name_2 = "Homework9_files/names.txt"
file_name_3 = "Homework9_files/authors.txt"
result_1 = create_list_data(file_name_1)
result_2 = create_surname_list(file_name_2)
result_3 = create_dict(file_name_3)
print(result_1)
print(result_2)
print(take_data_date(file_name_3))
print(result_3)
