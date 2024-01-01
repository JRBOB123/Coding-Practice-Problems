class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        x = sorted(nums)
        length = len(x)
        max_product = (x[length -1]-1) * (x[length -2]-1)

        return max_product

s1 = Solution()
s1.maxProduct([3,4,5,2])