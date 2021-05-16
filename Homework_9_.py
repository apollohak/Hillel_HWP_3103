FILE_NAME = "Homework9_files/authors.txt"

##################################################
"""
1. Написать функцию, которая получает в виде параметра имя файла названия интернет доменов (domains.txt)
и возвращает их в виде списка строк (названия возвращать без точки).
"""


def take_data(filename):
    with open(filename, "r") as txt_file:
        data = txt_file.readlines()
    return data


def create_list_data(filename):
    res_list = [names[1:-1] for names in take_data(filename)]
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


def take_data_date(FILE_NAME):
    with open(FILE_NAME, "r") as txt_file:
        data = txt_file.readlines()
    return data


def create_split_list():
    res = []
    for data in take_data_date(FILE_NAME):
        data = data.split("-")[0]
        data = data.split()
        if len(data) == 3:
            res.append(data)
    return res


def create_modif_mm():
    dict_mm = {data[1]: None for data in create_split_list()}
    mm_list = ["0" + str(num) if len(str(num)) == 1 else str(num) for num in range(1, 13)]
    zip_dict = dict(zip(dict_mm.keys(), mm_list))
    return zip_dict


def create_list_dict():
    res = []
    for data in create_split_list():
        data_dd = data[0]
        data_dd = data_dd[:-2]
        data_mm = data[1]
        data_yy = data[2]
        if len(data_dd) == 1:
            data_dd = "0" + data_dd
        res.append({"date_original": " ".join(data),
                    "date_modified": f"{data_dd}/{data_mm.replace(data_mm, create_modif_mm().get(data_mm))}/{data_yy}"})
    return res


file_name_1 = "Homework9_files/domains.txt"
file_name_2 = "Homework9_files/names.txt"
result_1 = create_list_data(file_name_1)
result_2 = create_surname_list(file_name_2)
result_3 = create_list_dict()
