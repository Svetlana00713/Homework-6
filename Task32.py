# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не 
# меньше заданного минимума и не больше заданного максимума).

import random
lst = []
N = int(input("Введите длину массива: "))

for i in range(N):
	lst.append(random.randint(-N, N))
print(lst)
	 
min = int(input("Введите минимум: "))
max = int(input("Введите максимум: "))
index = []
for i in range(len(lst)):
	if min <= lst[i] <= max:
		index.append(i)
print("Количество: ", len(index))
print("Индексы: ", index)