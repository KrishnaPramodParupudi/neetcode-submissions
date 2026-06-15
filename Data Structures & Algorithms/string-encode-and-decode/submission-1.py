class Solution:

    def encode(self, strs: List[str]) -> str:
        str_res = ""
        for st in strs :
            str_res = str_res + st + "~``)"
        return str_res
    def decode(self, s: str) -> List[str]:
         res = s.split("~``)")
         return res[:len(res)-1]
