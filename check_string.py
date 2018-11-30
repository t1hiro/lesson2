
def check_str(string_1, string_2):
	if not isinstance(string_1, str) or not isinstance(string_2, str):
		return 0
	if string_1 == string_2:
		return 1
	else:
		if len(string_1) > len(string_2):
			return 2
		elif string_2 == 'learn':
			return 3
		return None


assert check_str(123, '123') == 0
assert check_str('123', None) == 0
assert check_str('123', '123') == 1
assert check_str('1234', '123') == 2
assert check_str('123', 'learn') == 3
assert check_str('12345', 'learn') == 3
assert check_str('123456', 'learn') == 2
assert check_str('12345', '123456') is None
