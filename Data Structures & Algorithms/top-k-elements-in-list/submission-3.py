class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_dict={}
        ans=[]
        for i in range(0,len(nums)):
            if(nums[i] in map_dict):
                map_dict[nums[i]]+=1
            else:
                map_dict[nums[i]]=1
        sorted_dict = dict(sorted(map_dict.items(), key=lambda item: item[1],reverse=True))
        print(sorted_dict)
        for k1,v1 in sorted_dict.items():
            if(len(ans)<k):
                ans.append(k1)
        return(sorted(ans))
        