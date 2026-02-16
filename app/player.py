class Player:
    def __init__(self, uid, name):
        self._uid = uid
        self._name = name

    def __str__(self):
        return f"Player {self._uid}: {self._name}"

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