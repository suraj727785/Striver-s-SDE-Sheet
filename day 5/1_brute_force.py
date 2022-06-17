# question: https://leetcode.com/problems/reverse-linked-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reverseList(head):
    if head==None or head.next==None:
        return head
    temp2=head.next
    temp3=head.next.next
    temp1=head
    head.next=None
    while(temp2!=None):
        temp2.next=temp1
        temp1,temp2=temp2,temp3
        if temp3!=None:
            temp3=temp3.next
    return temp1
a=[1,2,3,4,5]
head=ListNode(1)
temp1=head
for i in range(1,len(a)):
    temp2=ListNode(a[i])
    temp1.next=temp2
    temp1=temp1.next
head=reverseList(head)
while(head!=None):
    print(head.val)
    head=head.next