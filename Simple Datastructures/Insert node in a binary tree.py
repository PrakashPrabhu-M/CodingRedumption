from crio.ds.Tree import TreeNode
"""
class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

Use TreeNode.TreeNode(data) to create new Node
"""


def binaryTreeInsertion(root):
	current=root
	s=[]
	while 1:
		while current is not None:
			s.append(current)
			if current.left is None and current.right is None:
				break
			elif current.left is not None and current.right is None:
				current.right=TreeNode.TreeNode(0)
			elif current.right is not None and current.left is None:
				current.left=TreeNode.TreeNode(0)
			current=current.left
			
		if len(s)!=0:
			current=s.pop()
			current=current.right
		else:
			break

	return root