# Leetcode daily 10.12.23
class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        m_len = len(matrix)
        n_len = len(matrix[0])
        n = []

        for i in range(n_len):
            n.append([0] * m_len)
            for j in range(m_len):
                n[i][j] = matrix[j][i]

        return n

s1 = Solution()
print(s1.transpose([[1,2,3],[4,5,6],[7,8,9]]))
print(s1.transpose([[1,2,3],[4,5,6]]))


