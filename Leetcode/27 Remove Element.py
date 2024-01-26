class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        k = 0
        i = 0
        x = len(nums)
        while i < len(nums):
            if nums[i] == val:
                nums.remove(nums[i])
            else:
                i += 1
                k += 1

        return k
