import sys

def div_con(a):
    if len(set([element for array in a for element in array]))==1:
        numbers[a[0][0]+1]+=1
        return
    if len(a)==1:
        numbers[a[0][0]+1]+=1
        return
    length = len(a)//3
    div_con([row[:length] for row in a[:length]])
    div_con([row[:length] for row in a[length:2*length]])
    div_con([row[:length] for row in a[2 * length:]])
    div_con([row[length:2*length] for row in a[length:2*length]])
    div_con([row[length:2*length] for row in a[:length]])
    div_con([row[length:2*length] for row in a[2 * length:]])
    div_con([row[2 * length:] for row in a[2 * length:]])
    div_con([row[2 * length:] for row in a[:length]])
    div_con([row[2 * length:] for row in a[length:2*length]])


N = int(sys.stdin.readline())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
numbers =[0,0,0] # -1,0,1 갯수
div_con(arr)
for number in numbers:
    print(number)