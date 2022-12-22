# Реализуйте алгоритм перемешивания списка. 
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для получения случайного int

import random

my_list = [1, 27, 33, 43, 58, 69, 895]

def list_shuffling(my_list):
    for i in range(len(my_list)):
        my_random = random.randint(0, len(my_list)-1)
        my_buf = my_list[i]
        my_list[i] = my_list[my_random]
        my_list[my_random] = my_buf

    return my_list

print(list_shuffling(my_list))