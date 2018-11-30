def get_summ(num_one, num_two):
	try:
		return int(num_one) + int(num_two)
	except ValueError:
		return 'умею складывать только числа'

assert get_summ('5', 10) == 15
assert get_summ(2.6, 1) == 3
assert get_summ('2.6', 1) == 'умею складывать только числа'
assert get_summ('пять', 3) == 'умею складывать только числа'