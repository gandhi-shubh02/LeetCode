class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans=[None for i in range(len(indices))]
        word=list(s)
        for i in range(len(ans)):
            ans[indices[i]]=word[i]
        ans="".join(ans)
        return ans
