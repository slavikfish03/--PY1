'''
Условие задачи:
Дан целочисленный список, состоящий из 10
элементов. Поменять местами первый
максимальный и последний элементы.
'''
list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
max_value = -100000
index_max_value = 0

for i in range(0, len(list_numbers) - 1): # поиск максимального элемента
    if list_numbers[i] > max_value:
        max_value = list_numbers[i]
        index_max_value = i

list_numbers[index_max_value], list_numbers[-1] = list_numbers[-1], list_numbers[index_max_value]
print(list_numbers)
