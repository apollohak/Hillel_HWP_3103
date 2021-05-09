import random
import string

####################################################
"""
1. Написать функцию которой передается один параметр - список строк my_list.
Функция возвращает новый список в котором содержаться
элементы из my_list по следующему правилу:
Если строка стоит на нечетном месте в my_list, то ее заменить на
перевернутую строку. "qwe" на "ewq".
Если на четном - оставить без изменения.
"""


def create_revers_str_list(my_str_list):
    res_list = [value[::-1] if index % 2 else value for index, value in enumerate(my_str_list)]
    return res_list


####################################################
"""
2. Написать функцию которой передается один параметр - список строк my_list.
Функция возвращает новый список в котором содержаться
элементы из my_list у которых первый символ - буква "a".
"""


def create_list_start_a(str_list):
    res_list = [value for value in str_list if value.startswith('a')]
    return res_list


####################################################
"""
3. Написать функцию которой передается один параметр - список строк my_list.
Функция возвращает новый список в котором содержаться
элементы из my_list в которых есть символ - буква "a" на любом месте.
"""


def create_list_with_a(str_list):
    res_list = [some_str for some_str in str_list if 'a' in some_str]
    return res_list


####################################################
"""
4. Написать функцию которой передается один параметр - список строк my_list в
котором могут быть как строки (type str) так и целые числа (type int).
Функция возвращает новый список в котором содержаться только строки из my_list.
"""


def create_str_list(my_list):
    res_list = [some_str for some_str in my_list if type(some_str) == str]
    return res_list


####################################################
"""
5. Написать функцию которой передается один параметр - строка my_str.
Функция возвращает новый список в котором содержаться те символы из my_str,
которые встречаются в строке только один раз.
"""


def create_unique_sym_list(my_str):
    res_list = [symbol for symbol in my_str if my_str.count(symbol) == 1]
    return res_list


####################################################
"""
6. Написать функцию которой передается два параметра - две строки.
Функция возвращает список в который поместить те символы,
которые есть в обеих строках хотя бы раз.
"""


def create_inter_symb_list(some_str_1, some_str_2):
    res_list = [symbol for symbol in set(some_str_1) if symbol in set(some_str_2)]
    return res_list


####################################################
"""
7. Написать функцию которой передается два параметра - две строки.
Функция возвращает список в который поместить те символы, которые есть в обеих строках,
но в каждой только по одному разу.
"""

def create_inter_symbol_one(some_str_1, some_str_2):
    res_list = [symbol for symbol in some_str_1 if some_str_1.count(symbol) == 1 and some_str_2.count(symbol) == 1]
    return res_list


####################################################
"""
8. Даны списки names и domains (создать самостоятельно).
Написать функцию для генерирования e-mail в формате:
фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
Строку и число генерировать случайным образом.
"""


def create_surname(names):
    family = random.choice(names)
    return family


def create_random_num():
    random_num = random.randint(100, 999)
    return random_num


def create_random_str():
    list_word = "".join([random.choice(string.ascii_lowercase) for _ in range(random.randint(5, 7))])
    return list_word


def create_domain(domains):
    rand_domain = random.choice(domains)
    return rand_domain


def create_email(names, domains):
    email_name = f"{create_surname(names)}.{create_random_num()}@{create_random_str()}.{create_domain(domains)}"
    return email_name


####################################################

my_str_list = ['Дан', 'список', 'строк', 'my_list']
str_list = ['qwe', 'asd', 'afr', 'ooa', 'lki', 'pal', 'ayu']
my_list = ['Дан', 'список', 45, 'строка', 7]
my_str = "My name is Vova. I'm 41. But I still believe in magic. EXPELLIARMUS!"
some_str_1 = "Some text fo str"
some_str_2 = "Text for this string"
names = ["padawan", "master", "knight", "general"]
domains = ["net", "com", "ua", "ru"]

####################################################

result_1 = create_revers_str_list(my_str_list)
result_2 = create_list_start_a(str_list)
result_3 = create_list_with_a(str_list)
result_4 = create_str_list(my_list)
result_5 = create_unique_sym_list(my_str)
result_6 = create_inter_symb_list(some_str_1, some_str_2)
result_7 = create_inter_symbol_one(some_str_1, some_str_2)
result_8 = create_email(names, domains)
