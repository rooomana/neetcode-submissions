class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = []
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if (i != j and nums[i] + nums[j] == target):
                    indexes.append(i)
                    indexes.append(j)
                    return indexes
        return indexes
