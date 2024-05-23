class Solution:
    def beautifulSubsets(self, a: List[int], k: int) -> int:
        return (f:=lambda a,b,i:a[i:] and f(a,b,i+1)+(a[i]-k not in b and f(a,b+[a[i]],i+1)) or bool(b))(sorted(a),[],0) 