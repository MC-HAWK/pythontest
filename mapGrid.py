import enemies
import items


class MapGrid:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def intro_text(self):
    raise NotImplementedError()


def modify_player(self, player):
    raise NotImplementedError()


class StartingRoom(MapGrid):
    def intro_text(self):
        return """
        You slowly open your eyes to find yourself alone in a damp, poorly lit room
        with stone walls. There are three paths out of the room.
        """


def modify_player(self, player):
        # Room has no action on player
        pass


class LootRoom(MapGrid):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, player):
        player.inventory.append(self.item)

    def modify_player(self, player):
        self.add_loot(player)


class EnemyRoom(MapGrid):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage,
                                                                           the_player.hp))
