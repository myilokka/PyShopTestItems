fixture_get_score = [([{'offset': 0, 'score': {'away': 0, 'home': 0}},
                       {'offset': 1, 'score': {'away': 1, 'home': 0}},
                       {'offset': 3, 'score': {'away': 1, 'home': 1}},
                       {'offset': 5, 'score': {'away': 1, 'home': 2}}],
                      0,  {'away': 0, 'home': 0}),

                     ([{'offset': 0, 'score': {'away': 0, 'home': 0}},
                       {'offset': 1, 'score': {'away': 1, 'home': 0}},
                       {'offset': 3, 'score': {'away': 1, 'home': 1}},
                       {'offset': 5, 'score': {'away': 1, 'home': 2}}],
                      1,  {'away': 1, 'home': 0}),

                     ([{'offset': 0, 'score': {'away': 0, 'home': 0}},
                       {'offset': 1, 'score': {'away': 1, 'home': 0}},
                       {'offset': 3, 'score': {'away': 1, 'home': 1}},
                       {'offset': 5, 'score': {'away': 1, 'home': 2}}],
                      5,  {'away': 1, 'home': 2}),

                     ([{'offset': 0, 'score': {'away': 0, 'home': 0}},
                       {'offset': 1, 'score': {'away': 1, 'home': 0}},
                       {'offset': 3, 'score': {'away': 1, 'home': 1}},
                       {'offset': 5, 'score': {'away': 1, 'home': 2}}],
                      '5',  {'away': 1, 'home': 2}),

                     ([{'offset': 0, 'score': {'away': 0, 'home': 0}},
                       {'offset': 1, 'score': {'away': 1, 'home': 0}},
                       {'offset': 3, 'score': {'away': 1, 'home': 1}},
                       {'offset': 5, 'score': {'away': 1, 'home': 2}}],
                      '4', 'there is no such offset'),

                     ([], 0, "the game hasn't started yet"),

                     ([{'offset': 0, 'score': {'away': 0, 'home': 0}}],
                       -5, 'invalid offset value'),

                     ([{'offset': 0, 'score': {'away': 0, 'home': 0}}],
                      '-5', 'invalid offset value'),

                     ([{'offset': 0, 'score': {'away': 0, 'home': 0}},
                       {'offset': 1, 'score': {'away': 1, 'home': 0}},
                       {'offset': 3, 'score': {'away': 1, 'home': 1}},
                       {'offset': 5, 'score': {'away': 1, 'home': 2}}],
                      '6', 'invalid offset value'),

                     ([{'offset': 0, 'score': {'away': 0, 'home': 0}},
                       {'offset': 1, 'score': {'away': 1, 'home': 0}},
                       {'offset': 3, 'score': {'away': 1, 'home': 1}},
                       {'offset': 5, 'score': {'away': 1, 'home': 2}}],
                      7, 'invalid offset value'),

                     (None, 5, "the game hasn't started yet"),]


fixture_get_score_with_failure = [([{'offset': 0, 'score': {'away': 0, 'home': 0}},
                                    {'offset': 1, 'score': {'away': 1, 'home': 0}}],
                                   None)]



