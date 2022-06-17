# question: https://leetcode.com/problems/merge-two-sorted-lists/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def mergeTwoLists(list1,list2):
    if list1==None:
        return list2
    if list2==None:
        return list1
    temp=None
    if list1.val<list2.val:
        temp=list1
        list1=list1.next
    else:
        temp=list2
        list2=list2.next
    res=temp
    while(list1!=None and list2!=None):
        if list1.val<list2.val:
            temp.next=list1
            temp=list1
            list1=list1.next
        else:
            temp.next=list2
            temp=list2
            list2=list2.next
    while(list1!=None):
        temp.next=list1
        temp=list1
        list1=list1.next
    while(list2!=None):
        temp.next=list2
        temp=list2
        list2=list2.next
    return res
        
a=[1,2,4]
b=[1,3,4]
list1=ListNode(1)
temp1=list1
for i in range(1,len(a)):
    temp2=ListNode(a[i])
    temp1.next=temp2
    temp1=temp1.next
list2=ListNode(1)
temp1=list2
for i in range(1,len(b)):
    temp2=ListNode(b[i])
    temp1.next=temp2
    temp1=temp1.next

list1=mergeTwoLists(list1,list2)
while(list1!=None):
    print(list1.val)
    list1=list1.next