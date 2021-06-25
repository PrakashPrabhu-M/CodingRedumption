from crio.ds.List import ListNode

"""
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

Use ListNode.ListNode(data) to create new node
"""


def linkedListSplit(head):
	even=ListNode.ListNode(2)
	odd=ListNode.ListNode(1)
	p1=odd
	p2=even
	while head:
		if head.val%2==0:
			even.next=head
			even=even.next
		else:
			odd.next=head
			odd=odd.next
		head=head.next
	odd.next=None
	even.next=None
	return p1.next,p2.next
