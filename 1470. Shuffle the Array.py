class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l=[0 for i in range(2*n)]
        c=0
        k=0
        a=nums[:n]
        b=nums[n:]
        for i in range(2*n):
            if i%2==0:
                l[i]=a[c]
                c+=1
            elif i%2!=0:
                l[i]=b[k]
                k+=1
        return l

            
        
                
