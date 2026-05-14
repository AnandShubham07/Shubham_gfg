'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def deleteNode(self, head, x):
        count=1
        curr=head
        if not head:
            return None
        if(x==1):
            head=head.next
            return head
            
        while curr:
            count+=1
            if(count==x):
                curr.next=curr.next.next
                return head
            curr=curr.next
            
        
