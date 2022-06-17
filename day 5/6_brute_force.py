# question: https://leetcode.com/problems/delete-node-in-a-linked-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def deleteNode(node):
    node.val=node.next.val
    node.next=node.next.next
    
a=[1,2,3,4,5]
head=ListNode(1)
temp1=head
for i in range(1,len(a)):
    temp2=ListNode(a[i])
    temp1.next=temp2
    temp1=temp1.next
nodetobedeleted=3
temp1=head
while(temp1.val!=nodetobedeleted):
    temp1=temp1.next
deleteNode(temp1)
while(head!=None):
    print(head.val)
    head=head.next