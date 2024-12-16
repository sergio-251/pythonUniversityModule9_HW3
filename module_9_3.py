# Генераторные сборки
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
first_result = (len(elem_1) - len(elem_2) for elem_1, elem_2 in zip(first, second) if len(elem_1) != len(elem_2))
second_result =(len(first[i]) == len(second[i]) for i in range(min(len(first), len(second))))

print(list(first_result))
print(list(second_result))