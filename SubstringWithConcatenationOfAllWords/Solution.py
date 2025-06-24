class Solution(object):
    def findSubstring(self, s, words):
        words = list(set(words))  # Remove duplicates
        if not s or not words:
            return []
        n = len(s)
        word_length = len(words[0])
        word_count = len(words)
        total_length = word_length * word_count
        word_map = {word: words.count(word) for word in words}
        result = []
        for i in range(n - total_length + 1):
            seen = {}
            for j in range(word_count):
                start_index = i + j * word_length
                word = s[start_index:start_index + word_length]
                if word not in word_map:
                    break
                seen[word] = seen.get(word, 0) + 1
                if seen[word] > word_map[word]:
                    break
            else:
                result.append(i)