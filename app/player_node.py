from app.player import Player

class PlayerNode:
    def __init__(self, player):
        self.player = player
        # self.player = Player()
        self.__next = None
        self.__previous = None
    
    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, next):
        self.__next = next

    @property
    def previous(self):
        return self.__previous
    
    @previous.setter
    def previous(self, previous):
        self.__previous = previous

    @property
    def key(self):
        if self.player is None:
            return None
        return self.player.uid

    def __str__(self):
        prev_node = self.__previous.key if self.__previous else None
        next_node = self.__next.key if self.__next else None
        return f"PlayerNode(key(player_uid) = {self.key}, prev = {prev_node}, next = {next_node})"
