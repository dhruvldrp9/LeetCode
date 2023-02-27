# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

 

# Example 1:

# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:

# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
# Example 3:

# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
 

# Constraints:

# 1 <= s.length <= 20
# 1 <= p.length <= 20
# s contains only lowercase English letters.
# p contains only lowercase English letters, '.', and '*'.
# It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.


#Program
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        a, b = len(s), len(p)
        q = [[False] * (b + 1) for _ in range(a + 1)]
        q[0][0] = True
        for j in range(1, b + 1):
            if p[j - 1] == '*':
                q[0][j] = q[0][j - 2]
        for i in range(1, a + 1):
            for j in range(1, b + 1):
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    q[i][j] = q[i - 1][j - 1]
                elif p[j - 1] == '*':
                    q[i][j] = q[i][j - 2]
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        q[i][j] |= q[i - 1][j]
        return q[a][b]