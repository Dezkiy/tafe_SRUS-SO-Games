import unittest

from app.player import Player
from app.player_hash_map import PlayerHashMap


class TestPlayerHashMap(unittest.TestCase):
    def setUp(self):
        self.player_map = PlayerHashMap()

    def test_set_and_get(self):
        self.player_map["uid_1"] = "Bob"
        player = self.player_map["uid_1"]
        self.assertEqual(player.uid, "uid_1")
        self.assertEqual(player.name, "Bob")

    def test_update_existing(self):
        self.player_map["uid_1"] = "Bob"
        self.player_map["uid_1"] = "Jenkins"
        self.assertEqual(len(self.player_map), 1)
        self.assertEqual(self.player_map["uid_1"].name, "Jenkins")

    def test_set_player_instance(self):
        player = Player("uid_2", "Beth")
        self.player_map["uid_2"] = player
        self.assertIs(self.player_map["uid_2"], player)

    def test_delete(self):
        self.player_map["uid_1"] = "Bob"
        del self.player_map["uid_1"]
        self.assertEqual(len(self.player_map), 0)
        with self.assertRaises(KeyError):
            _ = self.player_map["uid_1"]
        with self.assertRaises(KeyError):
            del self.player_map["uid_1"]

    def test_collision_chaining(self):
        self.player_map["a"] = "Alpha"
        self.player_map["k"] = "Kappa"
        self.assertEqual(len(self.player_map), 2)
        self.assertEqual(self.player_map["a"].name, "Alpha")
        self.assertEqual(self.player_map["k"].name, "Kappa")

    def test_display(self):
        self.player_map["uid_1"] = "Bob"
        self.player_map["uid_2"] = "Jenkins"
        output = self.player_map.display()
        self.assertIn("index", output)
        self.assertIn("Player", output)


if __name__ == "__main__":
    unittest.main()
