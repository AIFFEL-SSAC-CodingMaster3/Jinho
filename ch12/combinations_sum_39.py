class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []        
        candidates_len = len(candidates)
        def dfs(csum, index, path):
            
            if csum < 0:
                return
            elif csum == 0:
                result.append(path)
                return
            
            #자신부터 하위 재귀
            for i in range(index, candidates_len):
                dfs(csum-candidates[i], i, path + [candidates[i]])
        
        dfs(target, 0, [])
        return result
            
# 76~84ms

'''
# other1 
# lap-time 44~52ms
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, index, target, temp, ans):
            if (target == 0):
                ans.append(temp[:])
                return
            
            for i in range(index, len(candidates)):
                if (candidates[i] > target):
                    break;
                temp.append(candidates[i])
                dfs(candidates,i, target - candidates[i], temp, ans)
                temp.pop()
                
        ans = []
        temp = []
        candidates.sort()
        dfs(candidates, 0, target, temp, ans)
        return ans
        
#other2
# lap-time 32~56ms
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        list_cand = []
        
        def dfs(list_cur, candidates, target):
            
            for i,cand in enumerate(candidates):
                
                rem = target - cand
                
                if rem == 0:
                    list_cand.append(list_cur + [cand])
                    break
                
                elif rem > 0:
                    dfs(list_cur + [cand], candidates[i:], rem)
                else:
                    break
        
        # 담길 list, candidates를 오름차순 정렬, target
        dfs([], sorted(candidates), target)
        #2344566   17
        return list_cand

'''


