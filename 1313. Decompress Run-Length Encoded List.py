class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        l=[]
        for i in range(0,len(nums),2):
            l.extend([nums[i+1] for x in range(nums[i])])
        return l
