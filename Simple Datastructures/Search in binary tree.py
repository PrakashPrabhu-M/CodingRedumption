'''
# Definition of TreeNode
class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

Use TreeNode.TreeNode(data) to create new Node
'''


# Implement Your Solution Here
def binaryTreeSearching(root,k):
	s=[]
	l=[]
	s.append(root)
	root=root.left
	while 1:
		while root:
			s.append(root)
			root=root.left
		if len(s)!=0:
			e=s.pop()
			if e.val==k: return True
			root=e.right
		else: break
	return False