# question: https://leetcode.com/problems/reverse-linked-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def removeNthFromEnd(head,n):
    temp1=head
    count=0
    while(temp1!=None):
        temp1=temp1.next
        count+=1
    count=count-n-1
    temp1=head
    for i in range(count):
        temp1=temp1.next
    if temp1.next==None:
        return None
    if count==-1:
        return head.next
    temp1.next=temp1.next.next   
    return head
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