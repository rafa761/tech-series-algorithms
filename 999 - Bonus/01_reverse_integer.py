# Given an Integer, return the integer with reversed digits
# Note: The Integer could be either positive or negative


def reversed_solution(number):
	string_number = str(number)

	if string_number[0] == '-':
		return int('-' + string_number[:0:-1])

	return int(string_number[::-1])


if __name__ == '__main__':
	print(reversed_solution(-894))
	print(reversed_solution(572))
