from typing import List

def searchInsert(self, nums: List[int], target: int) -> int:
    for i, n in enumerate(nums):
        if n == target or n > target:
            return i
    return len(nums)