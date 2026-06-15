class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_freq = {}
        for num in nums:
            dict_freq[num] = dict_freq.get(num,0) + 1
        sorted_dict = dict(sorted(dict_freq.items(), key=lambda item:item[1],
                       reverse=True))
        return list(sorted_dict.keys())[:k]