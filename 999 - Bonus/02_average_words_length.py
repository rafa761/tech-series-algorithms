# For a given sentence, return the average word length
# Note: Remember to remove ponctuation first

sentence1 = 'Hi all, my name is Rafael...I am originally from Brazil.'
sentence2 = 'To learn more about algorithms, we need to work very hard!'


def word_length_solution(sentence):
	for ponct in "!?',;.":
		sentence = sentence.replace(ponct, '')

	words = sentence.split()
	return round(sum(len(word) for word in words) / len(words), 2)


if __name__ == '__main__':
	print(word_length_solution(sentence1))
	print(word_length_solution(sentence2))
