import unittest, random
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

    def test_sort_players(self):
        players = [Player(name="Alice", uid='01', score=10), Player(name="Bob", uid='02', score=5), Player(name="Charlie", uid='03', score=15)]
        # note: ensure initialization code is valid for **your** implementation.
        # For example, is your parameter called uid? is the first parameter name?

        # do **not** change the following code:
        sorted_players = sorted(players)

        # players must be sorted by score as shown here:
        manually_sorted_players = [Player(name="Bob", uid='02', score=5), Player(name="Alice", uid='01', score=10), Player(name="Charlie", uid='03', score=15)]

        self.assertListEqual(sorted_players, manually_sorted_players)


    def test_players_can_be_compared_by_score(self):
        # note: ensure initialization code is valid for **your** implementation
        alice = Player(name="Alice", uid='01', score=10)
        bob = Player(name="Bob", uid='02', score=5)

        # Add the appropriate expression to the following assert test
        self.assertLess(bob, alice)

    def test_sort_quickly_desc(self):
        players = [
            Player(name="Alice", uid='01', score=10),
            Player(name="Bob", uid='02', score=5),
            Player(name="Charlie", uid='03', score=15),
            Player(name="Diana", uid='04', score=10),
        ]

        sorted_players = Player.sort_quickly_desc(players)

        manually_sorted_players = [
            Player(name="Charlie", uid='03', score=15),
            Player(name="Alice", uid='01', score=10),
            Player(name="Diana", uid='04', score=10),
            Player(name="Bob", uid='02', score=5),
        ]

        self.assertListEqual(sorted_players, manually_sorted_players)

    def test_sort_quickly_desc_with_many_players(self):
        players = [Player(name=f"Player{i}", uid=f"{i:03}", score=random.randint(0, 1000)) for i in range(1000)]
        sorted_players = Player.sort_quickly_desc(players)
        manually_sorted_players = sorted(players, reverse=True)
        self.assertListEqual(sorted_players, manually_sorted_players)

if __name__ == "__main__":
    unittest.main()
