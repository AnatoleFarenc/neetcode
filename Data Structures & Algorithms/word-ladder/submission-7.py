class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList:
            return 0
        words = set(wordList)
        if endWord not in words:
            return 0

        word_patterns = collections.defaultdict(list)
        for word in words:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                word_patterns[pattern].append(word)

        front, back = {beginWord}, {endWord}
        visited = {beginWord, endWord}
        steps = 1
        while front and back:
            if len(front) > len(back):
                front, back = back, front
            next_front = set()
            for node in front:
                for i in range(len(node)):
                    pattern = node[:i] + "*" + node[i + 1:]
                    for neighbor in word_patterns.get(pattern, []):
                        if neighbor in back:
                            return steps + 1
                        if neighbor not in visited:
                            visited.add(neighbor)
                            next_front.add(neighbor)
            front = next_front
            steps += 1
        return 0
        