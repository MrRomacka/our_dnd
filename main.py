import board
import character

easy_1 = character.Wizard('Anton', 0)
easy_2 = character.Druid('Ivan', 1)
easy_3 = character.Warlock('Rudya', 0)
easy_4 = character.Warrior('Gena', 1)
easy_5 = character.Barbarian('Zhenya', 0)
easy_6 = character.Monk('IGOR', 1)

board = board.Board()
board.add(easy_1, 0, 0)
board.add(easy_2, 1, 3)
board.add(easy_3, 0, 1)
board.add(easy_4, 5, 5)
board.add(easy_5, 6, 5)
board.add(easy_6, 4, 2)

board.game()