import unittest
from app.player_list import PlayerList
from app.player_node import PlayerNode
from app.player import Player

class TestPlayerList(unittest.TestCase):
    
    def setUp(self):
        self.player_list = PlayerList()
        self.node1 = PlayerNode(Player("uid_1", "Bob1"))
        self.node2 = PlayerNode(Player("uid_2", "Bob2"))
        self.node3 = PlayerNode(Player("uid_3", "Bob3"))

    def test_is_player_list_empty(self):
        self.assertEqual(self.player_list.is_empty(), True)

    def test_insert_first(self):
        player_node = PlayerNode(Player("uid_1", "Bob1"))
        self.player_list.insert_first(player_node)
        output = self.player_list.display()

        assert "List first --> last:" in output
        assert "uid_1" in output

    def test_instance_updated_when_new_items_inserted(self):
        self.assertIsNone(self.player_list.last)

        self.player_list.insert_first( self.node1)
        self.assertIs(self.player_list.first,  self.node1)
        self.assertIs(self.player_list.last,  self.node1)

        self.player_list.insert_first( self.node2)
        self.assertIs(self.player_list.first, self.node2)
        self.assertIs(self.player_list.last, self.node1)

    def test_insert_last(self):
        self.player_list.insert_last( self.node1)
        self.assertIs(self.player_list.first,  self.node1)
        self.assertIs(self.player_list.last,  self.node1)
        self.assertIsNone(self.node1.previous)
        self.assertIsNone(self.node1.next)

        self.player_list.insert_last(self.node2)
        self.assertIs(self.player_list.first, self.node1)
        self.assertIs(self.player_list.last, self.node2)
        self.assertIs(self.node1.next, self.node2)
        self.assertIs(self.node2.previous, self.node1)
        self.assertIsNone(self.node2.next)

    def test_delete_first(self):
        self.assertIsNone(self.player_list.delete_first())

        self.player_list.insert_last(self.node1)
        removed = self.player_list.delete_first()
        self.assertIs(removed, self.node1)
        self.assertIsNone(self.player_list.first)
        self.assertIsNone(self.player_list.last)
        self.assertIsNone(removed.previous)
        self.assertIsNone(removed.next)

        self.player_list.insert_last(self.node1)
        self.player_list.insert_last(self.node3)
        removed = self.player_list.delete_first()
        self.assertIs(removed, self.node1)
        self.assertIs(self.player_list.first, self.node3)
        self.assertIs(self.player_list.last, self.node3)
        self.assertIsNone(self.node3.previous)
        self.assertIsNone(removed.previous)
        self.assertIsNone(removed.next)

    def test_delete_last(self):
        self.assertIsNone(self.player_list.delete_last())

        self.player_list.insert_last(self.node1)
        removed = self.player_list.delete_last()
        self.assertIs(removed, self.node1)
        self.assertIsNone(self.player_list.first)
        self.assertIsNone(self.player_list.last)
        self.assertIsNone(removed.previous)
        self.assertIsNone(removed.next)

        self.player_list.insert_last(self.node1)
        self.player_list.insert_last(self.node3)
        removed = self.player_list.delete_last()
        self.assertIs(removed, self.node3)
        self.assertIs(self.player_list.first, self.node1)
        self.assertIs(self.player_list.last, self.node1)
        self.assertIsNone(self.node1.next)
        self.assertIsNone(removed.previous)
        self.assertIsNone(removed.next)

if __name__ == "__main__":
    unittest.main()
