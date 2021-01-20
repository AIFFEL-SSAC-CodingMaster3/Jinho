class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        from itertools import combinations
        
        tmp_dict = {}
        for case in combinations(nums,3):
            sorted_case = tuple(sorted(case))
            if sum(case) == 0 and not tmp_dict[sorted_case]:
                tmp_dict[sorted_case] = sorted_case
                
        result = []
        for case in tmp_dict:
            result.append(tmp_dict)
                
        return result
		
# Time Limit Exceeded!!