class Player:
    def __init__(self, uid, name, score=0):
        self._uid = uid
        self._name = name
        self._score = score

    def __repr__(self):
        return f"Player(name='{self._name}', uid='{self._uid}', score={self._score})"

    def __lt__(self, item):
        return self._score < item._score

    def __eq__(self, player):
        return (
            self._uid == player._uid and
            self._name == player._name and
            self._score == player._score
        )
    
    @property
    def uid(self):
        return self._uid
    
    @uid.setter
    def uid(self, value):     
        self._uid = value
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):     
        self._name = value

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, value):
        if value < 0:
            raise ValueError("Score cannot be negative.")
        self._score = value

    @classmethod
    def sort_quickly_desc(cls, players):
        players = list(players)
        if len(players) <= 1:
            return players
        pivot = players[0]
        left = []
        right = []
        for player in players[1:]:
            if player.score > pivot.score:
                left.append(player)
            else:
                right.append(player)
        return cls.sort_quickly_desc(left) + [pivot] + cls.sort_quickly_desc(right)
