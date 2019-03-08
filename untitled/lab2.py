def horner(coefficients, value):
    returnable_arr = coefficients
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

def 
coefficients = [1, 3, 3, 4]
print(coefficients[2])
value_in_point = 5
print(horner(coefficients, value_in_point))