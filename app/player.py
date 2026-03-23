class Player:
    def __init__(self, uid, name, score=0):
        self._uid = uid
        self._name = name
        self._score = score

    def __repr__(self):
        return f"Player(name='{self._name}', uid='{self._uid}', score={self._score})"

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