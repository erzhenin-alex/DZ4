#Ерженин Александр ДПИ23-1с

#1. Дан кольцевой список из 20 фамилий студентов.
#Разбить студентов на 2 группы по 10 человек. Во вторую группу попадает каждый 12-й человек.

import collections


# Создаем кольцевой список из 20 фамилий студентов
students = collections.deque([
    "Иванов", "Петров", "Сидоров", "Кузнецов", "Семенов", 
    "Федоров", "Александров", "Давыдов", "Ковалев", "Морозов",
    "Громов", "Романов", "Егоров", "Лебедев", "Сидорчук", 
    "Станиславов", "Панферов", "Лаврентьев", "Косарев", "Баранов"
])

# Первая группа будет содержать первых 10 студентов
group1 = []
# Вторая группа будет заполняться каждым 12-м студентом
group2 = []

# Сначала добавляем первые 10 студентов в первую группу
for _ in range(10):
    group1.append(students.popleft())

# Теперь добавляем каждого 12-го студента во вторую группу
# Чтобы рассмотреть кольцевой список, нам нужно добавлять студентов к концу
# с помощью метода append, когда мы не берем их.
for i in range(12):
    student = students.popleft()
    if i % 12 == 11:  # Каждый 12-й студент (в 0-индексации - это элемент с индексом 11)
        group2.append(student)
    else:
        students.append(student)  # Возвращаем остальных студентов обратно в конец очереди

# Выводим результаты
print("Группа 1:", group1)
print("Группа 2:", group2)