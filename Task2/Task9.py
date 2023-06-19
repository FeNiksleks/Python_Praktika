# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120

def factorial(n):
   if n == 0:
       return 1
   i = 1
   fact = 1
   while i <= n:
       fact *= i
       i += 1
   return fact


num = 3
result = factorial(num)
print(result)