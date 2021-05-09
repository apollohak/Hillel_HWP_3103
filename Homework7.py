# 1) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]

person_sw = [{"name": "Чубакка", "age": 202},
             {"name": "Йода", "age": 900},
             {"name": "Люк", "age": 88},
             {"name": "С-3РО", "age": 433},
             {"name": "Энакин", "age": 41}]

# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена.

age_list = [list(age.values())[1] for age in person_sw]
min_age = min(age_list)

for some_person in person_sw:
    if age_list.count(min_age) > 1:
        print(list(some_person.values())[0])
    elif list(some_person.values())[1] == min_age:
        print(f"Имя самого молодого:{list(some_person.values())[0]}")

# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.

long_list = [len(list(len_name.values())[0]) for len_name in person_sw]
max_len = max(long_list)

for some_person in person_sw:
    if long_list.count(max_len) > 1:
        print(list(some_person.values())[0])
    elif len(list(some_person.values())[0]) == max_len:
        print(f"Самое длинное имя: {list(some_person.values())[0]}")

# в) Посчитать среднее количество лет всех людей из списка.

average_age = sum(age_list) // len(age_list)

#################################################################

# 2) Даны два словаря my_dict_1 и my_dict_2.

my_dict_1 = dict(black="#000000", purple="#800080", green="#008000", teal="#008080", maroon="#800000")
my_dict_2 = dict(black="#000001", magenta="#ff00ff", green="#008002", yellow="#ffff00", maroon="#800003")

# а) Создать список из ключей, которые есть в обоих словарях.

key_list = [key for key in my_dict_1 if key in my_dict_2]

# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.

key_list = [key for key in my_dict_1 if key not in my_dict_2]

# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.

new_dict = {key: value for key, value in my_dict_1.items() if key not in my_dict_2}

# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},

key_dict_1 = {key: value for key, value in my_dict_1.items() if key not in my_dict_2}
key_dict_2 = {key: value for key, value in my_dict_2.items() if key not in my_dict_1}
key_value1_value2 = {key: [value, my_dict_2.get(key)] for key, value in my_dict_1.items() if key in my_dict_2}

total_dict = {**key_dict_1, **key_dict_2, **key_value1_value2}
