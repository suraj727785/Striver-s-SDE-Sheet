# question: https://leetcode.com/problems/middle-of-the-linked-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def middleNode(head):
    temp1=head
    count=0
    while(temp1!=None):
        temp1=temp1.next
        count+=1
    count//=2
    for i in range(count):
        head=head.next
    return head
a=[1,2,3,4,5]
head=ListNode(1)
temp1=head
for i in range(1,len(a)):
    temp2=ListNode(a[i])
    temp1.next=temp2
    temp1=temp1.next
print(middleNode(head).val)