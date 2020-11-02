def checkcheck(s):
    m,j=0,0
    for i in s:
        if i in ["a","e","i","o","u"]:
            m+=1
        else :
            j+=1
    if m>=1 and j>=2:
        return True
    else :
        return False

def go(str,goal,index):
    if len(str) is L:
        if checkcheck(str):
            print(str)
        return
    if index >=C:
        return False

    go(str+a[index],C,index+1)
    go(str, C, index + 1)




L, C = map(int,input().split())
a = sorted(list(input().split()))
go("",C,0)
