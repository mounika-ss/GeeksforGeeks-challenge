class Solution:
    @staticmethod
    def constructLps(pat, lps):
        length = 0  # Length of the previous longest prefix suffix
        m = len(pat)
        lps[0] = 0  # lps[0] is always 0
        
        i = 1
        while i < m:
            if pat[i] == pat[length]:  # Match case
                length += 1
                lps[i] = length
                i += 1
            else:  # Mismatch case
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

    def search(self, pat, txt):
        n, m = len(txt), len(pat)
        lps = [0] * m  # Initialize LPS array
        result = []
        
        # Preprocess pattern (calculate LPS array)
        Solution.constructLps(pat, lps)
        
        i, j = 0, 0  # Pointers for txt and pat
        while i < n:
            if txt[i] == pat[j]:  # Match
                i += 1
                j += 1
                if j == m:  # Full pattern match
                    result.append(i - j)
                    j = lps[j - 1]  # Continue matching
            else:  # Mismatch
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return result
