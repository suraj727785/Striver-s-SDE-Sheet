# question: https://leetcode.com/problems/linked-list-cycle/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def hasCycle(head):
    li=[]
    while(head!=None):
        if head not in li:
            li.append(head)
        else:
            return True
        head=head.next
    return False
    

a=[4,1,8,6,5]
list1=ListNode(a[0])
temp1=list1
for i in range(1,len(a)):
    temp2=ListNode(a[i])
    temp1.next=temp2
    temp1=temp1.next
cycleAt=8
end=temp1
temp1=list1
while(temp1.val!=cycleAt):
    temp1=temp1.next
end.next=temp1
print(hasCycle(list1))