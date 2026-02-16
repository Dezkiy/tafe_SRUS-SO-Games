import unittest
from app.player import Player

class TestPlayer(unittest.TestCase):
    player_one = Player("1","Bob")

    def test_initialization(self):
        self.assertEqual(self.player_one._uid, "1")
        self.assertEqual(self.player_one.name, "Bob")

    def test_str(self):
        self.assertEqual(str(self.player_one), "Player 1: Bob")

if __name__ == "__main__":
    unittest.main()
