'''import sympy as sp
def lagrange(tab_with_xn_s):
    value_range = len(tab_with_xn_s[0])
    final_tab = ["" for x in range(value_range)]
    result_string = ''

    for iterator in range(0,value_range):
        string_part_1 = ''
        string_part_2 = ''

        for i in range(0,value_range):
            if i != iterator:
                if tab_with_xn_s[0][i] > 0 :
                    string_part_1 += '(x-' + str(tab_with_xn_s[0][i]) + ')'

                    if(i<value_range-1 ):
                        #tutaj jest bład
                        if i == 3:
                            string_part_1 += '*'
                        print("iterator: ",iterator,"i: ", i)

                else:
                    string_part_1 += '(x' + str(tab_with_xn_s[0][i]) + ')'
                    if (i < value_range - 1 ):
                        string_part_1 += '*'

            else:
                pass

        sum = 1
        print(tab_with_xn_s[0][iterator])
        for i in range(0, value_range):
             if iterator != i:
                 sum *= (tab_with_xn_s[0][iterator] -  tab_with_xn_s[0][i])
             else:
                 pass
        print(sum)
        print(1/sum)
        print(tab_with_xn_s[1][iterator])
        print((1/sum)*tab_with_xn_s[1][iterator])
        string_part_2 += str((1/sum)*tab_with_xn_s[1][iterator])
        final_string =   string_part_1 + '*(' +  string_part_2 + ')'

        final_tab[iterator] += '(' +  final_string + ')'
        result_string += final_string
        if (iterator < value_range - 1):
            result_string += '+'
    return result_string




coeffs  = [[1,1.5,2,2.5,3] , [1,3,4,2,0]]
tab =lagrange(coeffs)
#print(tab)
print(len(tab))
newstr = tab[:191] + tab[192:]
print(newstr)
print(sp.expand('(x-1.5)*(x-2)*(x-2.5)*(x-3)*(0.6666666666666666)+(x-1)*(x-2)*(x-2.5)*(x-3)*(-2.6666666666666665)+(x-1)*(x-1.5)*(x-2.5)*(x-3)*(4.0)'))
print(sp.expand('(x-1)*(x-1.5)*(x-2)*(x-3)*(-2.6666666666666665)+(x-1)*(x-1.5)*(x-2)*(x-2.5)*(0.6666666666666666)'))
print(sp.expand(newstr))'''
import sympy as sp
def lagrange(tab_with_xn_s):
    value_range = len(tab_with_xn_s[0])
    final_tab = ["" for x in range(value_range)]
    result_string = ''
    print(tab_with_xn_s[0][4])
    for iterator in range(0,value_range):
        string_part_1 = ''
        string_part_2 = ''
        for i in range(0,value_range):
            if i != iterator:
                if tab_with_xn_s[0][i] > 0 :
                    string_part_1 += '(x-' + str(tab_with_xn_s[0][i]) + ')'

                    if(i<value_range-1 ):
                        #moze sie zepsuc bardzo
                        if not (iterator == (value_range-1) and i == (value_range-2)):
                            string_part_1 += '*'
                            print("iterator: ",iterator,"i: ", i)

                else:
                    string_part_1 += '(x' + str(tab_with_xn_s[0][i]) + ')'
                    if (i < value_range - 1 ):
                        string_part_1 += '*'
            else:
                pass

        sum = 1
        print(tab_with_xn_s[0][iterator])
        for i in range(0, value_range):
             if iterator != i:
                 sum *= (tab_with_xn_s[0][iterator] -  tab_with_xn_s[0][i])
             else:
                 pass


        #print(sum)
        #print(1/sum)
        #print(tab_with_xn_s[1][iterator])
        #print((1/sum)*tab_with_xn_s[1][iterator])
        string_part_2 += str((1/sum)*tab_with_xn_s[1][iterator])
        final_string =   string_part_1 + '*(' +  string_part_2 + ')'

        final_tab[iterator] += '(' +  final_string + ')'
        result_string += final_string
        if (iterator < value_range - 1):
            result_string += '+'
    return result_string




coeffs  = [[1,1.5,2,2.5,3] , [1,3,4,2,0]]
tab =lagrange(coeffs)
#print(tab)
print(len(tab))
#newstr = tab[:191] + tab[192:]
newstr = tab
print(newstr)
print(sp.expand(newstr))
print(sp.expand('((x-6)*(4-x)/8)+((x-7)*(x-8)/7)'))
