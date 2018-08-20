# https://en.wikipedia.org/wiki/Alias_method
import random
from math import floor
from numbers import Real


class InvalidInputs(Exception):
    pass


class RandomGen:
    _distribution = None

    def __init__(self, distribution, random_source=None):
        if not distribution:
            raise InvalidInputs("Don't give an empty distribution because weird things will happen")

        if not all(
                isinstance(probability, Real) and (probability >= 0)
                for probability in distribution.values()
        ):
            raise InvalidInputs("Probabilities must be non-negative numbers")

        # Technically if the probabilities don't add exactly to 1, it's a measure not a probability distribution.
        # However the rest of the code works perfectly fine in either scenario.
        # Let's just normalise them.
        total_measure = sum(distribution.values())
        if not total_measure:
            raise InvalidInputs("Your measure/probability distribution cannot add to 0!")

        for key in distribution:
            distribution[key] /= total_measure

        self.n = n = len(distribution)
        self._distribution = [
            {
                'u': n * probability,  # u is used probability, also terminology used on wikipedia
                'k': None,
                'value': value,
            } for value, probability in distribution.items()
        ]

        for _ in range(n):  # we will be done before this many redistributions

            # Doing this every time is wasteful but we only do it in the init
            self._distribution.sort(key=lambda u: u['u'])

            underfull = self.get_underfull()
            if not underfull:
                break

            overfull = self._distribution[-1]  # easy because we sorted

            underfull['k'] = overfull['value']
            overfull['u'] = overfull['u'] + underfull['u'] - 1
        else:
            # If this happens my code logic is wrong so abandon ship
            raise Exception("I deliberately put too many iterations in the for loop so this will never happen.")

        self.random_source = random_source or random.Random()

    def get_underfull(self):
        for entry in self._distribution:
            # Floating point errors means sometimes the exactly full entries are actually 0.99999999 not 1
            if entry['u'] < 0.999999999999 and not entry['k']:
                return entry

        # Didn't find one so we should be good to stop
        return None

    def next_num(self):
        random_key = self.n * self.random_source.random()
        i = floor(random_key)
        y = random_key - i
        random_value = self._distribution[i]
        if y < random_value['u']:
            return random_value['value']

        return random_value['k']
