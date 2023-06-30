# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Example 2:

# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]
 

# Constraints:

# 1 <= nums.length <= 200
# -109 <= nums[i] <= 109
# -109 <= target <= 109

# Solution

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        result = []
        for i in range(n-3):
            if i>0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n-2):
                if j>i+1 and nums[j] == nums[j-1]:
                    continue
                low = j+1
                high = n-1
                while low<high:
                    temp = nums[i] + nums[j] + nums[low] + nums[high]
                    if temp == target:
                        result += [nums[i], nums[j], nums[low], nums[high]],

                        while low<high and nums[low] == nums[low+1]:
                            low +=1
                        low+=1
                        while low<high and nums[high] == nums[high-1]:
                            high -= 1
                        high -= 1
                    elif temp < target:
                        low += 1
                    else:
                        high -= 1
        return result