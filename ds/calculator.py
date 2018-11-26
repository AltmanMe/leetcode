from basic.stack import Stack
import pdb

def calculator(s):
    """
    s: string
    """
    precedence = dict()
    precedence['+'] = precedence['-'] = 1
    precedence['/'] = precedence['*'] = 2

    tokens = s.split()
    num_stack = Stack()
    op_stack = Stack()

    for token in tokens:
        if is_digit(token):
            num_stack.push(int(token))
        else:
            if op_stack.isEmpty():
                op_stack.push(token)
            else:
                if precedence[op_stack.peek()] > precedence[token]:
                    top = op_stack.pop()
                    num2 = num_stack.pop()
                    num1 = num_stack.pop()
                    result = cal(top, num1, num2)
                    num_stack.push(result)
                op_stack.push(token) # anyway, we need to push current operator

    op_stack.traverse()
    num_stack.traverse()
#    pdb.set_trace() 
    
    while not op_stack.isEmpty():
        top = op_stack.pop()
        num2 = num_stack.pop()
        num1 = num_stack.pop()
        result = cal(top, num1, num2)
        num_stack.push(result)

    return num_stack.pop()

def is_digit(s):
    return s.replace('.','',1).isdigit()

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

math_exp1 = '34 + 17'
math_exp2 = '1 + 2 * 10'
math_exp3 = '2 * 3 + 10 / 5 + 100'
print(calculator(math_exp1))
print(calculator(math_exp2))
print(calculator(math_exp3))
