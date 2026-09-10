class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=defaultdict(list)
        for s in strs: #take act
            count = [0] * 26 #since there are 26 letters [0,0,0...]
            for c in s: #take a from act
                count[ord(c)-ord("a")]+=1
                #ord("a")=97. so ord c-a gives 0 as both are 'a' itself.
                #so count of character a = 1

                #tuple(count) converts count=[1,0,0,0..] into (1,0,0,....)
            x=tuple(count)
            result[x].append(s) #result = {(1,0,0,0,..): ["act"]}
        return list(result.values())        
