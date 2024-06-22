class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        combined=list(zip(names,heights))
        def get_height(element):
             return element[1]
        combinedsorted=sorted(combined,key=get_height,reverse=True)
        sortednames=[name for name,height in combinedsorted]
        return sortednames
