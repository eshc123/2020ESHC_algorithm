N, M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort()
B.sort()
a_index = 0
b_index = 0
while a_index < len(A) and b_index < len(B):
    if A[a_index] > B[b_index]:
        print(B[b_index],end=" ")
        b_index+=1
    else:
        print(A[a_index],end=" ")
        a_index+=1
if a_index==len(A):
    for i in B[b_index:]:
        print(i,end=" ")
else:
    for i in A[a_index:]:
        print(i,end=" ")
