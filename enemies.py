class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

        def is_alive(self):
            return self.hp > 0


class Spider(Enemy):
    def __init__(self):
        super().__init__(name="Spider", hp=3, damage=1)


class GiantPython(Enemy):
    def __init__(self):
        super().__init__(name="Giant Python", hp=12, damage=5)


class Skeleton(Enemy):
    def __init__(self):
        super().__init__(name="Skeleton", hp=5, damage=3)


class BronzeDragon(Enemy):
    def __init__(self):
        super().__init__(name="Bronze Dragon", hp=40, damage=10)
