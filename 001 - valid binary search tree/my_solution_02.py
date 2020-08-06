class Node(object):
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class ValidateTree:
	def validate(self, tree_root):
		return self.__validate_tree_helper(tree_root, float('-inf'), float('inf'))

	def __validate_tree_helper(self, node, low, high):
		# Base Case
		if not node:
			return True

		# Test Case
		if ((low < node.val < high) and
				self.__validate_tree_helper(node.left, low, node.val) and
				self.__validate_tree_helper(node.right, node.val, high)):
			return True

		return False


if __name__ == '__main__':
	valid_tree = Node(5)
	valid_tree.left = Node(4)
	valid_tree.right = Node(7)

	invalid_tree = Node(5)
	invalid_tree.left = Node(4)
	invalid_tree.right = Node(7)
	invalid_tree.right.left = Node(2)

	invalid_tree2 = Node(1)
	invalid_tree2.left = Node(1)

	print('invalid tree:', ValidateTree().validate(invalid_tree))
	print('valid tree:', ValidateTree().validate(valid_tree))
	print('invalid tree:2', ValidateTree().validate(invalid_tree2))
