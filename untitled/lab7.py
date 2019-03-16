
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



def normal_method(coefficients, value):
    mysum = 0
    my_itr = 0
    if my_itr != len(coefficients)-1:
        for coefficient in coefficients:
            temp = len(coefficients)-1-my_itr
            mysum += (coefficient *pow(value,temp))
            my_itr +=1

    else:
        mysum+= coefficients[len(coefficients)-1]
    return mysum

def check_for_intervals(coefficients):
    pass


def lagrange_sinus(value,significance):
    iterator = 1;
    value_of_function = 0;
    diff = value + significance +2;
    previous =0
    while(abs(diff  - value_of_function)>significance):
        if iterator == 1:
            previous = (value)
            iterator+=2
            value_of_function += previous
        else:
            diff = value_of_function
            previous =  previous * (-1)*(value)*(value)/((iterator)*(iterator-1))
            value_of_function += previous
            iterator+=2
            #print(value_of_function)
            print((iterator/2)-0.5)
    return  value_of_function


coefficients = [1, 3,3,1]
#print(coefficients[2])
value_in_point = -5
print(horner(coefficients, value_in_point))
#print(normal_method(coefficients,value_in_point))
print(lagrange_sinus(0.4,0.000001))


