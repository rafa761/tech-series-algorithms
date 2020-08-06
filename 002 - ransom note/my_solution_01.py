## This is the Brute force aproach
class Note(object):
	def can_spell(self, magazine, word):
		for w in word:
			if not w in magazine:
				return False

		return True


if __name__ == '__main__':
	magazine = ['A', 'B', 'C', 'D', 'E', 'F']
	word_1 = 'BED'  # Can Spell
	word_2 = 'CAT'  # can't spell

	print('word 1 = ', Note().can_spell(magazine, word_1))
	print('word 2 = ', Note().can_spell(magazine, word_2))
