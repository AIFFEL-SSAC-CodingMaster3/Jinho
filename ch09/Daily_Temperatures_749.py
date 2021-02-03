#Time Limit Exceeded
class Solution:
    from collections import deque
    #from multiprocessing import Pool
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        
        result = [ 0 for _ in range(len(T)) ]
        max_temper = max(T)
        stack = deque()        
        
        #stack 각 요소는 (idx, temperature) 튜플로 구성
        for idx in range(len(T)):
            tmp = deque()
            today_temper = T[idx]
            for stk in stack:
                if today_temper > stk[1]:
                    result[stk[0]] = idx-stk[0]
                else:
                    tmp.append((stk[0], stk[1]))                    
            stack = tmp
            if max_temper > T[idx]:
                stack.append((idx, T[idx]))
            
        return result