def solution(n, words):
    answer = [0, 0]
    temp = []
    order = 1
    for i, word in enumerate(words):

        if temp and word not in temp:
            if temp[-1][-1] == word[0]:
                temp.append(word)
            else:
                answer = [(i % n) + 1, order]
                break
        elif temp and word in temp:
            answer = [(i % n) + 1, order]
            break
        else:
            temp.append(word)
        if (i + 1) % n == 0:
            order += 1

    return answer