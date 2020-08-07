def tetromino1(x_sp,y_sp): #2x2 정사각형
    if x_sp + 1>= N or y_sp + 1>= M:
        return False
    return arr[x_sp][y_sp]+arr[x_sp+1][y_sp]+arr[x_sp][y_sp+1]+arr[x_sp+1][y_sp+1]

def tetromino2(x_sp,y_sp): #1x4 직사각형 가로
    if x_sp + 1>= N or x_sp + 2>= N or x_sp + 3>= N:
        return False
    return arr[x_sp][y_sp]+arr[x_sp+1][y_sp]+arr[x_sp+2][y_sp]+arr[x_sp+3][y_sp]

def tetromino3(x_sp,y_sp): #1x4 직사각형 세로
    if y_sp + 1>= M or y_sp + 2>= M or y_sp + 3>= M:
        return False
    return arr[x_sp][y_sp]+arr[x_sp][y_sp+1]+arr[x_sp][y_sp+2]+arr[x_sp][y_sp+3]

def tetromino4(x_sp,y_sp): # L직사각형 1
    if y_sp + 1>= M or y_sp + 2>= M or x_sp + 1>= N:
        return False
    return arr[x_sp][y_sp]+arr[x_sp][y_sp+1]+arr[x_sp][y_sp+2]+arr[x_sp+1][y_sp+2]

def tetromino5(x_sp,y_sp): # L직사각형 1
    if y_sp + 1>= M or y_sp + 2>= M or x_sp - 1 < 0:
        return False
    return arr[x_sp][y_sp]+arr[x_sp][y_sp+1]+arr[x_sp][y_sp+2]+arr[x_sp-1][y_sp+2]

def tetromino6(x_sp,y_sp): # L직사각형 2
    if x_sp + 1>= N or x_sp + 2>= N or y_sp + 1>= M:
        return False
    return arr[x_sp][y_sp]+arr[x_sp+1][y_sp]+arr[x_sp+2][y_sp]+arr[x_sp+2][y_sp+1]

def tetromino7(x_sp,y_sp): # L직사각형 2
    if x_sp + 1 >= N or x_sp + 2 >= N or y_sp - 1 < 0:
        return False
    return arr[x_sp][y_sp]+arr[x_sp+1][y_sp]+arr[x_sp+2][y_sp]+arr[x_sp+2][y_sp-1]

def tetromino8(x_sp,y_sp): # L직사각형 1
    if y_sp - 1 < 0 or y_sp - 2 < 0 or x_sp + 1>= N:
        return False
    return arr[x_sp][y_sp]+arr[x_sp][y_sp-1]+arr[x_sp][y_sp-2]+arr[x_sp+1][y_sp-2]

def tetromino9(x_sp,y_sp): # L직사각형 1
    if y_sp - 1 < 0 or y_sp - 2 < 0 or x_sp -1 < 0:
        return False
    return arr[x_sp][y_sp] + arr[x_sp][y_sp - 1] + arr[x_sp][y_sp - 2] + arr[x_sp - 1][y_sp - 2]

def tetromino10(x_sp,y_sp): # L직사각형 2
    if x_sp - 1 < 0 or x_sp - 2 < 0 or y_sp + 1>= M:
        return False
    return arr[x_sp][y_sp]+arr[x_sp-1][y_sp]+arr[x_sp-2][y_sp]+arr[x_sp-2][y_sp+1]

def tetromino11(x_sp,y_sp): # L직사각형 2
    if x_sp - 1 < 0 or x_sp - 2 < 0 or y_sp - 1 < M:
        return False
    return arr[x_sp][y_sp]+arr[x_sp-1][y_sp]+arr[x_sp-2][y_sp]+arr[x_sp-2][y_sp-1]


N, M = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(N)]
mx= 0
for i in range(N):
    for j in range(M):
        if tetromino1(i, j) > mx:
            mx = tetromino1(i, j)
        if tetromino2(i, j) > mx:
            mx = tetromino2(i, j)
        if tetromino3(i, j) > mx:
            mx = tetromino3(i, j)
        if tetromino4(i, j) > mx:
            mx = tetromino4(i, j)
        if tetromino5(i, j) > mx:
            mx = tetromino5(i, j)
        if tetromino6(i, j) > mx:
            mx = tetromino6(i, j)
        if tetromino7(i, j) > mx:
            mx = tetromino7(i, j)
        if tetromino8(i, j) > mx:
            mx = tetromino8(i, j)
        if tetromino9(i, j) > mx:
            mx = tetromino9(i, j)
        if tetromino10(i, j) > mx:
            mx = tetromino10(i, j)
        if tetromino10(i, j) > mx:
            mx = tetromino11(i, j)
