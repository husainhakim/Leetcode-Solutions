class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        list=[]
        for i in sentence:
            if i not in list:
                list.append(i)
        if len(list)==26:
            return True
        else:
            return False
