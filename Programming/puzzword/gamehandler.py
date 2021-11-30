import requests
import json
import collections
import heapq
import numpy as np

MOVEMENT_DICT = {

    "2" : "^",
    "1" : "v",
    "3" : ">",
    "4" : "<"

}

# Get puzzle config
def setup_remote():

    s = requests.session()
    r = s.get("https://puzzword.csa-challenge.com/puzzle")
    config = json.loads(json.loads(r.text).get('message'))
    return config_remote(config)

# Config the puzzle
def config_remote(config):

    puz_id = config.get('puzzle_id')
    source_board = config.get('source_board')
    destination_board = config.get('destination_board')
    brd_config = [puz_id, source_board, destination_board]
    return get_board_config(brd_config)

# Translate board to work with
def translate_board(board):

    new_board = []
    for i in board:
        i = i.replace(" ", "2")
        i = i.replace("O", "1")
        i = i.replace(".", "0")
        i = list(i)
        new_list = [int(j) for j in i]
        new_board.append(new_list)
    return new_board

# Check if moves are correct
def check_solution(puzzle_id,solution):

    url = 'https://puzzword.csa-challenge.com/solve'
    data = {"puzzle_id": puzzle_id, "solution": solution}
    response = requests.post(url, json=data)
    return response.text

# Translate board
def get_board_config(board_config):

    board_config[1] = translate_board(board_config[1])
    board_config[2] = translate_board(board_config[2])
    return board_config

# Change steps to axis
def solution_steps_translate(ans):
    solution_list = []
    for i in ans:
        i = list(i)
        direction = MOVEMENT_DICT[str(i[2])]
        answer = [i[1],i[0],direction]
        solution_list.append(answer)
    return solution_list

#-------------------------------------------------------------------------------------------------------------------------------------------------------

def count_moves(current_board, solution_board):
    count_current_board = 0
    count_solution_board = 0
    for i in current_board:
        count_current_board = count_current_board + i.count(1)
    for i in solution_board:
        count_solution_board = count_solution_board + i.count(1)
    return count_current_board - count_solution_board

def updateState(state, x, y, x1, y1, x2, y2):
    newState = [[j for j in i] for i in state]
    newState[x][y] = 0
    newState[x + x1][y + y1] = 0
    newState[x + x2][y + y2] = 1
    return newState


def updateAnswer(ans, x, y, type):
    newAns = [i for i in ans]
    newAns.append((x, y, type))
    return newAns

def isLegal(current_board,solution_board):
    if current_board == solution_board:
        return True
    return False


def solveWithBackTracking(current_board, solution_board, moves):

    row = len(current_board)
    column = len(current_board[0])

    ans = [(0, 0, 0)]

    #visitMap = set()
    stackStt = collections.deque([current_board])
    stackAns = collections.deque([ans])

    while stackStt:
        top = stackStt.pop()
        ans = stackAns.pop()
        if isLegal(top, solution_board):
            result = []
            cnt = 0
            for i in ans:
                cnt += 1
                if cnt >= 2:
                    result.append(i)
            return result

        delta = 1
        for i in range(0, row):
            for j in range(0, column):
                if i + 2 < row and top[i][j] == 1 and top[i + 1][j] == 1 and top[i + 2][j] == 0 and ((moves+delta) > len(ans)):
                    stackStt.append(updateState(top, i, j, 1, 0, 2, 0))
                    stackAns.append(updateAnswer(ans, i, j, 1))
                if i - 2 >= 0 and top[i][j] == 1 and top[i - 1][j] == 1 and top[i - 2][j] == 0 and ((moves+delta) > len(ans)):
                    stackStt.append(updateState(top, i, j, -1, 0, -2, 0))
                    stackAns.append(updateAnswer(ans, i, j, 2))
                if j + 2 < column and top[i][j] == 1 and top[i][j + 1] == 1 and top[i][j + 2] == 0 and ((moves+delta) > len(ans)):
                    stackStt.append(updateState(top, i, j, 0, 1, 0, 2))
                    stackAns.append(updateAnswer(ans, i, j, 3))
                if j - 2 >= 0 and top[i][j] == 1 and top[i][j - 1] == 1 and top[i][j - 2] == 0 and ((moves+delta) > len(ans)):
                    stackStt.append(updateState(top, i, j, 0, -1, 0, -2))
                    stackAns.append(updateAnswer(ans, i, j, 4))
    return -1


#-------------------------------------------------------------------------------------------------------------------------------------------------------------

board_conf = setup_remote()
flag = ''

while True:

    moves = count_moves(board_conf[1], board_conf[2])
    solved = solveWithBackTracking(board_conf[1], board_conf[2], moves)
    solution = solution_steps_translate(solved)

    try:
        board_conf = check_solution(board_conf[0],solution)
        message = json.loads(json.loads(board_conf).get('message')).get('message')
        flag += message[0]
        board_conf = json.loads(json.loads(board_conf).get('message'))
        board_conf = config_remote(board_conf)
        print(message)
        print(flag)
        print(board_conf)

    except:
        print(board_conf)
        break



