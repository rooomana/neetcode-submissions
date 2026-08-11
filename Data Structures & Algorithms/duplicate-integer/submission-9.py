class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_hash = set(nums)
        has_size_difference = len(nums) > len(nums_hash)
        return has_size_difference
        