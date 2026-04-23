import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    min_heap=[]
    for i in nums:
        heapq.heappush(min_heap,-i)
    
    ans=[]
    while min_heap:
        top=-heapq.heappop(min_heap)
        ans.append(top)
    
    return(ans)
    pass





# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
