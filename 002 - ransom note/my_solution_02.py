class RansomNote:
	def can_spell(self, magazine, note) -> bool:
		if type(magazine) == list:
			magazine = ''.join(magazine)

		for c in note:
			if c in magazine:
				magazine = magazine.replace(c, '', 1)

			else:
				return False

		return True


if __name__ == '__main__':
	magazine = ['a', 'b', 'c', 'd', 'e', 'f']
	word_1 = 'bed'  # Can Spell
	word_2 = 'cat'  # can't spell

	print('word 1 = ', RansomNote().can_spell(magazine, word_1))
	print('word 2 = ', RansomNote().can_spell(magazine, word_2))
