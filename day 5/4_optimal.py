# question: https://leetcode.com/problems/reverse-linked-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def removeNthFromEnd(head,n):
    temp1=ListNode()
    temp1.next=head
    s,f=temp1,temp1
    for _ in range(n):
        f=f.next
    while(f.next!=None):
        f=f.next
        s=s.next
    s.next=s.next.next
    return temp1.next
a=[2,4,1,3,5,6]
head=ListNode(a[0])
temp1=head
for i in range(1,len(a)):
    temp2=ListNode(a[i])
    temp1.next=temp2
    temp1=temp1.next
head=removeNthFromEnd(head,4)
while(head!=None):
    print(head.val)
    head=head.next