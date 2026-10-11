class Solution:
     
    def encode(self, strs: List[str]) -> str:
       #["Hello","World"]
       res=""#empty str
       for s in strs:
         res+=str(len(s))+"#"+s
       return res  
    def decode(self, s: str) -> List[str]:
        res=[]
        i,j=0,0
        while i<len(s):#lens =5
            j=i
            while s[j]!="#":
                j=j+1
            length=int(s[i:j])  #s[0:1]=5
            res.append(s[j+1:j+1+length])
            i=j+1+length
        return res