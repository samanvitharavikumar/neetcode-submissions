class Solution:
    #strs = ["hello", "world", "hi"]
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs: #hello
          res += str(len(s)) + "#" + s #len(s)=5. str(5)+#+s= 5#hello
        #res="5#hello5#world2#hi"
        return res
    def decode(self, s: str) -> List[str]:
        
        #s="5#hello5#world2#hi"
        res = []
        i = 0 #i=index 0,val=5
        while i<len(s): #0<
            j=i#j=index 0
            while s[j] != "#": #if the value is not a hash and os a cjaracter. j is 5
                j += 1 #j=#
            length = int(s[i:j]) 
            #i=0,j=1. s[0:1]=5. this means lenght=5.
            # 5 characters after # are the required word
            res.append(s[j + 1:j + 1 + length]) #s[2:7]=hello
            i=j+1+length #i=7. which is 5 
        return res               