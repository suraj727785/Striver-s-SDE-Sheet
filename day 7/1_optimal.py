# question: https://leetcode.com/problems/rotate-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def rotateRight(head,k):
    temp=head
    if head==None or head.next==None:
        return head
    count=0
    while(temp.next!=None):
        temp=temp.next
        count+=1
    count+=1
    if k%count==0:
        return head
    k=count-k%count
    nex=head
    while(k>1):
        nex=nex.next
        k-=1
    res=nex.next
    nex.next=None
    temp.next=head
    return res
    
a=[1,2]
head=ListNode(a[0])
temp1=head
for i in range(1,len(a)):
    temp2=ListNode(a[i])
    temp1.next=temp2
    temp1=temp1.next
head=rotateRight(head,2)
while(head!=None):
    print(head.val)
    head=head.next
