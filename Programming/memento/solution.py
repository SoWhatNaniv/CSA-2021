import base64
import requests
import random

board1 = b'[[1,1,2,2,3,3,4,4],[5,5,6,6,7,7,8,8],[9,9,10,10,11,11,12,12],[13,13,14,14,15,15,16,16],[17,17,18,18,19,19,20,20]]'
board2 = b'[[1,2,1,2,3,4,3,4],[5,6,5,6,7,8,7,8],[9,10,9,10,11,12,11,12],[13,14,13,14,15,16,15,16],[17,18,17,18,19,20,19,20]]'
board3 = b'[[1,2,3,1,2,3,16,20],[4,5,6,4,5,6,17,19],[7,8,9,7,8,9,18,16],[10,11,12,10,11,12,19,17],[13,14,15,13,14,15,20,18]]'
board4 = b'[[1,2,3,4,1,2,3,4],[5,6,7,8,5,6,7,8],[9,10,11,12,9,10,11,12],[13,14,15,16,13,14,15,16],[17,18,19,20,17,18,19,20]]'
board5 = b'[[1,6,11,16,17,1,6,11],[2,7,12,18,18,2,7,12],[3,8,13,19,19,3,8,13],[4,9,14,20,20,4,9,14],[5,10,15,17,16,5,10,15]]'
board6 = b'[[1,2,3,4,5,6,19,20],[7,8,9,10,14,13,12,11],[18,17,19,15,16,20,18,17],[14,13,12,11,7,8,9,10],[15,16,1,2,3,4,5,6]]'
board7 = b'[[1,2,3,4,5,6,7,8],[7,8,9,15,11,12,1,2],[10,14,14,15,16,16,13,10],[12,20,20,19,18,17,17,9],[11,13,6,19,18,3,4,5]]'
board8 = b'[[1,5,12,12,13,13,7,10],[2,6,15,14,14,15,8,1],[3,10,17,16,16,17,9,2],[4,7,18,19,18,19,5,3],[9,8,20,20,11,11,6,4]]'

board11 = [[1,1,2,2,3,3,4,4],[5,5,6,6,7,7,8,8],[9,9,10,10,11,11,12,12],[13,13,14,14,15,15,16,16],[17,17,18,18,19,19,20,20]]
board22 = [[1,2,1,2,3,4,3,4],[5,6,5,6,7,8,7,8],[9,10,9,10,11,12,11,12],[13,14,13,14,15,16,15,16],[17,18,17,18,19,20,19,20]]
board33 = [[1,2,3,1,2,3,16,20],[4,5,6,4,5,6,17,19],[7,8,9,7,8,9,18,16],[10,11,12,10,11,12,19,17],[13,14,15,13,14,15,20,18]]
board44 = [[1,2,3,4,1,2,3,4],[5,6,7,8,5,6,7,8],[9,10,11,12,9,10,11,12],[13,14,15,16,13,14,15,16],[17,18,19,20,17,18,19,20]]
board55 = [[1,6,11,16,17,1,6,11],[2,7,12,18,18,2,7,12],[3,8,13,19,19,3,8,13],[4,9,14,20,20,4,9,14],[5,10,15,17,16,5,10,15]]
board66 = [[1,2,3,4,5,6,19,20],[7,8,9,10,14,13,12,11],[18,17,19,15,16,20,18,17],[14,13,12,11,7,8,9,10],[15,16,1,2,3,4,5,6]]
board77 = [[1,2,3,4,5,6,7,8],[7,8,9,15,11,12,1,2],[10,14,14,15,16,16,13,10],[12,20,20,19,18,17,17,9],[11,13,6,19,18,3,4,5]]
board88 = [[1,5,12,12,13,13,7,10],[2,6,15,14,14,15,8,1],[3,10,17,16,16,17,9,2],[4,7,18,19,18,19,5,3],[9,8,20,20,11,11,6,4]]

flag = '_abcdefghijklmnopqrstuvwxyz'
boards_list = [board1, board2, board3, board4, board5, board6, board7, board8]
local_boards_list = [board11, board22, board33, board44, board55, board66, board77, board88]
flag_letters_list = []
game_level = 4
game_lengths = [5,3,3,7,3,3,6]

def shortest_path(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def verify_game(board, level):
    card_number = random.randint(1, 20)
    indexes = []
    for i in range(5):
        for j in range(8):
            if board[i][j] == card_number:
                indexes.append([i, j])

    shortest = shortest_path(indexes[0], indexes[1])# board, "UP|DOWN|LEFT|RIGHT"
    result = 0
    if shortest == (ord(flag[level]) % 9) + 1:
        result = 1
    return result

def verify_game_loop(board,level):
    counter = 0
    for i in range(50):
        counter += verify_game(board,level)
    if counter >= 20:
        return True
    return False

def board_len_counter(board):
    return_dict = dict()
    board_obj = eval(board)
    for card_number in range(1, 21):
        indexes = []
        for i in range(5):
            for j in range(8):
                if board_obj[i][j] == card_number:
                    indexes.append([i, j])
        x = shortest_path(indexes[0], indexes[1])
        if x not in return_dict:
            return_dict[x] = 1
        else:
            return_dict[x] += 1
    return return_dict

def board_to_obj(board):
    board_object = base64.b64encode(board)
    return str(board_object).strip('b').strip("'")

def check_board(level, board_obj):
    request_url = f'http://memento.csa-challenge.com:7777/verifygame?level={level}&board={board_obj}'
    request = requests.get(url=request_url)
    value = request.content.decode()
    request.close()
    return value

def possible_letters(board_counter):
    pos_let = []
    for letter in range(ord('_'), ord('{')):
        if letter != 96 and (letter % 9) + 1 == board_counter:
            pos_let.append(chr(letter))
    if (ord('}') % 9) + 1 == board_counter:
        pos_let.append('}')
    return pos_let

def validate_board_card_length(level, board_obj):
    counter = 0
    for i in range(40):
        if i > 10 and not counter:
            return False
        counter += int(check_board(level, board_obj))
    return counter >= 20

def check_local(game_level):
    while game_level < 40:

        print(f"Trying game level {game_level}....")
        board_counter = 1
        for board in local_boards_list:
            print(f'Trying board number {board_counter}')
            #board_obj = board_to_obj(board)
            if verify_game_loop(board,game_level):
                flag_letters_list.append(possible_letters(board_counter))
                print(board_counter)
                break
            board_counter += 1

        if board_counter == 9:
            flag_letters_list.append(possible_letters(board_counter))
            print(board_counter)

        game_level += 1
        print(flag_letters_list)

def check_remote(game_level):
    while game_level <= 23 :

        print(f"Trying game level {game_level}....")
        board_counter = 1
        for board in boards_list:
            print(f'Trying board number {board_counter}')
            board_obj = board_to_obj(board)
            if validate_board_card_length(game_level,board_obj):
                flag_letters_list.append(possible_letters(board_counter))
                print(board_counter)
                break
            board_counter += 1

        if board_counter == 9:
            flag_letters_list.append(possible_letters(board_counter))
            print(board_counter)

        game_level += 1
        print(flag_letters_list)

check_remote(4)
