from basic.stack import Stack

def par_checker(s):
    """
    s: string
    """
    
    stack_ = Stack()
    balanced = True
    for idx, char in enumerate(s):
        if balanced:
            if char in '({[':
                stack_.push(char)
            else:
                if stack_.isEmpty():
                    balanced = False
                else:
                    top = stack_.pop()
                    if not par_match(top, char):
                        balanced = False
        else:
            break

    if balanced and stack_.isEmpty():
        return True
    else:
        return False

def par_match(c1, c2):
    left = '([{'
    right = ')]}'
    return left.index(c1) == right.index(c2)

print(par_checker('((()))'))
print(par_checker('(()))'))
print(par_checker('{{([][])}()}'))
print(par_checker('[{()]'))
