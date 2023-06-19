# 3.Даны целые положительные числа A и B.
# Найти их наибольший общий делитель (НОД),
# и наименьшее общее кратное (НОК)

a = 42
b = 14
nod = 0
nok = 0

flag = False
for i in range(2, min(a, b)):
    if a % i == 0 and b % i == 0:
        nod = i
        if flag:
            continue
        else:
            nok = i
            flag = True

print(f"НОК = {nok}")
print(f"НОД = {nod}")