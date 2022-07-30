# Создайте программу для игры в ""Крестики-нолики"".

from platform import mac_ver
import random

my_list = [ [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
turn = random.randint(0, 1)
game_stoper = False


while game_stoper == False:
    if turn == 0:
        print('Ход первого игрока')
        x = int(input('Введите значение по горизонтали от 0 до 2: '))
        y = int(input('Введите значение по вертикали от 0 до 2: '))
        if my_list[x][y] != 'X' and my_list[x][y] != 'O':
            my_list[x][y] = 'X'
            for i in my_list:
                print(i)
            check_1 = (my_list[0][0] == my_list[0][1] == my_list[0][2])
            check_2 = (my_list[0][0] == my_list[1][1] == my_list[2][2])
            check_3 = (my_list[0][0] == my_list[1][0] == my_list[2][0])
            check_4 = (my_list[0][1] == my_list[1][1] == my_list[2][1])
            check_5 = (my_list[0][2] == my_list[1][1] == my_list[2][0])
            check_6 = (my_list[0][2] == my_list[1][2] == my_list[2][2])
            check_7 = (my_list[1][0] == my_list[1][1] == my_list[1][2])
            check_8 = (my_list[2][0] == my_list[2][1] == my_list[2][2]) 
            if check_1 or check_2 or check_3 or check_4 or check_5 or check_6 or check_7 or check_8:
                print('Первый игрок выиграл')
                game_stoper = True
            turn = 1
        else:
            print('Это место занято, введите новые координаты')
    else:
        print('Ход второго игрока')
        x = int(input('Введите значение по горизонтали от 0 до 2: '))
        y = int(input('Введите значение по вертикали от 0 до 2: ')) 
        if my_list[x][y] != 'X' and my_list[x][y] != 'O':
            my_list[x][y] = 'O'
            for i in my_list:
                print(i)
            check_1 = (my_list[0][0] == my_list[0][1] == my_list[0][2])
            check_2 = (my_list[0][0] == my_list[1][1] == my_list[2][2])
            check_3 = (my_list[0][0] == my_list[1][0] == my_list[2][0])
            check_4 = (my_list[0][1] == my_list[1][1] == my_list[2][1])
            check_5 = (my_list[0][2] == my_list[1][1] == my_list[2][0])
            check_6 = (my_list[0][2] == my_list[1][2] == my_list[2][2])
            check_7 = (my_list[1][0] == my_list[1][1] == my_list[1][2])
            check_8 = (my_list[2][0] == my_list[2][1] == my_list[2][2]) 
            if check_1 or check_2 or check_3 or check_4 or check_5 or check_6 or check_7 or check_8:
                print('Второй игрок выиграл')
                game_stoper = True    
            turn = 0
        else:
            print('Это место занято, введите новые координаты')
       
