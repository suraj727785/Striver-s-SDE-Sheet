# question: https://leetcode.com/problems/copy-list-with-random-pointer/

class ListNode:
    def __init__(self, val=0, next=None,random=None):
        self.val = val
        self.next = next
        self.random = random
def copyRandomList(head):
    temp=head
    while(temp!=None):
        new=ListNode(temp.val)
        new.next=temp.next
        temp.next=new
        temp=temp.next.next
    temp=head
    while(temp!=None):
        if temp.random==None:
            temp.next.random=None
        else:
            temp.next.random=temp.random
        temp=temp.next.next
    dmmy=ListNode()
    curr=dmmy
    temp,nex=head,head.next.next
    curr.next=temp.next
    curr=curr.next
    while(nex!=None and nex.next!=None):
        temp.next=nex
        temp=temp.next
        nex=nex.next.next
        curr.next=temp.next
        curr=curr.next
    return dmmy.next
    
a=[7,13,11,10,1]
random=[None,0,4,2,0]
head=ListNode(a[0])
temp1=head
for i in range(1,len(a)):
    temp2=ListNode(a[i])
    temp1.next=temp2
    temp1=temp1.next
temp1=head
for i in range(len(a)):
    temp2=head
    c=0
    if random[i]==None:
        temp1.random=None
    else:
        while(c!=random[i]):
            c+=1
            temp2=temp2.next
        temp1.random=temp2
    temp1=temp1.next


head=copyRandomList(head)
while(head!=None):
    if head.random==None:
        k=None
    else:
        k=head.random.val
    print(head.val,k)
    head=head.next
