class Character(object):
    """Documentation for Character

    """
    __hp = 10
    __str = 3
    def __init__(self, name = None, hp = None, _str = None):
        super(Character, self).__init__()
        self.name = name
        if name == None:
            self.name = input("Please enter a character name:")
        if hp != None:
            self.__hp = hp
        if _str != None:
            self.__str = _str

    def speak(self, msg):
        print('%s says, "%s".(currently at %d)' % (self.name, msg, self.__hp))

    def getHP(self):
        return self.__hp

    def adjustHP(self, delta):
        self.__hp += delta
        if self.__hp < 0:
            self.__hp = 0

    def getStr(self):
        return self.__str


class Npc(Character):
    """Documentation for Npc

    """
    def __init__(self, name = None, hp = None):
        if name == None:
            name = "Mob"
        super(Npc, self).__init__(name, hp)

    def damage(self, amount):
        self.adjustHP(-amount)
        

class Boss(Npc):
    """Documentation for Boss

    """
    def __init__(self, name = None, hp = None):
        if name == None:
            name = "Boss"
        if hp == None:
            hp = 100
        super(Boss, self).__init__(name, hp)


class Player(Character):
    """Documentation for Player

    """
    __xp = 0
    __level = 1
    def __init__(self):
        super(Player, self).__init__()
        self.__hp = 30

    def levelup(self, xp):
        self.__xp += xp
        if self.__xp/100 > self.__level:
            self.__level += 1
            self.__str += 1
        return self.__level

    def getLevel(self):
        return self.__level
    
