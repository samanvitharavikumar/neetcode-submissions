class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        counts1 = {}
        counts2 = {}
        for c in s1:
            counts1[c] = counts1.get(c, 0) + 1

        for i in range(len(s2) - len(s1) + 1):
            #window is of 2 like ea ab..
            window = s2[i:i + len(s1)]
            counts2 = {}

            for p in window:
                counts2[p] = counts2.get(p, 0) + 1

            if counts1 == counts2:
                return True

        return False