from basic.stack import Stack

"""
If the token is an operand, convert it from a string to an integer and push the value onto the operandStack.
If the token is an operator, *, /, +, or -, it will need two operands. Pop the operandStack twice. 
    The first pop is the second operand and the second pop is the first operand. 
        Perform the arithmetic operation. Push the result back on the operandStack.
"""

def postfix_eval(s):
    """
    s: postfix expression: A + B * C --> ABC*+
    """
    valid_list = '0123456789'
    num = Stack()
    tokens = s.split()

    for token in tokens:
        if token in valid_list:
            num.push(int(token))
        else:
            num2 = num.pop()
            num1 = num.pop()
            result = cal(token, num1, num2)
            num.push(result)

    return num.pop()

def cal(op, num1, num2):
    if op == '*':
        result = num1 * num2
    elif op == '/':
        result = num1 / num2
    elif op == '+':
        result = num1 + num2
    else:
        result = num1- num2

    return result

print(postfix_eval('7 8 + 3 2 + /'))
