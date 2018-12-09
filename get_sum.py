def get_sum(num_one, num_two):
    try:
        return int(num_one) + int(num_two)
    except ValueError:
        return 'умею складывать только числа'


if __name__ == '__main__':
    assert get_sum('5', 10) == 15
    assert get_sum(2.6, 1) == 3
    assert get_sum('2.6', 1) == 'умею складывать только числа'
    assert get_sum('пять', 3) == 'умею складывать только числа'
