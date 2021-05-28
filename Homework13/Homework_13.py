##################################################

"""
1. Написать функцию, которая получает в виде параметра имя файла названия интернет доменов (domains.txt)
и возвращает их в виде списка строк (названия возвращать без точки).
"""


class DomainsWorker:
    def __init__(self, filename):
        self.filename = filename

    def read_domains_file(self):
        with open(self.filename, "r") as txt_file:
            data = txt_file.readlines()
        return data

    def create_domains_list(self):
        res_list = [name.replace(".", "")[:-1] for name in self.read_domains_file()]
        return res_list

    def __repr__(self):
        return f"{self.create_domains_list()}"


##################################################
"""
2. Написать функцию, которая получает в виде параметра имя файла (names.txt)
и возвращает список всех фамилий из него.
Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
Разделитель - символ табуляции "\t"
"""


class NamesWorker:
    def __init__(self, filename):
        self.filename = filename

    def read_names_file(self):
        with open(self.filename, "r") as txt_file:
            data = txt_file.readlines()
        return data

    def create_surname_list(self):
        res_list = [surname.split("\t")[1] for surname in self.read_names_file()]
        return res_list

    def __repr__(self):
        return f"{self.create_surname_list()}"


##################################################

"""
3. Написать функцию, которая получает в виде параметра имя файла (authors.txt) и возвращает список
словарей вида {"date_original": date_original, "date_modified": date_modified}
в которых date_original - это дата из строки (если есть),
а date_modified - эта же дата, представленная в формате "dd/mm/yyyy" (d-день, m-месяц, y-год)
Например [{"date_original": "8th February 1828", "date_modified": 08/02/1828},  ...]
"""


class ModDateWorker:
    def __init__(self, filename):
        self.filename = filename
        self.months = {'January': '01',
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
        self.create_modified_dictionaries()

    def read_authors_file(self):
        with open(self.filename, "r") as txt_file:
            data = txt_file.readlines()
        return data

    def create_split_date_list(self):
        result = []
        for data in self.read_authors_file():
            data = data.split("-")[0]
            data = data.split()
            if len(data) == 3:
                result.append(data)
        return result

    def create_modified_dictionaries(self):
        result = []
        for data in self.create_split_date_list():
            data_dd = data[0]
            data_dd = data_dd[:-2]
            if len(data_dd) == 1:
                data_dd = "0" + data_dd
            result.append({"date_original": " ".join(data),
                           "date_modified": f"{data_dd}/{self.months.get(data[1])}/{data[2]}"})
        return result

    def __repr__(self):
        return f"{self.create_modified_dictionaries()}"


surnames = NamesWorker("names.txt")
modified_date = ModDateWorker("authors.txt")
domains_worker = DomainsWorker("domains.txt")
print(domains_worker)
print(surnames)
print(modified_date)
