import unittest

from app.player import Player
from app.player_bst import PlayerBST


class TestPlayerBST(unittest.TestCase):
    def setUp(self):
        self.player_bst = PlayerBST()

    def test_insert_root_when_tree_is_empty(self):
        player = Player("uid_1", "Sam")
        self.player_bst.insert(player)

        self.assertIsNotNone(self.player_bst.root)
        self.assertIs(self.player_bst.root.player, player)

    def test_insert_adds_smaller_name_to_left_subtree(self):
        root_player = Player("uid_1", "Sam")
        left_player = Player("uid_2", "Bob")
        self.player_bst.insert(root_player)
        self.player_bst.insert(left_player)

        self.assertIsNotNone(self.player_bst.root.left)
        self.assertIs(self.player_bst.root.left.player, left_player)

    def test_insert_adds_greater_name_to_right_subtree(self):
        root_player = Player("uid_1", "Sam")
        right_player = Player("uid_2", "Tim")
        self.player_bst.insert(root_player)
        self.player_bst.insert(right_player) 

        self.assertIsNotNone(self.player_bst.root.right) 
        self.assertIs(self.player_bst.root.right.player, right_player) 

    def test_insert_updates_existing_node_when_name_is_duplicate(self):
        first_player = Player("uid_1", "Sam", 10)
        updated_player = Player("uid_2", "Sam", 20)
        self.player_bst.insert(first_player)
        self.player_bst.insert(updated_player)

        self.assertIs(self.player_bst.root.player, updated_player)
        self.assertIsNone(self.player_bst.root.left)
        self.assertIsNone(self.player_bst.root.right)

    def test_search_returns_root_when_name_matches_root(self):
        player = Player("uid_1", "Sam")
        self.player_bst.insert(player)
        found_node = self.player_bst.search("Sam")

        self.assertIs(found_node, self.player_bst.root)
        self.assertIs(found_node.player, player)

    def test_search_returns_node_from_left_subtree(self):
        root_player = Player("uid_1", "Sam")
        left_player = Player("uid_2", "Bob")
        self.player_bst.insert(root_player)
        self.player_bst.insert(left_player)
        found_node = self.player_bst.search("Bob")

        self.assertIs(found_node, self.player_bst.root.left)
        self.assertIs(found_node.player, left_player)

    def test_search_returns_node_from_right_subtree(self):
        root_player = Player("uid_1", "Sam")
        right_player = Player("uid_2", "Tim")
        self.player_bst.insert(root_player)
        self.player_bst.insert(right_player)

        found_node = self.player_bst.search("Tim")

        self.assertIs(found_node, self.player_bst.root.right)
        self.assertIs(found_node.player, right_player)

    def test_search_returns_none_when_name_is_not_found(self):
        root_player = Player("uid_1", "Sam")
        self.player_bst.insert(root_player)

        found_node = self.player_bst.search("Alex")

        self.assertIsNone(found_node)


if __name__ == "__main__":
    unittest.main()
