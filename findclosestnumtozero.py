# Given an integer array nums of size n, 
# return the number with the value closest to 0 in nums. If there are multiple answers, return the number with the largest value.

def findClosestNumber(self, nums: List[int]) -> int:
    closest = nums[0]
    for num in nums:
        abs_num,abs_closest = abs(num),abs(closest)
        if( abs_num < abs_closest or (abs_num == abs_closest and num > closest)):
            closest = num
    return closest 