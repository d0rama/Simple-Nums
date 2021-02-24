def is_simple(a, b):
	numCount = 0
	for i in range(a, b + 1): # Перебор всех чисел в указанном диапазоне
	    numCount = 0 # Сброс счетчика
	    for j in range(1, i + 1): # Делители числа i
	        if i % j == 0: # Нахождение делителей
	            numCount += 1
	    if numCount == 2: # Проверка является ли число простым
	        print(i)

one_num, two_num = int(input('Число 1: ')), int(input('Число 2: ')) # Диапазон чисел

is_simple(one_num, two_num)