from random import randint


class Character:
    def __init__(self, _str, _agl, _int, team, name, x, y):
        self.str = _str
        self.agl = _agl
        self.int = _int
        self.health = self.str * 25
        self.evasion = self.agl * 2
        self.chance_spec_attack = self.int * 1.5
        self.team = team
        self.name = name
        self.stun_status = 0
        self.x = x
        self.y = y

    def damage(self):
        dmg = randint(self.damage_min, self.damage_max)
        return dmg

    def strike(self, enemy):
        if randint(1, 100) <= self.chance_spec_attack:
            if randint(0, 1):
                self.first_skill(self, enemy)
            else:
                self.second_skill(self, enemy)
        else:
            dmg = self.damage()
            enemy.health = enemy.health - dmg
            print(f"{self.name} ({self.team}) has damaged {enemy.name} ({enemy.team}) for {dmg}\n===")


class Strength(Character):
    def __init__(self, _str, _agl, _int, team, name, x, y, first_skill, second_skill):
        super(Character, self).__init__(_str, _agl, _int, team, name, x, y, first_skill, second_skill)
        self.damage_min = self.str * 2 - 3
        self.damage_max = self.str * 2 + 4


class Agility(Character):
    def __init__(self, _str, _agl, _int, team, name, x, y, first_skill, second_skill):
        super(Character, self).__init__(_str, _agl, _int, team, name, x, y, first_skill, second_skill)
        self.damage_min = self.agl * 3 - 5
        self.damage_max = self.agl * 3 + 6


class Intelligence(Character):
    def __init__(self, _str, _agl, _int, team, name, x, y):
        super(Character, self).__init__(_str, _agl, _int, team, name, x, y)


class Wizard(Intelligence):
    def __init__(self, name, team, x=9, y=9):
        self.first_skill = Wizard.fireball
        self.second_skill = Wizard.polymorf
        _int = 30
        self.damage_min = _int * 3 - 4
        self.damage_max = _int * 3 + 5
        super(Intelligence, self).__init__(13, 7, 30, team, name, x, y)

    def fireball(self, enemy):
        dmg = self.damage() * 4
        enemy.health = enemy.health - dmg
        print(f"{self.name} ({self.team}) has used Fireball."
              f"\n{self.name} ({self.team}) has damaged {enemy.name} ({enemy.team}) for {dmg}\n===")

    def polymorf(self, enemy):
        enemy.stun_status += 2
        print(f'{self.name} ({self.team}) has used Polymorph.'
              f"\n{self.name} ({self.team}) has stunned {enemy.name} ({enemy.team}) for 2 turns.\n===")


class Warlock(Intelligence):
    def __init__(self, name, team, x=9, y=9):
        super.__init__(0, 0, 0, name, team, x, y)

    def spell_1(self):
        pass

    def spell_2(self):
        pass


class Druid(Intelligence):
    def __init__(self, name, team, x=9, y=9):
        super.__init__(0, 0, 0, name, team, x, y)

    def spell_1(self):
        pass

    def spell_2(self):
        pass


class Barbarian(Strength):
    def __init__(self, name, team, x=9, y=9):
        super.__init__(0, 0, 0, name, team, x, y)

    def spell_1(self):
        pass

    def spell_2(self):
        pass


class Warrior(Strength):
    def __init__(self, name, team, x=9, y=9):
        super.__init__(0, 0, 0, name, team, x, y)

    def spell_1(self):
        pass

    def spell_2(self):
        pass


class Paladin(Strength):
    def __init__(self, name, team, x=9, y=9):
        super.__init__(0, 0, 0, name, team, x, y)

    def spell_1(self):
        pass

    def spell_2(self):
        pass


class Rogue(Agility):
    def __init__(self, name, team, x=9, y=9):
        super.__init__(0, 0, 0, name, team, x, y)

    def spell_1(self):
        pass

    def spell_2(self):
        pass


class Hunter(Agility):
    def __init__(self, name, team, x=9, y=9):
        super.__init__(0, 0, 0, name, team, x, y)

    def spell_1(self):
        pass

    def spell_2(self):
        pass


class Monk(Agility):
    def __init__(self, name, team, x=9, y=9):
        super.__init__(0, 0, 0, name, team, x, y)

    def spell_1(self):
        pass

    def spell_2(self):
        pass
