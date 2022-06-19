# question: https://leetcode.com/problems/linked-list-cycle-ii/

from multiprocessing import dummy


class Node:
    def __init__(self, d=0):
        self.data=d
        self.next=None
        self.bottom=None
def mergeTwoNode(a,b):
    res=Node(0)
    temp=res
    while(a!=None and b!=None):
        if a.data<b.data:
            temp.bottom=a
            a=a.bottom
        else:
            temp.bottom=b
            b=b.bottom
        temp=temp.bottom
    if(a!=None):
        temp.bottom=a
    else:
        temp.bottom=b

    return res.bottom
        

def flatten(root):
    if root==None or root.next==None:
        return root
    root.next=flatten(root.next)
    root=mergeTwoNode(root,root.next)
    return root   

a=[5,10,19,28]
b=[[7,8,30],[20],[22,50],[35,40,45]]
list1=Node()
temp1=list1
for i in range(len(a)):
    temp2=Node(a[i])
    temp1.next=temp2
    temp1=temp1.next
    
    save=temp1
    for j in range(len(b[i])):
        temp2=Node(b[i][j])
        temp1.bottom=temp2
        temp1=temp1.bottom
    temp1=save
list1=list1.next
# while(list1!=None):
#     print(list1.data)
#     d=list1.bottom
#     while(d!=None):
#         print(d.data,sep=" ")
#         d=d.bottom
#     list1=list1.next
head=flatten(list1)
while(head!=None):
    print(head.data)
    head=head.bottom