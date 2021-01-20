from typing import *
'''
주식 Profit 최대화
1. buy 한 번
2. sell 한 번
: 가장 쌀 때 사서, 가장 비쌀 때 팔면 됨 ->
input은 list로 주어짐
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 처음 시작 profit => 0 buy도 sell도 없기 때문에
        profit = 0
        # 최소 가격 초기값 설정
        min_price = 99999999
        # 주어진 가격은 전부 확인하면서 가장 작은 가격을 찾음
        # 현재가격에서 가장 작은 가격을 뺐을 때의 값이 가장 크면 그것이 정답 -> 이익의 최대화
        for price in prices:
            # 현재 가격이 최소 가격보다 작으면 최소 가격을 현재 가격으로 바꾸어 줌
            if price < min_price:
                min_price = price
            # 이익 => 현재 가격에서 최소 가격을 뺀 이익과, 현재 이익 중에서 큰 값
            profit = max(profit, price - min_price)
        return profit
if __name__ == "__main__":
    # example 데이터
    # [7,1,5,3,6,4],
    input_data = [7,6,4,3,1]
    solution = Solution()
    # 알고리즘 테스트
    answer = solution.maxProfit(input_data)
    print(answer)