class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList:
            return 0
        words = set(wordList)
        if endWord not in words:
            return 0

        queu = [(beginWord, 1)]
        is_visited = {beginWord}
        head = 0
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        while head < len(queu):
            node, step = queu[head]
            head += 1
            if node == endWord:
                return step
            for letter in alphabet:
                for i, char in enumerate(node):
                    if char == letter:
                        continue
                    attempt = node[:i] + letter + node[i + 1:]
                    if attempt in words and attempt not in is_visited:
                        is_visited.add(attempt)
                        queu.append((attempt, step + 1))
        return 0
        