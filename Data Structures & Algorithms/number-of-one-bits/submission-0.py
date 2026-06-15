class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_rep = str(bin(n))
        return bin_rep.count('1')
        