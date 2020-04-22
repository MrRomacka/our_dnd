import board
import character

easy_1 = character.Wizard('Anton', 0)
easy_2 = character.Wizard('Ivan', 1)

board = board.Board()
board.add(easy_1, 0, 0)
board.add(easy_2, 1, 3)

print(board.team_list)

board.game()