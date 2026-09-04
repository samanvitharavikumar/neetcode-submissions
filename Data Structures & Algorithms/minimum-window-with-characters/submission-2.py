class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        countt={}
        counts={}
        #go thru all elements in the t string 
        for c in t:
            countt[c]=1+countt.get(c,0)    
        l=0
        res=0
        have=0
        need=len(countt)
        reslen=float("infinity")    
        #go thru al elements using right pointer r 
        for r in range (len(s)):
            #assign s[r] to p 
            p=s[r]
            counts[p]=1+counts.get(p,0)
            #if p in the str s is in countt ( t strings count)
            if p in countt and counts[p] == countt[p]:
                have+=1
                while have==need:
                    if (r-l+1<reslen):
                        res=[l,r]
                        reslen=r-l+1
                    counts[s[l]]-=1
                    if s[l] in countt and countt[s[l]]>counts[s[l]]:
                        have-=1
                    l+=1
        return s[res[0]:res[1]+1] if reslen!= float("infinity") else ""