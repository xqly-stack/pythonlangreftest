# euklid 

from dataclasses import dataclass

@dataclass(kw_only=True)
class ggT:
    
    a: int
    b: int
    
    def calcggT(self: object) -> int:
        
        temp_a:int
        temp_b: int
        r_ab: int
        temp_a = self.a
        temp_b = self.b
        
        while True:

            if temp_b == 0:
                # to avoid the zero division erorr
                print(f"\nggT={temp_a}")
                return temp_a
            
            r_ab = temp_a%temp_b
            print(temp_a, "%",temp_b, "=",r_ab)
            
            temp_a = temp_b
            temp_b = r_ab
            print(temp_a)
    
    
newggt: ggT = ggT(a=30,b=12)

newggt.calcggT()