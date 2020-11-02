''' 내가 짠 코드,, 시간 초과 떠서 실패

import sys


def permutations(arr,prefix,k):
    global c
    if c:
        return
    if len(prefix) == N+1:
        check = True
        for idx, val in enumerate(a):
            if val == "<":
                if prefix[idx]< prefix[idx + 1]:
                    continue
                else:
                    check = False
                    break
            else:
                if prefix[idx] > prefix[idx + 1]:
                    continue
                else:
                    check = False
                    break
        if check:
            print(''.join(list(map(str, prefix))))
            c=True

        else :
            yield prefix

    else:
        for i in range(k,len(arr)):
            arr[i], arr[k] = arr[k], arr[i]
            for next in permutations(arr,prefix + [arr[k]], k+1):
                yield next
            arr[i], arr[k] = arr[k], arr[i]


N = int(sys.stdin.readline())
a = list(sys.stdin.readline().split())
c=False
min_numbers = [i for i in range(0, 10)]
max_numbers = [i for i in range(9, -1, -1)]
list(permutations(min_numbers,[],0))
c=False
list(permutations(max_numbers,[],0))
'''
### 성공 코드 ,, 코드 분석 하고 공부해야함..


n = int(input())
op = input().split()
c = [False]*10
mx, mn = "", ""

def possible(i, j, k):
    if k == '<':
        return i < j
    if k == '>':
        return i > j
    return True

def solve(cnt, s):
    global mx, mn
    if cnt == n+1:
        if not len(mn):
            mn = s
        else:
            mx = s
        return
    for i in range(10):
        if not c[i]:
            if cnt == 0 or possible(s[-1], str(i), op[cnt-1]):
                c[i] = True
                solve(cnt+1, s+str(i))
                c[i] = False

solve(0, "")
print("%s\n%s" % (mx, mn))

