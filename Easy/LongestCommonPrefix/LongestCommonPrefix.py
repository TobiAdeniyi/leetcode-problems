# Runtime: 28 ms, faster than 94.97% of Python3 online submissions
# Memory Usage: 13.8 MB, less than 87.63% of Python3 online submissions

# If list is empty return ""
# Initialise i = 1, and s = ""
# Let m be the length of the shortest strin
# Whilest sliced strings are the same and i < m:
## s = slice of any string
## i ++ 

class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        i = 1
        s = ""
        m = len(min(strs, key=len))
        while len({ss[:i] for ss in strs})==1 and i<=m:
            s = strs[0][:i]
            i += 1
        return s