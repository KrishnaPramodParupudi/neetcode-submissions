class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_alphanum = ""
        for cha in s:
            if cha.isalnum():
                s_alphanum +=cha
        i=0 
        j=len(s_alphanum)-1
        while (i<=j) :
            if s_alphanum[i].lower() != s_alphanum[j].lower() :
                return False
            i+=1
            j-=1
        return True

        