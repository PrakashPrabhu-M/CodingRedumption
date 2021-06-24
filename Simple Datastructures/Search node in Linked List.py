from crio.ds.List import ListNode

"""
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

Use ListNode.ListNode(data) to create new node
"""


def linkedListSearch(head, x):
	p=head
	while p is not None:
		if p.val==x:
			return True
		p=p.next
	return False