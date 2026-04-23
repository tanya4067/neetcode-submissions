from collections import defaultdict
from typing import List, Dict


def count_chars(s: str) -> Dict[str, int]:
    char_dict=defaultdict(int)
    for i in s:
        if(i in char_dict):
            char_dict[i]+=1
        else:
            char_dict[i]=1
        
    return(char_dict)
    pass


def nested_list_to_dict(nums: List[List[int]]) -> Dict[int, List[int]]:
    ans=defaultdict(list)
    for i in nums:
        key=i[0]
        value=i[1:]
        ans[key]+=value        
    
    return(ans)
    pass


# do not modify below this line
print(count_chars("hello"))
print(count_chars("helloworld"))
print(count_chars("areallylongstringwhyareyoureadingthishahalol"))

print(nested_list_to_dict([[1, 2, 3], [4, 5, 6], [1, 4]]))
print(nested_list_to_dict([[1, 2, 3, 4], [4, 5, 6, 7], [1, 4, 5, 6]]))
print(nested_list_to_dict([[5, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]))
print(nested_list_to_dict([[3, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8]]))
