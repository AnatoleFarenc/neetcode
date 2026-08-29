class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            sorte_w = "".join(sorted(word))
            res[sorte_w].append(word)
        return list(res.values())