# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        op = []
        if not pairs:
            return op
        op.append(pairs.copy())  
        for i in range(1,len(pairs)):
            key = pairs[i]
            j = i - 1
            while j>=0 and pairs[j].key > key.key:
                pairs[j+1] = pairs[j] 
                j -= 1 
            pairs[j+1] = key
            op.append(pairs.copy()) 
        return op

