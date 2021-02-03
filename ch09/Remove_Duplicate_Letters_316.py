#Wrong Answer
class Solution:
    #from collections from deque
    def removeDuplicateLetters(self, s: str) -> str:
        q = []
        s_len = len(s)
        for idx in range(s_len):
            if s[idx] not in s[idx+1:]:
                q.append(s[idx])
        return ''.join(q)
'''
사전식 순서란?
'''