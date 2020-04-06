class Character:
    def __init__(self, _str, _agl, _int, team, name):
        self.str = _str
        self.agl = _agl
        self.int = _int
        self.health = self.str * 25
        self.evasion = self.agl * 2
        self.chance_spec_attack = self.int * 2
        self.team = team
        self.name = name


class Strength(Character):
    def __init__(self, _str, _agl, _int):
        super.__init__(_str, _agl, _int)
        self.damage_min = self.str * 2 - 3
        self.damage_max = self.str * 2 + 4


class Agility(Character):
    def __init__(self, _str, _agl, _int):
        super.__init__(_str, _agl, _int)
        self.damage_min = self.agl * 3 - 5
        self.damage_max = self.agl * 3 + 6


class Intelligence(Character):
    def __init__(self, _str, _agl, _int, name, team):
        super.__init__(_str, _agl, _int, name, team)
        self.damage_min = self.int * 3 - 4
        self.damage_max = self.int * 3 + 5


class Wizard(Intelligence):
    def __init__(self, name, team):
        super.__init__(13, 7, 30, name, team)

    def fireball(self):
        pass

    def polymorph(self):
        pass


class Warlock(Intelligence):
    def __init__(self, name, team):
        super.__init__(0, 0, 0, name, team)

    def spell_1(self):
        pass

    def spell_2(self):
        pass


class Druid(Intelligence):
    def __init__(self, name, team):
        super.__init__(0, 0, 0, name, team)

    def spell_1(self):
        pass

    def spell_2(self):
        pass


class Barbarian(Strength):
    def __init__(self, name, team):
        super.__init__(0, 0, 0, name, team)

    def spell_1(self):
        pass

    def spell_2(self):
        pass


class Warrior(Strength):
    def __init__(self, name, team):
        super.__init__(0, 0, 0, name, team)

    def spell_1(self):
        pass

    def spell_2(self):
        pass


class Paladin(Strength):
    def __init__(self, name, team):
        super.__init__(0, 0, 0, name, team)

    def spell_1(self):
        pass

    def spell_2(self):
        pass


class Rogue(Agility):
    def __init__(self, name, team):
        super.__init__(0, 0, 0, name, team)

    def spell_1(self):
        pass

    def spell_2(self):
        pass


class Hunter(Agility):
    def __init__(self, name, team):
        super.__init__(0, 0, 0, name, team)

    def spell_1(self):
        pass

    def spell_2(self):
        pass


class Monk(Agility):
    def __init__(self, name, team):
        super.__init__(0, 0, 0, name, team)

    def spell_1(self):
        pass

    def spell_2(self):
        pass
