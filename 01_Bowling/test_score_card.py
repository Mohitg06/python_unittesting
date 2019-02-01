import unittest
from score_card import Game

class TestScoreCard(unittest.TestCase):


    def test_a_new_game_has_a_score_of_zero(self):
        game = Game()
        self.assertEqual(0, game.get_score())

    def test_throw_a_1_and_throw_a_2_score_is_3(self):
        # Arrange: Create a game
        game = Game()

        # Act:
        #   Throw a 1
        game.throw(1)
        #   Throw a 2
        game.throw(2)

        # Assert: Verify that the game score is equal to 3
        self.assertEqual(3, game.get_score())

    def test_throw_3_and_a_1_score_is_4(self):
        game = Game()

        game.throw(3)
        game.throw(1)

        self.assertEqual(4, game.get_score())

    def test_throw_3_and_score_is_0(self):
        game = Game()
        game.throw (3)

        self.assertEqual(0, game.get_score())

    def test_group_and_one_attempt(self):
        game = Game()
        game.throw(3)
        game.throw(2)
        game.throw(1)

        self.assertEqual(5,game.get_score())





if __name__ == '__main__':
    unittest.main()
