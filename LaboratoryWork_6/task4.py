'''
Условие задачи:
Реализовать конвертер из csv в json формат
'''


import json

INPUT_FILE = "input_1.csv"


def csv_to_list_dict(filename, delimiter=",") -> list[dict]:
    with open(filename, mode="r", encoding="utf-8") as inp_csv:
        data = inp_csv.readlines()  # разбиваем файл на списки из строк
        list_dictionary = []  # создаем список со словарями
        for i in range(0, len(data)):  # запускаем цикл по каждой строке
            if i == 0:  # при нулевом индексе делаем строку заголовков
                data[i] = data[i].replace("\n", "")  # убираем \n после метода readlines()
                headers = data[i].split(delimiter)
            else:
                data[i] = data[i].replace("\n", "")
                current_string = data[i].split(delimiter)
                list_dictionary.append(dict(zip(headers, current_string)))
    return list_dictionary  # добавляем на каждой итерации словарь и возвращаем список словарей


if __name__ == "__main__":
    print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4, ensure_ascii=False))
