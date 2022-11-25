import unittest
from parameterized import parameterized
from score_in_game import ScoreGame
from fixtures import fixture_get_score, fixture_get_score_with_failure


class TestScoreInGame(unittest.TestCase):

    def setUp(self) -> None:
        self.game = ScoreGame()

    @parameterized.expand(fixture_get_score)
    def test_get_score(self, game_stamps, offset, expected_result):
        result = self.game.get_score(game_stamps, offset)
        self.assertEqual(expected_result, result)

    @parameterized.expand(fixture_get_score_with_failure)
    @unittest.expectedFailure
    def test_get_score_failure_expected(self, game_stamps, offset):
        result = self.game.get_score(game_stamps, offset)
        self.assertEqual(TypeError, result)

