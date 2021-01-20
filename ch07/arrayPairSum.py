class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        result = 0
        for idx in range(0,len(nums),2):
            result += min(nums[idx], nums[idx+1])
            
        return result