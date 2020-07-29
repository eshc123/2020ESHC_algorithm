# def inequality_min(idx, a):
#     if len(a) == N + 1:
#         print(a)
#         return
#     if idx + 1 > len(min_numbers):
#         return
#     inequality_min(idx + 1, a + [min_numbers[idx]])
#     inequality_min(idx + 1, a)


# def b_permutation(n):
#     idx = -1
#     for i in range(n,0,-1):
#         if max_arr[i-1]>max_arr[i]:
#             idx = i
#             break
#     if idx == -1:
#         print(idx)
#         return
#     else :
#         for i in max_numbers:
#             #print(i)
#             if i not in max_arr and max_arr[idx]>i:
#                 max_arr[idx]=i
#                 break
#     print(max_arr)
#     b_permutation(n)
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
# for i in list(permutations(min_numbers,[],0)):
#     check=True
#     for idx,val in enumerate(a):
#         if val=="<":
#             if i[idx]<i[idx+1]:
#                 continue
#             else:
#                 check=False
#                 break
#         else :
#             if i[idx]>i[idx+1]:
#                 continue
#             else:
#                 check = False
#                 break
#     if check:
#         print(''.join(list(map(str,i))))
#         break

# for i in list(permutations(max_numbers,[],0)):
#     check=True
#     for idx,val in enumerate(a):
#         if val=="<":
#             if i[idx]<i[idx+1]:
#                 continue
#             else:
#                 check=False
#                 break
#         else :
#             if i[idx]>i[idx+1]:
#                 continue
#             else:
#                 check = False
#                 break
#     if check:
#         print(''.join(list(map(str,i))))
#         break

# min_arr = [i for i in range(0, N+1)]
# max_arr = [i for i in range(9, 9-N-1, -1)]
# #print(min_numbers, max_numbers)
# b_permutation(N)

