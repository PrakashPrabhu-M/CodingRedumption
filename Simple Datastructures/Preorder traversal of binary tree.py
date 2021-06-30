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
def preorderTraversal(root):
	s=[]
	l=[]
	e=root
	s.append(e)
	while 1:
		#print('Stack',s)
		#print('list',l)
		e=s.pop()
		l.append(e.val)
		if e.right:
			s.append(e.right)
			#print('right',s)
		if e.left:
			s.append(e.left)
			#print('left',s)
		if len(s)==0:break
	return l