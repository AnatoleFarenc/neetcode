class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        key = {}

        for word in strs:
            cur_k = "".join(sorted(word))
            if key.get(cur_k):
                key[cur_k].append(word)
            else:
                key.update({cur_k: [word]})
        result = [value for _, value in key.items()]
        return result
        