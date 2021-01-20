class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        from itertools import combinations
        
        result = []
        for case in combinations(nums,3):
            sorted_case = sorted(case)
            if sum(case) == 0 and sorted(case) not in result:                
                result.append(list(sorted_case))
                
        return result
		
# Time Limit Exceeded!!