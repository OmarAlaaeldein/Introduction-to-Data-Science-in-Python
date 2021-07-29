import sympy
x=sympy.Symbol('x')
y=0
while y!='exit':
    print(sympy.solve(eval(input())))
    y=input('type exit to end scipt, or any thing else to use again \n')