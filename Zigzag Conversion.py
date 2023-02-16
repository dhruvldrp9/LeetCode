# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);
 

# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# Example 3:

# Input: s = "A", numRows = 1
# Output: "A"
 

# Constraints:

# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000

#Program


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rev = 1
        temp = []
        ind = 0
        ans = ""
        if numRows > len(s):
            x = numRows + 1
        else:
            x = len(s) + 1
        for i in range(x):
            temp.append("")
        for i in range(len(s)):
            temp[ind] += s[i]
            if ind == (numRows-1) or ind == 0:
                rev = 1 - rev
            if rev:
                ind -= 1
            else:
                ind += 1
        for i in range(x-1):
            ans += temp[i]
        return ans