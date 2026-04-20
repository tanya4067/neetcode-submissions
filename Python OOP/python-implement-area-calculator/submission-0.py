import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate_circle(self,radius:int):
        area = (math.pi * radius * radius)
        return(round(area,2))
    
    def calculate(self,length:int,width:int):
        return(length * width)

  
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate_circle(5))    
print(calc.calculate(4, 6))
