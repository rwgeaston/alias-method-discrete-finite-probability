from unittest import TestCase
from collections import Counter

from next_num import RandomGen


class NextNumTests(TestCase):
    def test_typical_usage(self):
        distribution = {
            1: 0.5,
            2: 0.25,
            "three": 0.25,  # No reason why all the keys have to be numbers
        }
        random_gen = RandomGen(distribution)

        # Make the output completely predictable for unit test. Don't do this in normal usage!
        random_gen.random_source.seed(1)

        outputs = Counter()

        for _ in range(100000):
            outputs[random_gen.next_num()] += 1

        self.assertEqual(
            outputs,
            {
                1: 49615,
                2: 25112,
                "three": 25273,
            },
        )

    def test_more_outcomes(self):
        distribution = {
            1: 0.1,
            2: 0.2,
            3: 0.3,
            4: 0.1,
            5: 0.2,
            6: 0.06,
            7: 0.04,
        }
        random_gen = RandomGen(distribution)

        # Make the output completely predictable for unit test. Don't do this in normal usage!
        random_gen.random_source.seed(2)

        outputs = Counter()

        for _ in range(100000):
            outputs[random_gen.next_num()] += 1

        self.assertEqual(
            outputs,
            {
                1: 9926,
                2: 20049,
                3: 29779,
                4: 10023,
                5: 20233,
                6: 5956,
                7: 4034
            },
        )
