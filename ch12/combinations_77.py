class Solution:
    from itertools import combinations
    def combine(self, n: int, k: int) -> List[List[int]]:
        n_list = [i for i in range(1,n+1)]
        return combinations(n_list, k)