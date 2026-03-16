from app.player import Player
from app.player_list import PlayerList
from app.player_node import PlayerNode


class PlayerHashMap:
    SIZE = 10

    def __init__(self):
        self._buckets = [PlayerList() for _ in range(self.SIZE)]
        self._count = 0

    def get_index(self, key):
        return Player.hash(key) % self.SIZE

    def __getitem__(self, key):
        index = self.get_index(key)
        current = self._buckets[index].first

        while current:
            if current.key == key:
                return current.player
            current = current.next

        raise KeyError(key)

    def __setitem__(self, key, value):
        index = self.get_index(key)
        current = self._buckets[index].first

        while current:
            if current.key == key:
                if isinstance(value, Player):
                    current.player = value
                else:
                    current.player.name = value
                return
            current = current.next

        player = value if isinstance(value, Player) else Player(key, value)
        self._buckets[index].insert_last(PlayerNode(player))
        self._count += 1

    def __delitem__(self, key):
        index = self.get_index(key)
        removed = self._buckets[index].delete(key)
        if removed is None:
            raise KeyError(key)
        self._count -= 1

    def __len__(self):
        return self._count
