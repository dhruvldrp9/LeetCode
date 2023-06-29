# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

# Solution:
class Solution:
    def isValid(self, s: str) -> bool:
        list = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                list.append(s[i])
            else :
                if not list:
                    return False
                if s[i] == ')' and list[-1] == '(':
                    list.pop()
                elif s[i] == '}' and list[-1] == '{':
                    list.pop()
                elif s[i] == ']' and list[-1] == '[':
                    list.pop()
                else:
                    return False
        return not list