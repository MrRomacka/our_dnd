class Board:
    def __init__(self, x = 8, y = 8):
        self.field = [[0] * y for _ in range(x)]
        self.x_size = x
        self.y_size = y
        self.status_move = 0
        self.status_turn = 0
    def add(self, hero, x, y):
        if x >= self.x_size or x < 0 or y > self.y_size or y < 0:
            print('That is illegal!')
            return False
        elif self.field[x][y] != 0:
            print('This location isnt empty!')
            return False
        else:
            self.field[x][y] = hero
            return True

    def game(self):
        while True:
            print('Team 0 turn')
            x, y = map(int, input(), input())
            count_0 = 0
            count_1 = 0
            for i in range(self.x_size):
                for j in range(self.y_size):
                    if self.field[i][j] != 0:
                        if self.field[i][j].team == 0:
                            count_0 += 1
                        else:
                            count_1 += 1
            if count_0 == 0:
                print('Team 1 wins!')
                break
            elif count_1 == 0:
                print('Team 0 wins!')
                break

    def move(self, hero, x, y, x_now, y_now):
        hero = self.field[x][y]
        hero: Union[Character, int]
        if hero != 0:
            if hero.team == self.status_move:
                if self.field[x_now][y_now].team != 0:
                    enemy: Character
                    enemy = self.field[x_now][y_now].team
                    if enemy != 0:
                        if enemy.team == self.status_move:
                            return False
                        else:
                            result = self.fight(hero, enemy)
                            self.field[x_now][y_now] = result
                else:
                    self.field[x][y] = 0
                    self.field[x_now][y_now] = hero
                    return True

    def fight(self, hero, enemy):
        return hero