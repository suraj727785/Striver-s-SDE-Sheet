# question: https://leetcode.com/problems/copy-list-with-random-pointer/

class ListNode:
    def __init__(self, val=0, next=None,random=None):
        self.val = val
        self.next = next
        self.random = random
def copyRandomList(head):
    dic = {None:None}
    temp = head       
    while temp:
        new=ListNode(temp.val)
        dic[temp]=new
        temp=temp.next
    temp=head
    while temp:
        dic[temp].next=dic[temp.next]
        dic[temp].random=dic[temp.random]
        temp = temp.next
    
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
