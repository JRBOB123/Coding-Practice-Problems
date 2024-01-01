class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        count_flower = 0
        index_num = []
        count_plant = 0
        if sum(flowerbed) == 0:
            count_plant = (len(flowerbed) + 1) // 2
        else:
            i = 0
            while count_flower != 1:
                if flowerbed[i] == 1:
                    index_num.append(i)
                    if i % 2 == 0:
                        count_plant += i//2
                    elif i % 2 == 1:
                        count_plant += i//3
                    count_flower = 1
                else:
                    i += 1

            if i < len(flowerbed) - 1:
                for j in range(i+1, len(flowerbed)):
                    if flowerbed[j] == 1:
                        index_num.append(j)
                        if len(index_num) == 2:
                            num = index_num[1] - index_num[0]-3
                            if num >0:
                                count_plant += (num+1)//2
                            index_num = []
                            index_num.append(j)
                if len(flowerbed) -1 != index_num[0]:
                    num = len(flowerbed)-1 - index_num[0]
                    count_plant += num // 2

        if count_plant >= n:
            return True
        else:
            return False

s1 = Solution()
#s1.canPlaceFlowers([0,1,0,0,0,1,0,0,0,0,0,1], 1)
s1.canPlaceFlowers([1,0,1,0,0,1,0], 1)
#s1.canPlaceFlowers([1,0,0,0,1], 2)
