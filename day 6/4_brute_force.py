# question: https://leetcode.com/problems/palindrome-linked-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def isPalindrome(head):
    temp=head
    li=[]
    while(temp!=None):
        li.append(temp.val)
        temp=temp.next
    li=li[::-1]
    temp=head
    for i in range(len(li)//2):
        if temp.val!=li[i]:
            return False
        temp=temp.next
    return True
a=[1,2,2,1]
head=ListNode(a[0])
temp1=head
for i in range(1,len(a)):
    temp2=ListNode(a[i])
    temp1.next=temp2
    temp1=temp1.next
print(isPalindrome(head))