from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
    for c, num in enumerate(nums):
        for x, num2 in enumerate(nums):
            if target == num + num2:
                if c == x:
                    continue
                return {c, x}