class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Approach 1 -> O(1) space and O(N*M) time
        #min_len = len(strs[0])
        #min_word = ""
        #fin_str = ""
        #for word in strs:
         #   if len(word) < min_len :
          #      min_word = word
           #     min_len = len(word)
        #for i in range(min_len):
         #   for word in strs :
          #      if min_word[i] != word[i] :
           #         return fin_str
            #fin_str += min_word[i]
        #return fin_str

        #Approach 2 -> Same approach better code
        min_word = min(strs, key = len)
        prefix =""
        for i in range(len(min_word)) :
            for word in strs:
                if min_word[i] != word[i]:
                    return prefix
            prefix +=word[i]
        return prefix

        