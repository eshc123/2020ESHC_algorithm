

def get_stars(n):
    matrix = [] # 반복될 패턴을 새로이 저장하기 위한 리스트
    for i in range(3 * len(n)): # star의 크기의 3배 만큼의 반복될 패턴이 새롭게 저장됨.
        if i // len(n) == 1: # 몫이 1인 인덱스인지 아닌지에 따라 저장되는 패턴이 다름
            matrix.append(n[i % len(n)] + " " * len(n) + n[i % len(n)]) #몫이 1일 때 원래의 패턴과 빈칸이 더해짐
        else:
            matrix.append(n[i % len(n)] * 3) # 원래 패턴 반복
    return matrix


star = ["***", "* *", "***"]
N = int(input())

while True:
    if N==3: # N이 3이면 그대로 출력
        break
    star = get_stars(star)
    N//=3
for i in star:
    print(i)

## https://readytoearndon.tistory.com/11 참고