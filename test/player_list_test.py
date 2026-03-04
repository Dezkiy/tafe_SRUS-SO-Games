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

if __name__ == "__main__":
    unittest.main()
