class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        pascal_triangle = []
        for i in range(rowIndex + 1):
            list = []
            for j in range(i+1):
                if j == 0 or j == i:
                    list.append(1)
                else:
                    list.append(pascal_triangle[i-1][j-1] + pascal_triangle[i-1][j])
            pascal_triangle.append(list)
        return pascal_triangle[rowIndex]
C1 = Solution()
print(C1.getRow(4))