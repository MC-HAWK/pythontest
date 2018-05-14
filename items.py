# general Items class
class Items():
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n=====\n{}".format(self.name, self.description, self.value)


# Gold class subclass of the super class Items
class Gold(Items):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Gold",
                         description="A round  coin with {} stamped on the front."
                         .format(str(self.amt)),
                         value=self.amt)


# Weapons subclass of items and various subclasses of Weapons
class Weapons(Items):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str(self):
        return "{}\n=====\n{}value: {}\ndamage: {}".format(self.name,
                                                           self.description,
                                                           self.value,
                                                           self.damage)


class Shovel(Weapons):
    def __init__(self):
        super().__init__(name="Shovel",
                         description="Useful for digging and not much else.",
                         value=3,
                         damage=3)


class ShortSword(Weapons):
    def __init__(self):
        super().__init__(name="Short Sword",
                         description="An average weapon for an average adventurer.",
                         value=10,
                         damage=6)


class BattleAxe(Weapons):
    def __init__(self):
        super().__init__(name="Battle Axe",
                         description="A double sided axe, it's weight makes it "
                         "difficult to manuever.",
                         value=30,
                         damage=10)


class LongBow(Weapons):
    def __init__(self):
        super().__init__(name="Long Bow",
                         description="A simple wooden bow.",
                         value=10,
                         damage=5)


class Rock(Weapons):
    def __init__(self):
        super().__init__(name="Rock",
                         description="It's just a rock.",
                         value=0,
                         damage=2)


class FlamingoMallet(Weapons):
    def __init__(self):
        super().__init__(name="Flamingo Mallet",
                         description="You wouldn't want to run afowl of this hammer.",
                         value=50,
                         damage=17)
