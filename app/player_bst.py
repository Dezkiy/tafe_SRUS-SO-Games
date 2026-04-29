from app.player_bnode import PlayerBNode


class PlayerBST:
    def __init__(self):
        self._root = None

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, value):
        self._root = value

    #In accordance with Step 5.a "It should take a Player object as the only argument."
    def insert(self, player):
        self.root = self._insert(self.root, player)
        
    def _insert(self, current_node, player):
        if current_node is None:
            return PlayerBNode(player)

        if player.name < current_node.player.name:
            current_node.left = self._insert(current_node.left, player)
        elif player.name > current_node.player.name:
            current_node.right = self._insert(current_node.right, player)
        else:
            # To avoid duplicating nodes. Step 5.b.4
            current_node.player = player

        return current_node

    def search(self, name):
        return self._search(self.root, name)

    def _search(self, current_node, name):
        if current_node is None or current_node.player.name == name:
            return current_node

        if name < current_node.player.name:
            return self._search(current_node.left, name)

        return self._search(current_node.right, name)
