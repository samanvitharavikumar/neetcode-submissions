class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[]#store temp and index
        #consider [73,74,75]
        for i,t in enumerate(temperatures): #in first iter i=0,t=73 
                                            #in iter 2 , i=1,t=74 and stack=73 where top is 73
            while stack and t>stack[-1][0]:#stack is empty in iter 1 so append 73,0 to the stack
                stackt,stackind=stack.pop() 
            #pop the top of the stack along w the index. now the stack is empty
            #add to the res array
                res[stackind]=i-stackind #(i=1,stackind=0)
            stack.append([t,i])
        return res    