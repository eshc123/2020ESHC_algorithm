import sys


def div_con(number):
    l=0 # 리스트의 가장 왼쪽 인덱스를 l로
    r= N-1 # 리스트의 가장 오른쪽 인덱스를 r로 /// N-1
    while l<=r: # 반복문을 실행하다가 가장 왼쪽 인덱스가 오른쪽보다 작거나 같을 때까지만 반복문 실행
        m = (l+r)//2 # 가장 중간 인덱스 설정
        if number == cards[m]: # 중앙값이 찾으려는 값과 같으면 디셔너리의 갯수값을 반환
            return dic_cards[number]
        elif cards[m] > number: # 중앙값이 찾으려는 값보다 크면
            r = m - 1 # 오른쪽 인덱스를 중간 인덱스보다 1만큼 작게 설정하여 반으로 나눔
        else: # 중앙값이 찾으려는 값보다 작으면
            l = m + 1 # 왼쪽 인덱스를 중간 인덱스보다 1만큼 크게 설정하여 반으로 나눔
    return 0


N = int(input())
cards = list(map(int,sys.stdin.readline().split()))
cards.sort()
dic_cards=dict()
for card in cards:
    if card not in dic_cards.keys():
        dic_cards[card]=1
    else:
        dic_cards[card]+=1
M = int(input())
numbers = list(map(int,sys.stdin.readline().split()))
answer = []
for i in numbers:
    answer.append(div_con(i))
for i in answer:
    print(i,end=" ")