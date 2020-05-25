class Solution:
    def search(self, nums: List[int], target: int) -> int:
            f=0
            l=len(nums)-1
            mid=0
            while f<=l :
                mid=(f+l)//2
                if nums[mid]==target:
                    return mid
                if target>nums[mid]:
                    f=mid+1
                else:
                    l=mid-1
            return -1
           
