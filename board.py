from time import sleep


class Board:
    def __init__(self, x=8, y=8):
        self.field = [[0] * y for _ in range(x)]
        self.x_size = x
        self.y_size = y
        self.status_move = 0
        self.hero_list = []
        self.team_list = []
        self.team_dict = {}

    def add(self, hero, x, y):
        self.hero_list.append(hero)
        if x > (self.x_size - 1) or x < 0 or y > (self.y_size - 1) or y < 0:
            print('Hey, that is illegal!')
            return False
        elif self.field[x][y] != 0:
            print('This location isn`t empty, try other one!')
            return False
        else:
            self.field[x][y] = hero
            hero.x = x
            hero.y = y
            return True

    def team_add(self):
        for hero in self.hero_list:
            if hero.team not in self.team_dict:
                self.team_dict[hero.team] = [hero]
            else:
                self.team_dict[hero.team].append(hero)
            if hero.team not in self.team_list:
                self.team_list.append(hero.team)

    def game(self):
        self.team_add()
        while True:
            for hero in self.hero_list:
                flag = True
                print(f'\nTeam {hero.team} turn. \n{hero.name} has started moving.\n')
                while (self.status_move < 3) and flag:
                    self.status_move += 1
                    flag = self.move(hero)
                    if flag == 'break':
                        flag = 'break'
                        break
                self.status_move = 0
                if flag == 'break':
                    break
            if flag == 'break':
                break

    def move(self, hero):
        while True:
            direction = input().lower()
            if direction == 'up':
                if hero.x < 1:
                    print('There`s a wall, change my direction.')
                else:
                    hero.x = hero.x - 1
                    flag = self.check_heroes()
                    if flag == 'ally':
                        print('Oops, here`s hero`s ally.\nChange direction.')
                    else:
                        return flag
            elif direction == 'down':
                if hero.x == self.x_size:
                    print('There`s a wall, change my direction.')
                else:
                    hero.x = hero.x + 1
                    flag = self.check_heroes()
                    if flag == 'ally':
                        print('Oops, here`s hero`s ally.\nChange direction.')
                    else:
                        return flag
            elif direction == 'left':
                if hero.y < 1:
                    print('There`s a wall, change my direction.')
                else:
                    hero.y = hero.y - 1
                    flag = self.check_heroes()
                    if flag == 'ally':
                        print('Oops, here`s hero`s ally.\nChange direction.')
                    else:
                        return flag
            elif direction == 'right':
                if hero.y == self.y_size:
                    print('There`s a wall, change my direction.')
                else:
                    hero.y = hero.y + 1
                    flag = self.check_heroes()
                    if flag == 'ally':
                        print('Oops, here`s hero`s ally.\nChange direction.')
                    else:
                        return flag
            elif direction == "status":
                self.heroes_status()
            elif direction == 'stop':
                return False
            elif direction == 'close':
                print('You`ve closed this game. GL.')
                return 'break'
            else:
                print('You`ve written something wrong, write right direction.')

    def check_heroes(self):
        for i in range(len(self.hero_list) - 1):
            for j in range(i + 1, len(self.hero_list)):
                if (self.hero_list[i].x == self.hero_list[j].x) and (self.hero_list[i].y == self.hero_list[j].y):
                    if self.hero_list[i].team == self.hero_list[j].team:
                        return 'ally'
                    condition = self.fight(self.hero_list[i], self.hero_list[j])
                    if condition is None:
                        return 'break'
                    return False
        return True

    def fight(self, hero, enemy):
        hr_1 = hero
        hr_2 = enemy
        while True:
            sleep(0.2)
            if hr_1.stun_status > 0:
                hr_1.stun_status -= 1
            else:
                hr_1.strike(hr_2)
            if not ((hr_1.health >= 0) and (hr_2.health >= 0)):
                condition = self.hero_health_check()
                if condition == 'end':
                    return None
                return False
            hr_1, hr_2 = hr_2, hr_1

    def hero_health_check(self):
        for hero in self.hero_list:
            if hero.health < 0:
                print(f'{hero.name} ({hero.team}) was killed.\n')
                self.hero_list.remove(hero)
                self.team_dict[hero.team].remove(hero)
                condition = self.team_check()
                if condition is None:
                    return 'end'

    def team_check(self):
        for team in self.team_dict.keys():
            if len(self.team_dict[team]) == 0:
                self.team_dict.pop(team)
                self.team_list.remove(team)
                if len(self.team_dict.keys()) > 1:
                    print(f"Team {team} was destroyed!\n{len(self.team_dict.keys())} teams are left!")
                    return True
                else:
                    print(f'END OF THE GAME! \nTEAM {self.team_list[0]} IS A WINNER!')
                    return None
        return True

    def heroes_status(self):
        print()
        for hero in self.hero_list:
            print(f"{hero.name} ({hero.team}): [{hero.x}, {hero.y}], {hero.health} HP")
        print()
