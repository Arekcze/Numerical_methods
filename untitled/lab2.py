import sympy as sy
from sympy import S
def horner(coefficients, value):
    returnable_arr = coefficients.copy()
    if (len(coefficients) <= 2):
        returnable_arr[0] = coefficients[0]
        returnable_arr[1] = coefficients[1] + value*returnable_arr
        return returnable_arr
    else:
        iterator = 0
        for coefficient in coefficients:
            if iterator == 0:
                returnable_arr[iterator] = coefficients[iterator]
                iterator += 1
            else:
                returnable_arr[iterator] = coefficient + returnable_arr[iterator-1] * value
                iterator += 1
        return returnable_arr

def task2(coefficients,value,significance):
    print(horner(coefficients,value))
    mytab = horner(coefficients,value)
    print(mytab)
    val = mytab[len(mytab)-1]
    print(val)
    k = sy.symbols('k')
    print(sy.solveset((val<=(value**4-1)/(value-1))*0.5*10**k<significance,k,S.Reals).evalf())
    print(sy.solveset((-11.625<=(2.755**4-1)/(2.755-1))*0.5*10**k< 0.001, k, S.Reals).evalf())

def horner_intervals(coefficients,value):
    hornered = horner(coefficients,value)
    value_to_verify = True
    for element in hornered:
        if element < 0:
            value_to_verify = False
    return value_to_verify



coefficients = [1, -3.5,0, 2, -1]
print(coefficients[2])
value_in_point = 9
print(horner(coefficients, value_in_point))
x = sy.symbols('x')
task2(coefficients,value_in_point,0.001)

