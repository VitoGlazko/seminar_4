def getListMult(num):
    list = []
    listMult = [list.append(i) for i in range(1, num+1) if num % i == 0]
    return list

def primeNum(numN):
    primeList = []
    for i in range(2, numN):
        while numN % i == 0:
            numN /= i
            primeList.append(i)
    return primeList

num = int(input("Введите натуральное число: "))
list1 = getListMult(num)
print(f'Множители числа {num} : {list1}')
list2 = primeNum(num)
print(f'Простые множители числа {num} :{list2}')
