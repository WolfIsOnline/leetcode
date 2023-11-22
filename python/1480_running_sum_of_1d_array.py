from typing import List

def runningSum(self, nums: List[int]) -> List[int]:
    sums = []
    _sum = 0
    for c in nums:
        _sum = _sum + c
        sums.append(_sum)
    return sums