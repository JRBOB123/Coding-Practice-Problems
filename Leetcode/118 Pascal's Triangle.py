class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascal_triangle = []
        for i in range(numRows):
            list = []
            for j in range(i+1):
                if j == 0 or j == i:
                    list.append(1)
                else:
                    list.append(pascal_triangle[i-1][j-1] + pascal_triangle[i-1][j])
            pascal_triangle.append(list)
        return pascal_triangle
c1 = Solution()
print(c1.generate(7))