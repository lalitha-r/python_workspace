# Problem #5
# Same as above, but the operator come first.
# eg - input ["+","1", "2", "*", "5"]
# output =  15
# explanation (1 + 2) * 5 = 15
# input ["-","10", "+", "2", "3", "*", "5"]
# output =  25
# explanation (10 - ( 2 + 3)) * 5 = 25

def calc_value(input):
    stack = []
    result = 0  # Initialize the result to 0
    operators = ['+', '-', '*']

    for element in input:
        if element.isdigit():
            stack.append(int(element))
        elif element in operators:
            if len(stack) < 2:
                raise ValueError("Invalid expression format")
            num2 = stack.pop()
            num1 = stack.pop()

            if element == '+':
                result = num1 + num2
            elif element == '-':
                result = num1 - num2
            elif element == '*':
                result = num1 * num2

            stack.append(result)  # Push the result back onto the stack
        else:
            raise ValueError(f"Invalid element: {element}")

    if len(stack) != 1:
        raise ValueError("Invalid expression format")

    return stack[0]


# Test the function
expression = ["10", "2", "3", "+", "-", "5", "*"]
result = calc_value(expression)
print(result)  # Output: 25
