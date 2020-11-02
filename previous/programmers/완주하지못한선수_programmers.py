import collections


def solution(participant, completion):
    answer = ''
    dict_part = collections.defaultdict()
    for p in participant:
        if p in dict_part.keys():
            dict_part[p] += 1
        else:
            dict_part[p] = 1
    for c in completion:
        dict_part[c] -= 1
    for dp, v in dict_part.items():
        if v == 1:
            answer = dp

    return answer