import collections
import operator

def solution(genres, plays):
    answer = []
    albums = collections.defaultdict()
    sum_albums= collections.defaultdict()
    for i in range(len(genres)):
        if genres[i] in albums.keys():
            albums[genres[i]].append([plays[i],i])
            sum_albums[genres[i]]+=plays[i]
        else:
            albums[genres[i]] = [[plays[i],i]]
            sum_albums[genres[i]] = plays[i]

    sum_albums=sorted(sum_albums.items(), key = lambda x : x[1],reverse=True)
    for sum_album in sum_albums:
        albums[sum_album[0]].sort(key = lambda x : x[0],reverse = True)
        cnt=0
        for a in albums[sum_album[0]]:
            answer.append(a[1])
            cnt+=1
            if cnt==2:
                break
    return answer