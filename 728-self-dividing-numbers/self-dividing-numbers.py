class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        list1=[]
        count=0
        for i in range(left,right+1):
            count=0
            s=str(i)
            for j in s:
                j=int(j)
                if j!=0 and i%j==0:
                    count+=1
            if count==len(s):
                list1.append(i)
        return list1

        

