class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
      
        full = [0] + flowerbed + [0]

        if n== 0:
            return True

        for i in range(1,len(full)-1):
            if full[i] == 0 and full[i-1] == 0 and full[i+1] ==0:
                full[i] = 1
                n-=1

                if n==0:
                    return True
        return n==0

