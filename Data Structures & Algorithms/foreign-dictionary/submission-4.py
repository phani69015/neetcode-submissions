
from collections import deque
from typing import List

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        i = 0
        j = 1
        arr = []
        chars = set()

        for word in words:
            for ch in word:
                chars.add(ch)

        while j < len(words):
            s1 = words[i]
            s2 = words[j]

            x = 0
            y = 0

            while x < len(s1) and y < len(s2):
                if s1[x] != s2[y]:
                    arr.append([s1[x], s2[y]])
                    break

                x += 1
                y += 1

            # Prefix case:
            # "abc" before "ab" is invalid
            if x == len(s2) and x < len(s1):
                return ""

            i += 1
            j += 1

        ind = {}
        adj = {}

        for i in chars:
            ind[i] = 0
            adj[i] = []

        for x, y in arr:
            ind[y] += 1
            adj[x].append(y)

        ans = ""
        q = deque()

        for i in ind.keys():
            if ind[i] == 0:
                q.append(i)

        while q:
            key = q.popleft()
            ans += key

            for nei in adj[key]:
                ind[nei] -= 1

                if ind[nei] == 0:
                    q.append(nei)

        return ans if len(ans) == len(chars) else ""


