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
        self.head = self.tail = None

    def insertAtEnd(self, data):
        temp=ListNode.ListNode(data)
        if self.head is None:
            self.head=temp
        else:
            p=self.head
            while p.next is not None:
                p=p.next
            p.next=temp
            temp.next=None

    def insertAtBeginning(self, data):
        temp=ListNode.ListNode(data)
        if self.head is None:
            self.head=temp
        else:
            temp.next=self.head
            self.head=temp
