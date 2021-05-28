from random import randint
import requests
import csv

############################################

"""
1. Написать функцию, которая принимает в виде параметра целое число - количество цитат.
и возвращает список не повторяющихся цитат. Если автор не указан, цитату не брать.
"""


def create_quotes_list(count):
    res = []
    while len(res) < count:
        params = {"method": "getQuote",
                  "format": "json",
                  "key": randint(0, 999)}
        r = requests.get(url, params=params)
        data = r.json()
        quote = data["quoteText"]
        author = data["quoteAuthor"]
        link = data["quoteLink"]
        if author and quote not in res:
            res.append([author, quote, link])
    return sorted(res)


############################################

"""
2. Написать функцию, которая принимает результат предыдущей функции и сохраняет в csv файл.
Имя файла сделать параметром по умолчанию.
Заголовки csv файла:
Author, Quote, URL.
Перед сохранением в csv, записи отсортировать по автору (в алфавитном порядке).
Разделитель - запятая.
"""


def create_quotes_csv_file(data):
    with open("quote.csv", 'w') as f:
        writer = csv.writer(f, delimiter=",", lineterminator="\r")
        writer.writerow(["Author", "Quote", "URL"])
        writer.writerows(data)


url = "http://api.forismatic.com/api/1.0/"
quotes_list = create_quotes_list(10)
create_quotes_csv_file(quotes_list)
