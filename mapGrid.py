import enemies
import items
import actions
import world


class MapGrid:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def intro_text(self):
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

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()


def adjacent_moves(self):
    """Returns all move actions for adjacent tiles."""
    moves = []
    if world.tile_exists(self.x + 1, self.y):
        moves.append(actions.MoveEast())
    if world.tile_exists(self.x - 1, self.y):
        moves.append(actions.MoveWest())
    if world.tile_exists(self.x, self.y - 1):
        moves.append(actions.MoveNorth())
    if world.tile_exists(self.x, self.y + 1):
        moves.append(actions.MoveSouth())
    return moves


def available_actions(self):
    """Returns all of the available actions in this room."""
    moves = self.adjacent_moves()
    moves.append(actions.ViewInventory())

    return moves


class LeaveCaveRoom(MapGrid):
    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... it grows as you get closer! It's sunlight!


        Victory is yours!
        """

    def modify_player(self, player):
        player.victory = True
