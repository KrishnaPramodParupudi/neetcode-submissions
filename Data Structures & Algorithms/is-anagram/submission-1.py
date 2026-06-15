class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        for ch in s :
            dict_s[ch] = dict_s.get(ch, 0) + 1
        for ch1 in t:
            dict_t[ch1] = dict_t.get(ch1,0) + 1
        if len(list(dict_s.keys())) != len(list(dict_t.keys())) :
            return False
        for cha in list(dict_s.keys()) :
            if dict_s.get(cha.lower()) != dict_t.get(cha.lower()) :
                return False
        return True

            
        
        