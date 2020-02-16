'''
3. Hужно нарисовать на экране доску для игры в крестики нолики. Пользователь вводит размер доски (3х3, 4х4 и т.д.)
и после этого ваши программа выводит её на экран.
Например:
Введите размер: 3 3
Доска готова!
--- --- ---
| | | |
--- --- ---
| | | |
--- --- ---
| | | |
--- --- ---
'''

def kvadrat_setka(stroka, stolbec):
    i=0
    while i < stroka:
        if stroka == stolbec:
            print("--- " * (stroka))
            print("|   " * (stolbec + 1))
            i+=1
            if i ==stroka:
                print("--- " * (stolbec))
        else:
            print("--- " * (stroka - (stroka - stolbec)))
            print("|   " * (stolbec + 1))
            i+=1
            if i ==stroka:
                print("--- " * (stroka - (stroka - stolbec)))
        


kvadrat_setka(3, 1)