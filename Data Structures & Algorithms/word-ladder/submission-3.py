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

        word_patterns = collections.defaultdict(list)
        for word in words:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                word_patterns[pattern].append(word)
                

        while head < len(queu):
            node, step = queu[head]
            head += 1
            if node == endWord:
                return step

            for i in range(len(node)):
                pattern = node[:i] + "*" + node[i + 1:]
                for neighbor in word_patterns[pattern]:
                    if neighbor not in is_visited:
                        is_visited.add(neighbor)
                        queu.append((neighbor, step + 1))
        return 0