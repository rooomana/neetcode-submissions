class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        shortest_length = len(min(strs, key=len))
        for c in range(shortest_length):
            char = strs[0][c]
            for i in range(len(strs) - 1):
                if (strs[i][c] != strs[i + 1][c]):
                    return prefix
            prefix += char
        return prefix