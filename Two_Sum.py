class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            diffrence = target - int(nums[i])
            for j in range(len(nums)):
                if diffrence == int(nums[j]):
                    if i != j :
                        return i,j
            