class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        
        for i,j in enumerate(nums):
            if d.get(target-j) is not None:
                return [d.get(target-j),i]    
            d[j] = i
