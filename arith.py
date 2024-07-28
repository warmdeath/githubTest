def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return('Error: Too many problems.')
    first_line = ""
    second_line = ""
    third_line = ""
    fourth_line = ""
    for prob in problems:
        operator = prob.find(" + ")
        if prob.find(" * ") > -1 or prob.find(" / ") > -1:
            return("Error: Operator must be '+' or '-'.")
        elif operator > -1:
            pass
        else:
            operator = prob.find(" - ")
        plus_or_minus = prob[operator+1]
        op1 = prob[0:operator]
        op2 = prob[operator+3:len(prob)]
        if not op1.isnumeric() or not op2.isnumeric():
            return('Error: Numbers must only contain digits.')

        if len(op1) > 4 or len(op2) > 4:
            return('Error: Numbers cannot be more than four digits.')
        
        underscores = max(len(op1),len(op2))+2
        third_line += (underscores*"-")+"    "
        
        op1_off = underscores - len(op1)
        first_line += (op1_off*" ")+op1+"    "
        
        op2_off = underscores - len(op2)-1
        second_line += plus_or_minus+(op2_off*" ")+op2+"    "

        if show_answers:
            result = 0
            if plus_or_minus == "+":
                result = int(op1)+int(op2)
            else:
                result = int(op1)-int(op2)
            res_off = underscores-len(str(result))
            prepend = " "*res_off
            fourth_line += prepend+str(result)+"    "
        # print(f"operator {plus_or_minus} is at: {operator}",op1,op2,underscores)
    full = first_line.rstrip(" ")+"\n"+second_line.rstrip(" ")+"\n"+third_line.rstrip(" ")
    if fourth_line != "":
        full+="\n"+fourth_line.rstrip(" ")
    return full    

print(f'\n{arithmetic_arranger(["98 + 35", "3801 - 2", "45 + 43", "123 + 49"],True)}')