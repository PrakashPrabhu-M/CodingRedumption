global res
res=[]
def binaryTreeBoundaryTraversal(root):
	if (root):
		res.append(root.val)
		BoundaryLeft(root.left)
		Leaves(root.left)
		Leaves(root.right)
		BoundaryRight(root.right)
	return res

def BoundaryLeft(root):
    if(root):
        if (root.left):
            res.append(root.val)
            BoundaryLeft(root.left)
        elif(root.right):
            res.append(root.val)
            BoundaryLeft(root.right)

def Leaves(root):
    if(root):
        Leaves(root.left)
        if root.left is None and root.right is None:
            res.append(root.val)
        Leaves(root.right)

def BoundaryRight(root):
    if(root):
        if (root.right):
            BoundaryRight(root.right)
            res.append(root.val) 
        elif(root.left):
            BoundaryRight(root.left)
            res.append(root.val)