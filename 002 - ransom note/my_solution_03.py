class RansomNote:
	def can_spell(self, magazine, note):
		if any(letter not in magazine for letter in note):
			return False

		for letter in set(note):
			if magazine.count(letter) < note.count(letter):
				return False
		return True


if __name__ == '__main__':
	magazine = ['a', 'b', 'c', 'd', 'e', 'f']
	word_1 = 'bed'  # Can Spell
	word_2 = 'cat'  # can't spell

	print('word 1 = ', RansomNote().can_spell(magazine, word_1))
	print('word 2 = ', RansomNote().can_spell(magazine, word_2))
