# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


start= int(input("Введите значение 1-го элемента:"))
step= int(input("Введите разность элементов:"))
quantity= int(input("Введите количество элементов:"))

def arithmetic_progression(start, step, quantity):
    arr = [start]
    for i in range(1,quantity):
        arr.append(arr[i-1] + step)
    return arr

print(arithmetic_progression(start, step, quantity))  