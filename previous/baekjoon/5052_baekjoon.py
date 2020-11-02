import sys


class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = True



    def search(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.word


    def startsWith(self,prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    t = int(sys.stdin.readline().rstrip())
    s = []
    b = True
    trie = Trie()
    for __ in range(t):
        number = str(sys.stdin.readline().rstrip())
        trie.insert(number)
        s.append(number)
    for i in range(len(s)):
        if trie.search(s[i]):
            print("No")
            b= False
            break
    if b:
        print("Yes")
