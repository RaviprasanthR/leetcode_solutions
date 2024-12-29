# Given an integer array nums, find the subarray, with the largest sum, and return its sum.

def maxSubArray(self, nums: List[int]) -> int:
    max_sum = float('-inf')
    curr_sum = 0
    for i in nums:
        curr_sum += i
        max_sum = max(curr_sum,max_sum)
        if(curr_sum < 0):
            curr_sum = 0

    return max_sum