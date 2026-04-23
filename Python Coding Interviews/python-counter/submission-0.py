from collections import Counter
from typing import Counter as CounterType


def count_chars(s1: str, s2: str) -> CounterType:
    s=s1+s2
    ans=Counter(s)
    # for i in s:
    #     if(i in ans):
    #         ans[i]+=1
    #     else:
    #         ans[i]=1
    return(ans)
    pass
  

# do not modify below this line
print(count_chars("hello", "world"))
print(count_chars("hello", "worldhello"))
print(count_chars("areallylongstring", "heyhowisitgoing"))
