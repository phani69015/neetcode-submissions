import string
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0

        q = deque()
        v = set()
        wordList = set(wordList)

        q.append(beginWord)
        v.add(beginWord)
        c = 0

        while q:
            n = len(q)
            c+=1
            for _ in range(n):
                key = q.popleft()

                if key == endWord:
                    return c
                for i in range(len(key)):
                    for j in string.ascii_lowercase:
                        temp = key[:i] + j + key[i+1:]
                        if temp not in v and temp in wordList:
                            q.append(temp)
                            v.add(temp) 
        return 0
                          


                        



        


        