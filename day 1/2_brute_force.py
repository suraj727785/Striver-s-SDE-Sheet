from math import factorial
def pascal(numRows):
        if numRows==0:
            pt=[]
        if numRows==1:
            pt=[[1]]
        if numRows>1:
            pt=[[1],[1,1]]
        for i in range(2,numRows):
            k=[1]
            for j in range(len(pt[i-1])-1):
                k.append(pt[i-1][j]+pt[i-1][j+1])
            k.append(1)
            pt.append(k)
        return pt
def print_rc_element(r,c):
    # print element from the given row and column from pascal tree
    return factorial(r) / factorial(c)* factorial(r-c)
def print_nth_row(n):
    li=[1]
    if n==1:
        return li
    k=1
    for i in range(n-2):
        k*=(n-i-1)
        k//=(i+1)
        li.append(k)
    li.append(1)
    return li
print(print_nth_row(10))
print(pascal(10))