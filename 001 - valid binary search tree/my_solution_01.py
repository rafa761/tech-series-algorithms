def print_tree_traverse(root):
	""" Just to print the tree, not used in the solution"""
	current_level = [root]
	while current_level:
		print(' '.join(str(node) for node in current_level))
		next_level = list()
		for n in current_level:
			if n.left:
				next_level.append(n.left)
			if n.right:
				next_level.append(n.right)
		current_level = next_level


class Node(object):
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

	def __gt__(self, other):
		if self.val > other.val:
			return True

	def __le__(self, other):
		if self.val < other:
			return True

	def __repr__(self):
		return str(self.val)


class ValidateTree:
	def __init__(self, tree):
		self.tree = tree

	def validate(self):
		"""
		To Validate the tree we need to traverse all branches, storing values on left and right branches
		"""
		left_branch = []
		right_branch = []
		if self.tree.left:
			left_branch = self.traverse_tree(self.tree.left)
		if self.tree.right:
			right_branch = self.traverse_tree(self.tree.right)

		if not left_branch and right_branch:
			return 'EMPTY'

		for left_value in left_branch:
			for right_value in right_branch:
				if left_value > right_value:
					return 'INVALID'

		return 'VALID'

	def traverse_tree(self, start_node):
		values_list = [start_node]
		current_level = [start_node]
		while current_level:
			next_level = []
			for node in current_level:
				if node.left:
					next_level.append(node.left)
					values_list.append(node.left)
				if node.right:
					next_level.append(node.right)
					values_list.append(node.right)
			current_level = next_level

		return values_list


if __name__ == '__main__':
	invalid_tree = Node(5)
	invalid_tree.left = Node(4)
	invalid_tree.right = Node(7)
	invalid_tree.right.left = Node(2)
	# print_tree_traverse(invalid_tree)
	validation = ValidateTree(invalid_tree).validate()
	print('invalid tree', validation)

	valid_tree = Node(5)
	valid_tree.left = Node(4)
	valid_tree.right = Node(7)
	validation = ValidateTree(valid_tree).validate()
	print('valid tree', validation)
