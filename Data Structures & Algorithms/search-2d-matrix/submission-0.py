class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])
        top=0
        bot=rows-1
        
        while top<=bot:
            middle=(top+bot)//2
            if target<matrix[middle][0]:
                bot=middle-1
            elif target>matrix[middle][-1]:
                top=middle+1
            else:
                break

        if not top<=bot:
            return False        
        l=0
        r=cols-1
        while l<=r:
            m=(l+r)//2
            if target>matrix[middle][m]:
                l=m+1
            elif target< matrix[middle][m]:
                r=m-1
            else:
                return True 
        return False        
        