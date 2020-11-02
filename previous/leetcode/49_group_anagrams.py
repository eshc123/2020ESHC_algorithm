strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

anag_dict = dict()
for str in strs:
    temp = ''.join(sorted(list(str)))
    if temp not in anag_dict.keys():
        anag_dict[temp] = [str]
    else:
        anag_dict[temp].append(str)
print(anag_dict)