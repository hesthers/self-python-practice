class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        from collections import Counter
        s_cnt = Counter(s)
        t_cnt = Counter(t)
        for i in t:
            if s_cnt.get(i, '0') == '0' or t_cnt[i]-s_cnt[i] == 1:
                return i
        
