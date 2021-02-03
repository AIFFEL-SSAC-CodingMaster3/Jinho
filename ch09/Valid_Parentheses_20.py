class Solution:
    def isValid(self, s: str) -> bool:
        the_list = []        
        
        for spel in list(s):
            if spel in ( '[', '(', '{' ):
                the_list.append(spel)
            elif the_list:
                pop_val = the_list.pop()
                if pop_val == '(' and spel != ')':
                    return False
                elif pop_val == '{' and spel != '}':
                    return False
                elif pop_val == '[' and spel != ']':
                    return False
            else: # ) } ] 가 먼저 들어온 경우
                return False
                
        if not the_list:
            return True