class calculatorx:
    def addition(self,x,y):
        added = x + y
        print(added)
    
    def subtraction(self,x,y):
        sub = x -y
        print(sub)

    def multiplication(self,x,y):
        mult = x * y
        print(mult)
    
    def division(self,x,y):
        div = x / y
        print(div)

calculator = calculatorx()
calculator.addition(10,10)
calculator.subtraction(10,10)
calculator.multiplication(10,10)
calculator.division(10,10)