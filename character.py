from random import randint


class Character:
    def __init__(self, _str, _agl, _int, name, team, x, y):
        self.str = _str
        self.agl = _agl
        self.int = _int
        self.health = self.str * 50
        self.evasion = self.agl * 2
        self.chance_spec_attack = self.int * 1.6
        self.team = team
        self.name = name
        self.stun_status = 0
        self.x = x
        self.y = y
        if self.attribute == 'int':
            self.damage_min = _int * 3 - 4
            self.damage_max = _int * 3 + 5
        elif self.attribute == 'str':
            self.damage_min = self.str * 2 - 3
            self.damage_max = self.str * 2 + 4
        elif self.attribute == 'ag':
            self.damage_min = self.agl * 3 - 5
            self.damage_max = self.agl * 3 + 6

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
            if randint(1, 100) < enemy.evasion:
                print(f"{enemy.name} ({enemy.team}) has evaded from {self.name}`s ({self.team}) strike!\n===")
            else:    
                dmg = self.damage()
                enemy.health = enemy.health - dmg
                print(f"{self.name} ({self.team}) has damaged {enemy.name} ({enemy.team}) for {dmg}\n===")


class Wizard(Character):
    def __init__(self, name, team, x=9, y=9):
        self.first_skill = Wizard.fireball
        self.second_skill = Wizard.polymorph
        self.attribute = 'int'
        super(Wizard, self).__init__(13, 7, 30, name, team, x, y)

    def fireball(self, enemy):
        dmg = self.damage() * 4
        enemy.health = enemy.health - dmg
        print(f"{self.name} ({self.team}) has used Fireball."
              f"\n{self.name} ({self.team}) has damaged {enemy.name} ({enemy.team}) for {dmg}\n===")

    def polymorph(self, enemy):
        enemy.stun_status += 2
        print(f'{self.name} ({self.team}) has used Polymorph.'
              f"\n{self.name} ({self.team}) has stunned {enemy.name} ({enemy.team}) for 2 turns.\n===")


class Warlock(Character):
    def __init__(self, name, team, x=9, y=9):
        self.first_skill = Warlock.lifesteal
        self.second_skill = Warlock.defile
        self.attribute = 'int'
        super(Warlock, self).__init__(12, 7, 31, name, team, x, y)

    def lifesteal(self, enemy):
        dmg = self.damage() * 2
        enemy.health = enemy.health - dmg
        self.health = self.health + dmg
        print(f"{self.name} ({self.team}) has used Lifesteal!"
              f'{self.name} ({self.team}) has damaged {enemy.name} ({enemy.team}) for {dmg},\n'
              f'And has healed himself for {dmg}.\n===')

    def defile(self, enemy):
        enemy.damage_min = enemy.damage_min - 10
        enemy.damage_max = enemy.damage_max - 10
        enemy.evasion = enemy.evasion - 5
        print(f'{self.name} ({self.team}) has used Defile.'
              f'{enemy.name} ({enemy.team}) has lost 10 damage and 5 evasion points.\n===')


class Druid(Character):
    def __init__(self, name, team, x=9, y=9):
        self.first_skill = Druid.self_heal
        self.second_skill = Druid.swipe
        self.attribute = 'int'
        self.class_name = 'Druid'
        super(Druid, self).__init__(17, 9, 24, name, team, x, y)

    def self_heal(self, enemy):
        heal = self.damage() * 5
        self.health = self.health + heal
        print(f"{self.name} ({self.team}) has used Self Heal!"
            f'{self.name} ({self.team}) has healed for {heal} HP.\n===')

    def swipe(self, enemy):
        dmg = self.damage() * 3
        enemy.health = enemy.health - dmg
        print(f"{self.name} ({self.team}) has used Swipe!"
              f'{self.name} ({self.team}) has damaged {enemy.name} ({enemy.team}) for {dmg}\n===')


class Barbarian(Character):
    def __init__(self, name, team, x=9, y=9):
        self.first_skill = Barbarian.stand_as_one
        self.second_skill = Barbarian.barbarian_strike
        self.attribute = 'str'
        super(Barbarian, self).__init__(32, 7, 11, name, team, x, y)

    def stand_as_one(self, enemy):
        self.health *= 1.25
        print(f'{self.name} ({self.team}) has used Stand as One.'
              f'His health has increased in 1.25 times.\n===')

    def barbarian_strike(self, enemy):
        dmg = self.damage() * 6
        s_dmg = dmg / 3
        enemy.health = enemy.health - dmg
        self.health = self.health - s_dmg
        enemy.stun_status += 1
        print(f"{self.name} ({self.team}) has used Barbarian!"
              f'{self.name} ({self.team}) has damaged {enemy.name} ({enemy.team}) for {dmg} and stunned him for a turn,'
              f'But has damaged himself for {s_dmg}\n===')



class Warrior(Character):
    def __init__(self, name, team, x=9, y=9):
        self.attribute = 'str'
        self.first_skill = Warrior.fury
        self.second_skill = Warrior.bash
        super(Warrior, self).__init__(35, 5, 10, name, team, x, y)

    def fury(self, enemy):
        dmg = self.damage() * 3
        s_dmg = self.damage()
        enemy.health = enemy.health - dmg
        self.health = self.health - s_dmg
        print(f"{self.name} ({self.team}) has used Fury!"
              f'{self.name} ({self.team}) has damaged {enemy.name} ({enemy.team}) for {dmg},\n'
              f'But has damaged himself for {s_dmg}\n===')

    def bash(self, enemy):
        enemy.stun_status += 3
        print(f'{self.name} ({self.team}) has used Bash.'
              f"\n{self.name} ({self.team}) has stunned {enemy.name} ({enemy.team}) for 3 turns.\n===")

class Paladin(Character):
    def __init__(self, name, team, x=9, y=9):
        self.attribute = 'str'
        self.first_skill = Paladin.heavenly_grace
        self.second_skill = Paladin.lifelink
        super(Paladin, self).__init__(30, 10, 10, name, team, x, y)

    def heavenly_grace(self, enemy):
        heal = self.damage() * 10
        self.health = self.health + heal
        f"{self.name} ({self.team}) has used Heavenly Grace."
        f'{self.name} ({self.team}) has healed for {heal} HP.\n==='

    def lifelink(self, enemy):
        dmg = self.damage() * 3.5 // 1
        s_dmg = self.damage()
        enemy.health = enemy.health - dmg
        self.health = self.health + s_dmg
        print(f"{self.name} ({self.team}) has used Lifelink!"
              f'{self.name} ({self.team}) has damaged {enemy.name} ({enemy.team}) for {dmg},\n'
              f'And has healed himself for {s_dmg}.\n===')


class Rogue(Character):
    def __init__(self, name, team, x=9, y=9):
        self.attribute = 'ag'
        self.first_skill = Rogue.backstab
        self.second_skill = Rogue.stealth
        super(Rogue, self).__init__(17, 22, 11, name, team, x, y)

    def backstab(self, enemy):
        dmg = self.damage() * 2.5 // 1
        enemy.health = enemy.health - dmg
        print(f"{self.name} ({self.team}) has used Backstab!"
              f'{self.name} ({self.team}) has damaged {enemy.name} ({enemy.team}) for {dmg}\n===')

    def stealth(self, enemy):
        self.stun_status = self.stun_status - 2
        print(f"{self.name} ({self.team}) has used Stealth!"
              f"Next 2 stuns will not work!\n===")


class Hunter(Character):
    def __init__(self, name, team, x=9, y=9):
        self.first_skill = Hunter.deadly_shot
        self.second_skill = Hunter.extra_dmg
        self.attribute = 'ag'
        super(Hunter, self).__init__(22, 22, 6, name, team, x, y)

    def deadly_shot(self, enemy):
        dmg = self.damage() * 3.5 // 1
        enemy.health = enemy.health - dmg
        print(f"{self.name} ({self.team}) has used Deadly Shot!"
              f'{self.name} ({self.team}) has damaged {enemy.name} ({enemy.team}) for {dmg}\n===')

    def extra_dmg(self, enemy):
        self.damage_min += 10
        self.damage_max += 10
        print(f"{self.name} ({self.team}) has used Roar!"
              f'{self.name} ({self.team}) has gained extra 10 damage.\n===')


class Monk(Character):
    def __init__(self, name, team, x=9, y=9):
        self.first_skill = Monk.brewery
        self.second_skill = Monk.dragon_dance
        self.attribute = 'ag'
        super(Monk, self).__init__(15, 25, 10, name, team, x, y)

    def brewery(self, enemy):
        enemy.damage_min = enemy.damage_min - 5
        enemy.damage_max = enemy.damage_max - 5
        dmg = self.damage() * 2
        enemy.health = enemy.health - dmg
        print(f"{self.name} ({self.team}) has used Brewery."
            f'{self.name} ({self.team}) has damaged {enemy.name} ({enemy.team}) for {dmg}\n'
              f'Also, {enemy.name} ({enemy.team}) has lost 5 damage.\n===')

    def dragon_dance(self, enemy):
        self.evasion = 200
        print(f"{self.name} ({self.team}) has used Dragon Dance."
              f"{self.name} has gained Timeless Evasion\n===")
