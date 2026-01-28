def add(a,b): #Функция сложения
    return a+b
def sub(a,b): #Функция уменьшение
    return a-b
def mul(a,b): #Функция умножение
    return a*b
def div(a,b): #Функция деление
    return a/b
while True:
    print("Команды: 1Складывать 2Уменьшать 3Умножать 4Делить 5Сравнить 6Узнать число Пи") #Команды программы
    Comand = int(input("Что вы хотите сделать?"))
    if Comand == 1:
        a = int(input("Введите 1 число"))
        b = int(input("Введите 2 число"))
        print(a,"+",b,"=",add(a,b))
    elif Comand == 2:
        a = int(input("Введите 1 число"))
        b = int(input("Введите 2 число"))
        print(a,"-",b,"=",sub(a,b))
    elif Comand == 3:
        a = int(input("Введите 1 число"))
        b = int(input("Введите 2 число"))
        print(a,"*",b,"=",mul(a,b))
    elif Comand == 4:
        a = int(input("Введите 1 число"))
        b = int(input("Введите 2 число"))
        print(a,"/",b,"=",div(a,b))
    elif Comand == 5:
        a = int(input("Введите 1 число"))
        b = int(input("Введите 2 число"))
        if a > b:
            print(a,">",b)
        elif a < b:
            print(a,"<",b)
        else:
            print(a,"=",b)
    elif Comand == 6:
        print("3,1415926535")
    else:
        print("Ошибка ты написал что-то не так либо ты это сделал специально зачем-то")

