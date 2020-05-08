class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        temp = 0
        num = []
        f=True
        for i in range(left, right + 1):
            temp = i
            f = True
            while temp != 0 and f==True :
                dig = temp % 10
                if dig!=0:
                    if i % dig != 0:
                        f = 0

                    if i % dig == 0 :
                        f = 1
                else:
                    f=False
                temp = temp // 10
            if f==True:
                num.append(i)
        return num
