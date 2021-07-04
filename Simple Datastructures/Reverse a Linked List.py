from crio.ds.List import ListNode

"""
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

Use ListNode.ListNode(data) to create new node
"""


def linkedListReverse(head):
	prev=None
	present=head
	nxt=present.next
	while present is not None:
		nxt=present.next
		present.next=prev
		prev=present
		present=nxt
		head=prev
		#print(f'Prev: {prev.val} present: {present.val} next: {nxt.val}')
	return head
