
# This is the base code for a greedy decision making algorithm for Reversi.
# It plays either on the corner or on the position that captures the maximum number of pieces.
# Adapted from: https://inventwithpython.com/chapter15.html

import random

import reversi as rev


def isOnCorner(board, x, y):
    lastX = len(board)-1
    lastY = len(board[0])-1
    # Returns True if the position is in one of the four corners.
    return (x == 0 and y == 0) or (x == lastX and y == 0) or (x == 0 and y == lastY) or (x == lastX and y == lastY)


def chooseGreedyMove(board, playerTile):
    validMoves = rev.getValidMoves(board, playerTile)
    if validMoves == []:
        return None  # passed

    # randomize the order of the possible moves
    random.shuffle(validMoves)

    # always go for a corner if available.
    for x, y in validMoves:
        if isOnCorner(board, x, y):
            return [x, y]

    # go through all the possible moves and remember the best scoring move
    bestScore = -1
    for x, y in validMoves:
        dupeBoard = rev.getBoardCopy(board)
        rev.makeMove(dupeBoard, playerTile, x, y)
        score = rev.getScoreOfBoard(dupeBoard)[playerTile]
        if score > bestScore:
            bestMove = [x, y]
            bestScore = score

    return bestMove
