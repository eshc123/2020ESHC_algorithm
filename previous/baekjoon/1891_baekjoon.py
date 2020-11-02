def conquer(cx,cy,idx,s):
    if idx == int(d):
        if 0<cx<=1 and 0<cy<=1 or (cx==0 and cy ==0):
            print(s)
            return
        else:
            print(-1)
            return
    if cx >= 1/(2**(idx+1)) and cy >= 1/(2**(idx+1)):
        s+='1'
        cx-=1/(2**(idx+1))
        cy-=1/(2**(idx+1))
    elif cx >= 1 / (2 ** (idx + 1)) and cy < 1 / (2 ** (idx + 1)):
        s+='4'
        cx -= 1 / (2 ** (idx + 1))
    elif cx < 1/(2**(idx+1)) and cy >= 1/(2**(idx+1)):
        s+='2'
        cy -= 1 / (2 ** (idx + 1))
    else:
        s+='3'
    conquer(cx,cy,idx+1,s)


def divide(idx,cx,cy):
    if idx == int(d):
        cx+=(x*(1/(2**(int(d)))))
        cy+=(y*(1/(2**(int(d)))))
        conquer(cx,cy,0,'')
        return

    t = 1/(2**(idx+1))
    if number[idx] == '1':
        cx+=t
        cy+=t
    elif number[idx] == '2':
        cy+=t
    elif number[idx]== '4':
        cx+=t
    divide(idx+1,cx,cy)


d, number = input().split()
x, y = map(int,input().split())
if int(d)!= len(number):
    print(-1)
else:
    divide(0,0.0,0.0)