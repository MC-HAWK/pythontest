class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

        def is_alive(self):
            return self.hp > 0


class Spider(Enemy):
    def __init__(self):
        super().__init__(name="Spider", hp=5, damage=1)
