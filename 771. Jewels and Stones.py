class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels=list(J)
        stones=list(S)
        c=0
        for i in range(len(stones)):
            for j in range(len(jewels)):
                if stones[i]==jewels[j]:
                    c+=1
        return c
        
