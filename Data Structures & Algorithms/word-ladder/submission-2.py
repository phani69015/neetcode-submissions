import string
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        q = deque()
        q.append(beginWord)

        wordList = set(wordList)
        v = set()
        v.add(beginWord)
        
        c = 0

        while q:
            c+=1
            for _ in range(len(q)):
                key = q.popleft()

                if key == endWord:
                    return c

                for i in range(len(key)):
                    for alpha in string.ascii_lowercase:
                        temp = key[:i] + alpha + key[i+1:]  
                        if temp not in v and temp in wordList:
                            q.append(temp)
                            v.add(temp) 
        return 0             
                
        