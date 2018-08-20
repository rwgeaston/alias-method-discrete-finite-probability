from collections import Counter

from next_num import RandomGen

distribution = {
    -1: 0.01,
    0: 0.3,
    1: 0.58,
    2: 0.1,
    3: 0.01,
}

random_gen = RandomGen(distribution)
results = Counter()

for _ in range(100):
    results[random_gen.next_num()] += 1

print(dict(results))
