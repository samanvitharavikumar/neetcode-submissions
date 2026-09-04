class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        countt={}
        counts={}
        for c in t:
            countt[c]=1+countt.get(c,0)    
        l=0
        res=0
        have=0
        need=len(countt)
        reslen=float("infinity")    

        for r in range (len(s)):
            c=s[r]
            counts[c]=1+counts.get(c,0)
            
            if c in countt and counts[c] == countt[c]:
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