# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        n = len(pairs)
        ans = []
        
        for i in range(n):               # include i=0 to capture initial state
            j = i - 1
            # Insert pairs[i] into sorted portion [0..i-1]
            while j >= 0 and pairs[j+1].key < pairs[j].key:
                # swap
                pairs[j], pairs[j+1] = pairs[j+1], pairs[j]
                j -= 1
            # Record state after this insertion (a copy of the list)
            ans.append(pairs[:])
        
        return ans
        