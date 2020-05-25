class Solution:
    def defangIPaddr(self, address: str) -> str:
        l=list(address)
        for i in range(len(l)):
            if l[i]=='.':
                l[i]='[.]'
        str=''.join(l)
        return str
