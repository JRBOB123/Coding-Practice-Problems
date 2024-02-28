class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        num_list = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            num_list[nums[i]] += 1


        missing_num = num_list.index(0)

        return missing_num

s1 = Solution()
s1.missingNumber([3,0,1])
s1.missingNumber([0,1])
s1.missingNumber([9,6,4,2,3,5,7,0,1])