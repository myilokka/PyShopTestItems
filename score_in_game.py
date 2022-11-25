from pprint import pprint
import random
import math


class ScoreGame:

    def __init__(self):
            self.TIMESTAMPS_COUNT = 50000
            self.PROBABILITY_SCORE_CHANGED = 0.0001
            self.PROBABILITY_HOME_SCORE = 0.45
            self.OFFSET_MAX_STEP = 3
            self.INITIAL_STAMP = {
                "offset": 0,
                "score": {
                    "home": 0,
                    "away": 0
                }
            }

    def generate_stamp(self, previous_value):
        score_changed = random.random() > 1 - self.PROBABILITY_SCORE_CHANGED
        home_score_change = 1 if score_changed and random.random() > 1 - \
        self.PROBABILITY_HOME_SCORE else 0
        away_score_change = 1 if score_changed and not home_score_change else 0
        offset_change = math.floor(random.random() * self.OFFSET_MAX_STEP) + 1

        return {
            "offset": previous_value["offset"] + offset_change,
            "score": {
                "home": previous_value["score"]["home"] + home_score_change,
                "away": previous_value["score"]["away"] + away_score_change
            }
        }

    def generate_game(self):
        stamps = [self.INITIAL_STAMP, ]
        current_stamp = self.INITIAL_STAMP
        for _ in range(self.TIMESTAMPS_COUNT):
            current_stamp = self.generate_stamp(current_stamp)
            stamps.append(current_stamp)

        return stamps

    def get_score(self, game_stamps, offset):
        """ Если переменная offset приходит в типе float - функция округляет ее, если в типе str - приводит к типу int. """

        offset = round(float(offset))

        if not game_stamps:
            return "the game hasn't started yet"
        if offset < 0 or offset > game_stamps[-1]['offset']:
            return f'invalid offset value'

        mid = len(game_stamps) // 2
        mid_offset = game_stamps[mid]['offset']

        if offset == mid_offset:
            return game_stamps[mid]['score']

        elif mid_offset < offset < game_stamps[mid+1]['offset'] or \
                mid_offset > offset > game_stamps[mid-1]['offset']:
            return 'there is no such offset'

        game_stamps = game_stamps[:mid] if offset < game_stamps[mid]['offset'] else game_stamps[mid:]

        return self.get_score(game_stamps, offset)

    def main(self, offset):
        return self.get_score(self.generate_game(), offset)


if __name__ == "__main__":
    offset = 65384
    first_game = ScoreGame()
    pprint(first_game.main(offset))
