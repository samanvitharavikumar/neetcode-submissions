class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #piles = [1, 4, 3, 2]
        #h= 9
        #k isthe rate at which the bananas can be eaten. 2 banas per hr
        l = 1
        r = max(piles) #4
        while l <= r:
            k = (l + r) // 2 #5/2=2
            hrs=0
            for banana in piles:
                hrs+=(banana+k-1)//k 
            #banana=1,k=2, hrs=1
            #banana=4,k=2,hrs=2+1=3
            #banana=3,k=2,hrs=2+3=5
            #banana=2,k=2,hrs=6
            if hrs <= h: #6<9
                r = k - 1 #r=1
            else:
                l = k + 1
        return l