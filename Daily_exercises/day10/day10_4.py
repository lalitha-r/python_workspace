# Problem #4
# Input is an array of strings of an arithmetic expression. Calculate the value.
# eg - input ["1", "2", "+", "5", "*"]
# output =  15
# explanation (1 + 2) * 5 = 15

# input ["10", "2", "3", "+","-", "5", "*"]
# output =  25
# explanation (10 - ( 2 + 3)) * 5 = 25
# Hint : Use the concept of stack. Push and pop.
# Parse the input list one element at a time. Convert to integer, push it to a stack. Whenever you see an
# operator, pop two elements from the stack, apply the operation and push the result back.

def calc_value(input):
    stack = []
    result = 0
    operators = ['+', '-', '*']
    for element in input:
        if element not in operators:
            stack.append(element)
        else:
            num2 = int(stack.pop(len(stack)-1))
            num1 = int(stack.pop(len(stack)-1))
            if (element == '+'):
                result = num1 + num2
                stack.append(result)
            elif (element == '-'):
                result = num1 - num2
                stack.append(result)
            elif (element == '*'):
                result = num1 * num2
                stack.append(result)

    return result


print(calc_value(["10", "2", "3", "+", "-", "5", "*"]))
