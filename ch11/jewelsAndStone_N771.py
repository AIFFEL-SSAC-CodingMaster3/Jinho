class Solution(object):
    from collections import Counter
    def numJewelsInStones(self, jewels, stones):
        jewels = set(list(jewels))
        stones = Counter(stones)
        cnt = 0
        for jewel in jewels:
            cnt += stones[jewel]
            
        return cnt