#Ерженин Александр ДПИ23-1с

# 1.Вставить элемент после n-го элемента списка.
def insert_after_nth_element(lst, n, element):
    if n < len(lst):
        lst.insert(n + 1, element)
    else:
        print("n больше длины списка.")

# 2.Добавить элемент в начало списка.
def add_to_start(lst, element):
    
    lst.insert(0, element)

# 3.Соединить два списка.
def combine_lists(lst1, lst2):
    
    return lst1 + lst2


# Исходные списки
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']

print("Исходный list1:", list1)
print("Исходный list2:", list2)

# 1. Вставить элемент после n-го элемента списка
n = 2
element_to_insert = 99
insert_after_nth_element(list1, n, element_to_insert)
print(f"Список после вставки {element_to_insert} после {n}-го элемента:", list1)

# 2. Добавить элемент в начало списка
element_to_add = 0
add_to_start(list1, element_to_add)
print("Список после добавления элемента в начало:", list1)

# 3. Соединить два списка
combined_list = combine_lists(list1, list2)
print("Соединенный список:", combined_list)