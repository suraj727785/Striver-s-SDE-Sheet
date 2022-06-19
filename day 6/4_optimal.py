# question: https://leetcode.com/problems/palindrome-linked-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def isPalindrome(head):
    if head==None or head.next==None:
        return True
    s,f=head,head
    while(f.next!=None and f.next.next!=None):
        s=s.next
        f=f.next.next
    s=s.next
    temp1=None
    while(s!=None):
        temp2=s.next
        s.next=temp1
        temp1,s=s,temp2
    while(temp1!=None):
        if head.val!=temp1.val:
            return False
        head=head.next
        temp1=temp1.next
    return True

a=[1,2,2,1]
head=ListNode(a[0])
temp1=head
for i in range(1,len(a)):
    temp2=ListNode(a[i])
    temp1.next=temp2
    temp1=temp1.next
print(isPalindrome(head))