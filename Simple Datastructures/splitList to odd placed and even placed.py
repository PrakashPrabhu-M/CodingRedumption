from crio.ds.List import ListNode

"""
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

Use ListNode.ListNode(data) to create new node
"""


def linkedListSplit(head):
	odd=ListNode.ListNode(None)
	even=ListNode.ListNode(None)
	p1=even
	p2=odd
	while head:
		#print(head.val)
		odd.next=ListNode.ListNode(head.val)
		if head.next is None:
			break
		head=head.next
		odd=odd.next
		even.next=ListNode.ListNode(head.val)
		if head.next is None:
			break
		head=head.next
		even=even.next
	
	return p2.next,p1.next
