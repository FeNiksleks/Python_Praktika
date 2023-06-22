# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо,  K – положительное число.

# Input:   [1, 2, 3, 4, 5] k = 3

# Output:  [3, 4, 5, 1, 2]

# Примечание: Пользователь может вводить значения списка или список задан изначально.

a = [1, 2, 3, 4, 5]
k = 3
print(a)
for _ in range(k):
    a.insert(0, a.pop())
print(a)

# nums = nums[-sdvig::] + nums[:-sdvig:]
# print(nums)

# Решение от Никиты
# k = int(input("Введите число для сдвига: "))
# n = int(input("Введите последовательность чисел: "))
# list_1 = [i for i in range(n)]
# print(list_1)
# for i in range(k):
#     list_1.insert(0, list_1.pop())
# print(list_1)

# Решение от Андрея
# a =[1, 2, 3, 4, 5]
# k = 3
# k = k%len(a)
# if k<0:
#     k = abs(k)
#     print(*a[k:],end =' ')
#     print(*a[0:k])
#     exit()
 
# if k>=0:
#     k = abs(k)
#     print(*a[-k:],end =' ')
#     print(*a[0:-k])