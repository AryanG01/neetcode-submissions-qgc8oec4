class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        lcs = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    lcs[i + 1][j+ 1] = lcs[i][j] + 1
                else:
                    l1 = lcs[i][j + 1]
                    l2 = lcs[i + 1][j]
                    lcs[i + 1][j + 1] = max(l1, l2)
        
        return lcs[-1][-1]