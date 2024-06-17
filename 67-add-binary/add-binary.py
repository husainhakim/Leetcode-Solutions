class Solution:
    def addBinary(self, a: str, b: str) -> str:
      
        inta = int(a, 2)
        intb = int(b, 2)
        
        
        sum_int = inta + intb
        
        
        sum_bin = bin(sum_int)[2:]  
        return sum_bin
