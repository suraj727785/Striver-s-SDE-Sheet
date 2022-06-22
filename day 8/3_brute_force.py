# question: https://practice.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1#

class Job:
    def __init__(self,id,deadline,profit):
        self.id=id
        self.deadline=deadline
        self.profit=profit

def JobScheduling(Jobs,n):
    Jobs=sorted(Jobs,reverse=True,key=lambda x:x.profit)
    maxD=0
    for i in range(n):
        if maxD<Jobs[i].deadline:
            maxD=Jobs[i].deadline
    k=[-1]*(maxD+1)
    res=0
    c=0
    for i in range(len(Jobs)):
        if Jobs[i].deadline>maxD:
            continue
        if k[Jobs[i].deadline]==-1:
            k[Jobs[i].deadline]=Jobs[i].profit
            res+=Jobs[i].profit
            c+=1
        else:
            r=Jobs[i].deadline-1
            while(k[r]!=-1):
                r-=1
                if r==0:
                    break
            if r==0:
                continue
            k[r]=Jobs[i].profit
            res+=Jobs[i].profit
            c+=1
    return [c,res]



inputt=[[1, 2, 100], [2, 1, 19], [3, 2, 27], [4, 1, 25], [5, 1, 15]]
Jobs=[]
for i in range(len(inputt)):
    newJob=Job(inputt[i][0],inputt[i][1],inputt[i][2])
    Jobs.append(newJob)
print(JobScheduling(Jobs,len(Jobs)))
