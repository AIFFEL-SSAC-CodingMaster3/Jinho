class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:       
        for idx in range(len(nums)):
            other_num = target - nums[idx]
            if other_num in nums[0:idx]+nums[idx+1:]:
                return [idx, nums.index(other_num, idx+1)]
