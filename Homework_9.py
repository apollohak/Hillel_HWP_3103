FILE_NAME = "Homework9_files/authors.txt"

##################################################
"""
1. Написать функцию, которая получает в виде параметра имя файла названия интернет доменов (domains.txt)
и возвращает их в виде списка строк (названия возвращать без точки).
"""


def open_domains_file(filename):
    with open(filename, "r") as txt_file:
        data = txt_file.readlines()
    return data


def create_domains_list(filename):
    res_list = [name.replace(".", "")[:-1] for name in open_domains_file(filename)]
    return res_list


##################################################
"""
2. Написать функцию, которая получает в виде параметра имя файла (names.txt)
и возвращает список всех фамилий из него.
Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
Разделитель - символ табуляции "\t"
"""


def open_names_file(filename):
    with open(filename, "r") as txt_file:
        data = txt_file.readlines()
    return data


def create_surname_list(filename):
    res_list = [surname.split("\t")[1] for surname in open_names_file(filename)]
    return res_list


##################################################
"""
3. Написать функцию, которая получает в виде параметра имя файла (authors.txt) и возвращает список
словарей вида {"date_original": date_original, "date_modified": date_modified}
в которых date_original - это дата из строки (если есть),
а date_modified - эта же дата, представленная в формате "dd/mm/yyyy" (d-день, m-месяц, y-год)
Например [{"date_original": "8th February 1828", "date_modified": 08/02/1828},  ...]
"""


def open_authors_file(fielname=FILE_NAME):
    with open(fielname, "r") as txt_file:
        data = txt_file.readlines()
    return data


def create_split_date_list():
    result = []
    for data in open_authors_file():
        data = data.split("-")[0]
        data = data.split()
        if len(data) == 3:
            result.append(data)
    return result


def create_modified_dictionaries():
    result = []
    for data in create_split_date_list():
        data_dd = data[0]
        data_dd = data_dd[:-2]
        if len(data_dd) == 1:
            data_dd = "0" + data_dd
        result.append({"date_original": " ".join(data),
                       "date_modified": f"{data_dd}/{months_dict.get(data[1])}/{data[2]}"})
    return result


file_name_1 = "Homework9_files/domains.txt"
file_name_2 = "Homework9_files/names.txt"

months_dict = {'January': '01',
               'February': '02',
               'March': '03',
               'April': '04',
               'May': '05',
               'June': '06',
               'July': '07',
               'August': '08',
               'September': '09',
               'October': '10',
               'November': '11',
               'December': '12'}

result_1 = create_domains_list(file_name_1)
result_2 = create_surname_list(file_name_2)
result_3 = create_modified_dictionaries()
