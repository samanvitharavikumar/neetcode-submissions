class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen=defaultdict(list)
        #stores like {"a": [10, 20],"b": [50, 60]}
        for s in strs:
            count=[0]*26
            for c in s:
                count[ord(c)-ord("a")]+=1 #ord gives value of chars
            x=tuple(count)    
            seen[x].append(s) 
            #seen={a:[1,0,1],etc}
        return list(seen.values()) 
        #list of values. ["act","cat"]