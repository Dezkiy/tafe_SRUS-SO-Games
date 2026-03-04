import unittest
from app.player_list import PlayerList
from app.player_node import PlayerNode
from app.player import Player

class TestPlayerList(unittest.TestCase):
    
    def setUp(self):
        self.player_list = PlayerList()

    def test_is_player_list_empty(self):
        self.assertEqual(self.player_list.is_empty(), True)

    def test_insert_first(self):
        player_node = PlayerNode(Player("uid_1", "Bob1"))
        self.player_list.insert_first(player_node)
        output = self.player_list.display()

        assert "List first --> last:" in output
        assert "uid_1" in output

    def test_instance_updated_when_new_items_inserted(self):
        node1 = PlayerNode(Player("uid_1", "Bob1"))
        node2 = PlayerNode(Player("uid_2", "Bob2"))

        self.assertIsNone(self.player_list.last)

        self.player_list.insert_first(node1)
        self.assertIs(self.player_list.first, node1)
        self.assertIs(self.player_list.last, node1)

        self.player_list.insert_first(node2)
        self.assertIs(self.player_list.first, node2)
        self.assertIs(self.player_list.last, node1)

if __name__ == "__main__":
    unittest.main()
