class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_common_prefix = ""
        current_common_prefix = ""
        shortest_string_length = len(min(strs, key=len))
        for c in range(shortest_string_length):
            for i in range(len(strs) - 1):
                if (strs[i][c] == strs[i + 1][c]):
                    current_common_prefix += strs[i][c]
                else:
                    longest_common_prefix = current_common_prefix
                    current_common_prefix = ""
        return longest_common_prefix