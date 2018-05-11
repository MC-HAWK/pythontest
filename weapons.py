class weapons(items):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str(self):
        return "{}\n=====\n{}value: {}\ndamage: {}".format(self.name,
                                                           self.description,
                                                           self.value,
                                                           self.damage)


class shovel(weapons):
    def __init__(self):
        super().__init__(name="Shovel",
                         description="Useful for digging and not much else.",
                         value=3,
                         damage=5)
