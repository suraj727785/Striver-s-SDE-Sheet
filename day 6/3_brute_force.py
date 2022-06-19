# question: https://leetcode.com/problems/reverse-nodes-in-k-group/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reverseKGroup(head,k):
    if head==None or k==1:
        return head
    dummy=ListNode()
    dummy.next=head
    cur,nex,pre=dummy,dummy,dummy
    count=0
    while(cur.next!=None):
        count+=1
        cur=cur.next
    while(count>=k):
        cur=pre.next
        nex=cur.next
        for i in range(1,k):
            cur.next=nex.next
            nex.next=pre.next
            pre.next=nex
            nex=cur.next
        pre=cur
        count-=k
    return dummy.next
a=[1,2,3,4,5]
head=ListNode(a[0])
temp1=head
for i in range(1,len(a)):
    temp2=ListNode(a[i])
    temp1.next=temp2
    temp1=temp1.next
head=reverseKGroup(head,2)
while(head!=None):
    print(head.val)
    head=head.next