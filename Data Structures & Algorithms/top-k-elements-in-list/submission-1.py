class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #nums = [1, 1, 1, 2, 2, 3]
        #k = 2
        #We want the 2 most frequent numbers → [1, 2].
        count={}
        freq = [[] for i in range(len(nums) + 1)] #freq=[]of length range 7
        for n in nums: #n=1
            count[n] = 1 + count.get(n, 0) #count[1]=1+0 as get from dict as no 1 in dict 
            #count = { 1: 3,2: 2,3: 1} in the end

        for n, c in count.items(): #n=1,c=3
            freq[c].append(n) #freq array looks like
            #0 → []
            #1 → [3]
            #2 → [2]
            #3 → [1]
            #4 → []
            #5 → []
            #6 → []
        res=[]
        for i in range(len(freq)-1, 0, -1): #range 6 to 0 backwards 
            for n in freq[i]: #i=3,n=1.
                res.append(n) #res=[1,2]
                if len(res)==k:
                    return res   