#Ерженин Александр ДПИ23-1с

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

# 1. Иеняем местами первый и последний элемент стека
    def swap_first_and_last(self):
        if self.size() > 1:
            self.items[0], self.items[-1] = self.items[-1], self.items[0]
# 2. Удаляем средний элемент стека, если нечетное кол-во элементов, а если четное, то удаляем два средних элемента
    def remove_middle(self):
        length = self.size()
        if length == 0:
            return
        
        if length % 2 == 1:  # Нечетное количество элементов
            mid_index = length // 2
            del self.items[mid_index]
        else:  # Четное количество элементов
            mid_index_1 = (length // 2) - 1
            mid_index_2 = mid_index_1 + 1
            del self.items[mid_index_2]  # Удаляем второй средний элемент
            del self.items[mid_index_1]  # Удаляем первый средний элемент


stack = Stack()
# Добавление элементов в стек
for i in range(6):
    stack.push(i + 1)

print("Исходный стек:", stack.items)

# Поменять местами первый и последний элементы
stack.swap_first_and_last()
print("Стек после замены первого и последнего элемента:", stack.items)

# Удалить средние элементы
stack.remove_middle()
print("Стек после удаления средних элементов:", stack.items)