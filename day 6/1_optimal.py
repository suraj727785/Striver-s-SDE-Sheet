# question: https://leetcode.com/problems/intersection-of-two-linked-lists/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def getIntersectionNode(headA,headB):
    temp1,temp2=headA,headB
    c1,c2=0,0
    while(temp1!=None):
        temp1=temp1.next
        c1+=1
    while(temp2!=None):
        temp2=temp2.next
        c2+=1
    temp1,temp2=headA,headB
    if c1>c2:
        while(c1!=c2):
            temp1=temp1.next
            c1-=1
    else:
        while(c1!=c2):
            temp2=temp2.next
            c2-=1
    while(temp1!=None and temp2!=None):
        if temp1==temp2 and temp1!=None:
            return temp1
        temp1=temp1.next
        temp2=temp2.next
    return None
    

a=[4,1,8]
b=[5,6,1,8,4,5]
list1=ListNode(a[0])
temp1=list1
for i in range(1,len(a)):
    temp2=ListNode(a[i])
    temp1.next=temp2
    temp1=temp1.next
r=temp1
list2=ListNode(b[0])
temp1=list2
intersect=8
intersect_node=None
for i in range(1,len(b)):
    temp2=ListNode(b[i])
    temp1.next=temp2
    temp1=temp1.next
    if b[i]==intersect:
        intersect_node=temp2
r.next=intersect_node

list1=getIntersectionNode(list1,list2)
if list1!=None:
    print(list1.val)
else:
    print("No intersection found")