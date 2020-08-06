from collections import defaultdict


class Solution(object):
	def canSpell(self, magazine, note):
		letters = defaultdict()
		for c in magazine:
			letters[c] += 1

		for c in note:
			if letters[c] <= 0:
				return False
			letters[c] -= 1

		return True


print(Solution().canSpell(['a', 'b', 'c', 'd', 'e'], 'bed'))  # True
print(Solution().canSpell(['a', 'b', 'c', 'd', 'e'], 'cat'))  # False
