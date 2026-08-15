class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        for i in range(len(s), 0, -1):
            for j in range(len(s) - i + 1):
                c = Counter(s[j:j + i])

                if max(c.values()) <= 2:
                    return i
        return 0