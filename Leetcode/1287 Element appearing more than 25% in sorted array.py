# Leetcode daily
class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        count_array = []
        count_num = []
        count = 0
        length = len(arr)

        for i in range(len(arr)):
            if arr[i] not in count_array and count > 0:
                count_num.append(count)
                count = 0
            if arr[i] not in count_array:
                count_array.append(arr[i])
                count += 1
            else:
                count += 1
        count_num.append(count)
        max_count = count_num.index(max(count_num))
        max_num = count_array[max_count]
        return max_num
s1 = Solution()
s1.findSpecialInteger([1,2,2,6,6,6,6,7,10])
s1.findSpecialInteger([1,1])
