import unittest
from app.player import Player

class TestPlayer(unittest.TestCase):
    player_one = Player("1","Bob")
    player_two = Player("2","Timofei", 2)


    def test_initialization(self):
        self.assertEqual(self.player_one._uid, "1")
        self.assertEqual(self.player_one._name, "Bob")

    def test_repr_defaults_score_to_zero(self):
        self.assertEqual(str(self.player_one), "Player(name='Bob', uid='1', score=0)")

    def test_repr_includes_custom_score(self):
        self.assertEqual(str(self.player_two), "Player(name='Timofei', uid='2', score=2)")

    def test_negative_score_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.player_one.score = -1

if __name__ == "__main__":
    unittest.main()
