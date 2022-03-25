import time
import functools
import pathlib
from Kakurasu.searchAlgo import AStarSearch, BreadthFirstSearch
from kakurasu import *

DIR_PATH = str(pathlib.Path(__file__).parent.resolve()) + '\\'

def readFile(fileName):
    scanner = open(fileName, "r")
    lines = scanner.read().splitlines()
    return lines


def initBoard(size):
    board = []
    for i in range(size):
        row = []
        for j in range(size):
            row.insert(j, 0)
        board.insert(i, row)
    return board

def printBoard(board):
    for i in board:
        line = ""
        for j in i:
            line += str(j) + " "
        print(line)
        
def printList(res):
    line = ""
    for i in res:
        line += str(i) + " "
    print(line)
    
if __name__ == '__main__':
    fileName = "input.txt"
    input = readFile(DIR_PATH + fileName)
    n = int(input[0][0])
    board = initBoard(n)
    grid = functools.reduce(lambda res, cur: res + 
    [[int(i) for i in cur.split(' ')]]
    , input[1:], [])
    
    row_const = grid[1]
    col_const = grid[2]
    
    kaku = Kakurasu(board, row_const, col_const, n)

    a_star = AStarSearch()
    bfs = BreadthFirstSearch()

    start

