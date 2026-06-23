class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        if len(s) > len(t):
            return False
        if len(s) == len(t):
            return s == t
        
        for i in range(len(t)):
            if t[i] == s[0]:
                t_cursor = i
                s_cursor = 0
                while t_cursor < len(t) and s_cursor < len(s):
                    if t[t_cursor] == s[s_cursor]:
                        t_cursor += 1
                        s_cursor += 1
                    else:
                        t_cursor += 1
                if s_cursor == len(s):
                    return True
        return False