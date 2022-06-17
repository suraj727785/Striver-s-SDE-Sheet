# question: https://leetcode.com/problems/add-two-numbers/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def addTwoNumbers(l1,l2):
    l3=ListNode()
    s=0
    if l1.val+l2.val<10:
        l3.val=l1.val+l2.val
    else:
        l3.val=l1.val+l2.val-10
        s=1
    res=l3
    l1,l2=l1.next,l2.next
    while(l1!=None and l2!=None):
        if l1.val+l2.val+s<10:
            k=ListNode(l1.val+l2.val+s)
            s=0
        else:
            k=ListNode(l1.val+l2.val+s-10)
            s=1
        l3.next=k
        l3=k
        l1,l2=l1.next,l2.next
    while(l1!=None):
        l1.val=l1.val+s
        s=0
        if l1.val>9:
            l1.val-=10
            s=1
        l3.next=l1
        l3=l1
        l1=l1.next
    while(l2!=None):
        l2.val=l2.val+s
        s=0
        if l2.val>9:
            l2.val-=10
            s=1
        l3.next=l2
        l3=l2
        l2=l2.next
    if s==1:
        k=ListNode(1)
        l3.next=k
    return res
    

a=[9,9,9,9,9,9,9]
b=[9,9,9,9]
list1=ListNode(a[0])
temp1=list1
for i in range(1,len(a)):
    temp2=ListNode(a[i])
    temp1.next=temp2
    temp1=temp1.next
list2=ListNode(b[0])
temp1=list2
for i in range(1,len(b)):
    temp2=ListNode(b[i])
    temp1.next=temp2
    temp1=temp1.next

list1=addTwoNumbers(list1,list2)
while(list1!=None):
    print(list1.val)
    list1=list1.next