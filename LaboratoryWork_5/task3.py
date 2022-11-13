import random


def get_unique_list_numbers() -> list[int]:
    list_numbers = []  # создаем пустой список
    while len(list_numbers) < 15:
        element = random.randint(-10, 10)  # создаем случайное число
        if element not in list_numbers:  # проверяем наличие числа в списке
            list_numbers.append(element)  # если число отсутствует, то добавляем
    return list_numbers


if __name__ == "__main__":
    list_unique_numbers = get_unique_list_numbers()
    print(list_unique_numbers)
    print(len(list_unique_numbers) == len(set(list_unique_numbers)))
