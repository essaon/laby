import os

n = int(input('Введите длину массива: '))
l = input('Введите отрезок: ').split(" ")
a = int(l[0])
b = int(l[1])
l = []
l = input("Введите массив: ").split(' ')
os.system('cls')


# Подсчет кол-ва различных элементов массива
def CountOfDiffrent(l):
    c = []
    for i in l:
        if int(c.count(i)) != 0:
            pass
        else:
            c.append(i)
    k = (int(len(c)))
    print(f"Кол-во различных элементов: {k}")

# Функция для подсчета суммы в массиве между первым и вторым положительным числом (писюны)


def SummOf(l):
    summ = 0
    first = -1
    second = -1
    for i in range(int(len(l))):
        if int(l[i]) > first and first == -1:
            first = i
        elif first != -1 and int(l[i]) > second:
            second = i
            break
    while first < second-1:
        summ += int(l[first+1])
        first += 1
    print(f"Сумма между первым положительным и вторым: {summ}")
# Функция для изменения массива


def PopAndAppend(l, a, b):
    k = a
    while k <= b:
        l.append(l.pop(a-1))
        k += 1
    print("Измененный массив: ", end='')
    for i in l:
        print(i, end=' ')


CountOfDiffrent(l)
SummOf(l)
PopAndAppend(l, a, b)
