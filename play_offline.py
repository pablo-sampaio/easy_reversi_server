########################
# Este arquivo permite a um humano jogar contra uma IA simples (gulosa, escolhe a jogada que vai dar mais pontos). 
# O humano joga digitando a jogada pelo teclado. Atenção pois você deve indicar a jogada na forma "x y", onde "x"
# se refere à coluna e o "y" se refere à linha.
#
# Modificado a partir de: https://inventwithpython.com/chapter15.html
########################

import sys

import reversi as rev
from greedy_base import chooseGreedyMove


def enterPlayerTile():
    # Lets the player type which tile they want to be.
    # Returns a list with the player's tile as the first item, and the computer's tile as the second.
    tile = ''
    while not (tile == 'X' or tile == 'O'):
        print('Do you want to be X or O?')
        tile = input().upper()
    # the first element in the list is the player's tile, the second is the computer's tile.
    if tile == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().strip().lower().startswith('y')


def getPlayerMove(board, playerTile):
    '''
    Let the player type in their move.
    Returns the move as [x, y] (or returns the strings 'hints' or 'quit' or 'pass')
    '''
    if rev.getValidMoves(board, playerTile) == []:
        print('Player has no valid move. Player forced to pass.')
        return 'pass'

    while True:
        print('Enter your move, or type quit to end the game, or hints to turn off/on hints.')
        moveStr = input().strip().lower()
        if moveStr == 'quit':
            return 'quit'
        if moveStr == 'hints':
            return 'hints'
        if moveStr == 'pass':
            return 'pass'
        
        move = moveStr.split()
        
        if len(move) == 2: 
            x = int(move[0])
            y = int(move[1])
            if rev.isValidMove(board, playerTile, x, y):
                break
        
        print(f'That is not a valid move.')
        print(f'Type the x digit (0 to {len(board)-1}), then space, then the y digit (0 to {len(board[0])-1}). Or type "pass".')
        print(f'For example, "1 1" will be the top-left corner.')

    return [x, y]


def isOnCorner(board, x, y):
    lastX = len(board)-1
    lastY = len(board[0])-1
    # Returns True if the position is in one of the four corners.
    return (x == 0 and y == 0) or (x == lastX and y == 0) or (x == 0 and y == lastY) or (x == lastX and y == lastY)


def showPoints(board, playerTile, computerTile):
    # Prints out the current score.
    scores = rev.getScoreOfBoard(board)
    print('You have %s points. The computer has %s points.' % (scores[playerTile], scores[computerTile]))


def PLAY_GAME():
    print('Welcome to Reversi!')

    while True:
        # tabuleiros de tamanho padrão 8x8
        #mainBoard = rev.getNewBoard()
        mainBoard = rev.getNewBoard(stones=[(1,6), (6,6)])
        
        # tabuleiros de tamanhos diferentes
        #mainBoard = rev.getNewBoard(sizeX=10, sizeY=10, stones=[(2,6), (2,7), (3,7), (6,2), (7,2), (7,3)])
        #mainBoard = rev.getNewBoard(sizeX=6,sizeY=6)
        
        playerTile, computerTile = enterPlayerTile()
        showHints = False
        passCount = 0

        turn = 'player' if (playerTile == 'X') else 'computer'  # player with 'X' starts
        print('The ' + turn + ' will go first.')

        while True:
            # O jogo acabe depois de dois "pass" consecutivos
            if passCount >= 2:
                print("Two consecutive passes.")
                print("End of game.")
                break

            if turn == 'player':
                # Player's turn.
                if showHints:
                    validMovesBoard = rev.getBoardWithValidMoves(mainBoard, playerTile)
                    rev.drawBoard(validMovesBoard)
                else:
                    rev.drawBoard(mainBoard)
                showPoints(mainBoard, playerTile, computerTile)
                
                move = getPlayerMove(mainBoard, playerTile)
                
                if move == 'quit':
                    print('Thanks for playing!')
                    sys.exit() # terminate the program
                elif move == 'hints':
                    showHints = not showHints
                    continue
                elif move == 'pass':
                    passCount += 1
                else:
                    passCount = 0
                    rev.makeMove(mainBoard, playerTile, move[0], move[1])

                turn = 'computer'

            else:
                # Computer's turn.
                rev.drawBoard(mainBoard)
                showPoints(mainBoard, playerTile, computerTile)
                input('Press Enter to see the computer\'s move.')

                if rev.getValidMoves(mainBoard, computerTile) == []:
                    passCount += 1
                    print("Computer passed.")
                else:
                    passCount = 0
                    x, y = chooseGreedyMove(mainBoard, computerTile)
                    rev.makeMove(mainBoard, computerTile, x, y)
                    print("Computer played x =", x, "y =", y)

                turn = 'player'

        # Display the final score.
        rev.drawBoard(mainBoard)
        scores = rev.getScoreOfBoard(mainBoard)
        print('X scored %s points. O scored %s points.' % (scores['X'], scores['O']))
        
        if scores[playerTile] > scores[computerTile]:
            print('You beat the computer by %s points! Congratulations!' % (scores[playerTile] - scores[computerTile]))
        elif scores[playerTile] < scores[computerTile]:
            print('You lost. The computer beat you by %s points.' % (scores[computerTile] - scores[playerTile]))
        else:
            print('The game was a tie!')

        if not playAgain():
            break


### ENTRY POINT ###

if __name__ == '__main__':
    PLAY_GAME()

