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

    def to_sorted_list(self):
        players = []
        self._to_sorted_list(self.root, players)
        return players

    def _to_sorted_list(self, current_node, players):
        if current_node is None:
            return

        self._to_sorted_list(current_node.left, players)
        players.append(current_node.player)
        self._to_sorted_list(current_node.right, players)

    def balance(self):
        players = self.to_sorted_list()
        self.root = self._build_balanced_tree(players, 0, len(players) - 1)

    def _build_balanced_tree(self, players, start, end):
        if start > end:
            return None

        middle = (start + end) // 2
        current_node = PlayerBNode(players[middle])
        current_node.left = self._build_balanced_tree(players, start, middle - 1)
        current_node.right = self._build_balanced_tree(players, middle + 1, end)
        return current_node
