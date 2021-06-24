from crio.ds.List import ListNode

"""
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

Use ListNode.ListNode(data) to create new node
"""
class Solution:
    def __init__(self):
        self.head = None

    def linkedListRemove(self, x):
        p=self.head
        while p is not None:
            if p.val==x:
                p.val=p.next.val
                p.next=p.next.next
                break
            p=p.next
                
