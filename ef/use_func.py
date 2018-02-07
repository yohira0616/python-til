import collections

names = ['Socrates', 'Archimedes', 'Plato', 'Aristotle']

names.sort(key=lambda x: len(x))

print(names)


def log_missing():
    print('Key Added')
    return 0


current = {'green': 12, 'blue': 3}
increments = [('red', 5), ('blue', 17), ('orange', 9)]

result = collections.defaultdict(log_missing, current)

print('Before:', dict(result))

for key, amount in increments:
    result[key] += amount

print('After', dict(result))


class BetterCountMissing(object):

    def __init__(self):
        self.added = 0

    def __call__(self):
        self.added += 1
        return 0


counter = BetterCountMissing()
counter()

assert callable(counter)

counter = BetterCountMissing()
result = collections.defaultdict(counter, current)

for key, amount in increments:
    result[key] += amount

assert counter.added == 2
