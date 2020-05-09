class Solution:
    def addDigits(self, num: int) -> int:
        sum=0
        if(num>=10):
            while num>=10:
                temp=[int(x) for x in str(num)]
                sum=0
                for i in range(len(temp)):
                    sum+=temp[i]
                num=sum
            return sum
        else:
            return num
