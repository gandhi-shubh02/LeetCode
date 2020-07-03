class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums=[0 for i in range(n)]
        xor_=0
        for i in range(n):
            nums[i]=start+2*i
            xor_=xor_^nums[i]
        return xor_
