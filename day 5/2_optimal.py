# question: https://leetcode.com/problems/middle-of-the-linked-list/
# tortiose method

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def middleNode(head):
    f=head
    while f!=None and f.next!=None:
        head=head.next
        f=f.next.next
    return head
a=[1,2,3,4,5]
head=ListNode(1)
temp1=head
for i in range(1,len(a)):
    temp2=ListNode(a[i])
    temp1.next=temp2
    temp1=temp1.next
print(middleNode(head).val)