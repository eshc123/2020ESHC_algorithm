def solution(begin, target, words):
    answer = 0

    def compare(s1, s2):
        cnt = 0
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                continue
            else:
                cnt += 1
        return True if cnt == 1 else False

    def search(s, cnt, arr):
        if s == target:
            answer.add(cnt)
            return cnt
        if cnt >= len(words):
            # print(s)
            return False
        for i, word in enumerate(words):
            if word in arr:
                continue
            if compare(s, word) and visited[i] == 0:
                arr.append(word)
                visited[i] == 1
                search(word, cnt + 1, arr)
                arr.pop()

    if target not in words:
        return 0
    answer = set()
    for word in words:
        visited = [0 for i in range(len(words))]
        if compare(begin, word):
            search(word, 1, [])
    return min(answer)