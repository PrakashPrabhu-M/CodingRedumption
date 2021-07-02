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
def postorderTraversal(root):
	stack=[]
	l=[]
	current=root
	while len(stack)!=0 or current is not None:
		if current is not None:
			stack.append(current)
			current=current.left
		else:
			temp=stack[-1].right
			if temp is None:
				temp=stack.pop()
				l.append(temp.val)
				while len(stack)!=0 and stack[-1].right==temp:
					temp=stack.pop()
					l.append(temp.val)
			else:
				current=temp
	return l
