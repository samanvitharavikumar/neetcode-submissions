class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=[]#empty stack to store [position,time]
        #pos=[10,8,3] and [1,2,3] target=12
        for i in range (len(position)): #i=0
            time=((target-position[i])/speed[i]) #time=12-10/1 =2
            cars.append((position[i],time)) #cars=[(10,2) and (8,2) amd (3,3)]
        cars.sort(reverse=True) #[(10,2),(8,2),(3,3)]
        stack=[]#keep track of the fleet times 
        pos=position[0]
        for pos,time in cars: #pos=10,time=2
            if not stack:#stack is currently empty
                stack.append(time)    #stack=[2]
            elif time>stack[-1]: #time is 2 which is NOT greater than 2. then time 3>2
                stack.append(time)
        return len(stack)        
                 


                
