import json
import re

"""
1. Необходимо написать функцию, которая считает эти данные из файла. Параметр функции - имя файла.
"""


def reads_json_data(filename):
    with open(filename, 'r', encoding="utf-8") as json_file:
        data = json.load(json_file)
        return data


##################################################

"""
2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
Например для Rene Descartes фамилия это Descartes, у Pierre de Fermat - Fermat и т.д.
Если фамилии нет, то использовать имя, например Euclid.
"""


def sort_by_surname(pers_dict):
    return pers_dict['name'].split()[-1]


##################################################

"""
3. Написать функцию сортировки по дате смерти из поля "years".
Обратите внимание на сокращение BC. - это означает до н.э.
"""


def sort_by_death_year(pers_dict):
    year = pers_dict['years']
    age = int(re.findall(r'[0-9]+', year)[-1])
    if "BC" in year:
        age = -1 * age
    return age


##################################################

"""
4. Написать функцию сортировки по количеству слов в поле "text"
"""


def sort_by_count_word(pers_dict):
    return len(pers_dict['text'].split())


file_name = "data.json"

persons = reads_json_data(file_name)

surname = sorted(persons, key=sort_by_surname)

death_year = sorted(persons, key=sort_by_death_year)

count_word = sorted(persons, key=sort_by_count_word)
