class RansomNote:
	def can_spell(self, magazine, note):
		return not any(note.count(c) > magazine.count(c) for c in set(note))


if __name__ == '__main__':
	magazine = ['a', 'b', 'c', 'd', 'e', 'f']
	word_1 = 'bed'  # Can Spell
	word_2 = 'cat'  # can't spell

	print('word 1 = ', RansomNote().can_spell(magazine, word_1))
	print('word 2 = ', RansomNote().can_spell(magazine, word_2))
