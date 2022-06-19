# question: https://leetcode.com/problems/rotate-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def rotateRight(head,k):
    temp=head
    li=[]
    if head==None or head.next==None:
        return head
    while(temp!=None):
        li.append(temp.val)
        temp=temp.next
    k=k%len(li)
    while(k>0):
        li.insert(0,li.pop(-1))
        k-=1
    temp=ListNode()
    res=temp
    for x in li:
        r=ListNode(x)
        temp.next=r
        temp=temp.next
    return res.next
    
a=[2,4,1,3,5,6]
head=ListNode(a[0])
temp1=head
for i in range(1,len(a)):
    temp2=ListNode(a[i])
    temp1.next=temp2
    temp1=temp1.next
head=rotateRight(head,4)
while(head!=None):
    print(head.val)
    head=head.next
