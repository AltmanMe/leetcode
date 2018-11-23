from basic.stack import Stack

"""
If the token is an operand, append it to the end of the output list.
If the token is a left parenthesis, push it on the opstack.
If the token is a right parenthesis, pop the opstack until the corresponding left 
    parenthesis is removed. Append each operator to the end of the output list.
If the token is an operator, *, /, +, or -, push it on the opstack. 
    However, first remove any operators already on the opstack 
        that have higher or equal precedence and append them to the output list.
"""

def infix_postfix(s):
    """
    s: infix expression: A + B * C
    """
    precedence = dict()
    precedence['('] = 1
    precedence['+'] = precedence['-'] = 2
    precedence['/'] = precedence['*'] = 3
    valid_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    op = Stack()
    postfix_list = list()
    tokens = s.split()

    for token in tokens:
        if token in valid_list:
            postfix_list.append(token)
        elif token == '(':
            op.push(token)
        elif token == ')':
            top = op.pop()
            while top != '(':
                postfix_list.append(top)
                top = op.pop()
        else:
            while (not op.isEmpty()) and \
                    (precedence[op.peek()] >= precedence[token]):
                postfix_list.append(op.pop())
            op.push(token)

    while not op.isEmpty():
        postfix_list.append(op.pop())
    return ''.join(postfix_list)

print(infix_postfix("A * B + C * D"))
print(infix_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
