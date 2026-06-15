class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_dict = {}
        for word in strs:
            word_tup = create_tuple(word)
            final_dict.setdefault(word_tup, []).append(word)
        return list(final_dict.values())
        
def create_tuple(word) :
    l = [0]*26
    for cha in word.lower() :
        l[ord(cha)-ord('a')] +=1
    return tuple(l)

        