def my_zip(*iterables):
    min_length = min(len(iterable) for iterable in iterables)
    for i in range(min_length):
        yield tuple(iterable[i] for iterable in iterables)


names = ['Denys', 'Sasha', 'Ya']
ages = [1337, 228, 777]
countries = ['Ukraine', 'Pomoyka', 'Canada']

zipped = my_zip(names, ages, countries)

for item in zipped:
    print(item)