import math
import numpy

RADIOS = 10
ACCURACY = 10**(-6)
def execute() :
    print("開始")
    
    beforeX = RADIOS
    beforeY = 0
    circumference = 0
    for i in numpy.arange(ACCURACY,RADIOS,ACCURACY) :
        x = RADIOS - i
        y = demandHeight(x,RADIOS)
        
        hypotenuse = demandHypotenuse(beforeX - x,y - beforeY)
        beforeX = x
        beforeY = y

        circumference = circumference + hypotenuse
    
    print(f"円周率　:　{circumference * 4 / 2 * RADIOS / 100}")

    print("終了")
    
def demandHeight(bottom,hypotenuse) :
    bottomSquare = bottom ** 2
    hypotenuseSquare = hypotenuse ** 2
    return math.sqrt(hypotenuseSquare - bottomSquare)

def demandHypotenuse(bottom,height) :
    bottomSquare = bottom ** 2
    heightSquare = height ** 2
    return math.sqrt(bottomSquare + heightSquare)


if __name__ == "__main__" :
    execute()