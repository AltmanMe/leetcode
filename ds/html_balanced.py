import re
from basic.stack import Stack


def check_html_balance(text):
    s = Stack()
    x = text.replace('<', ' <')
    y = x.replace('>', '> ')
    a = [w for w in y.split() if re.search('<\S+>', w)]
    b = [w for w in a if "/" not in w]
    c = [w for w in a if "/" in w]
    for w in text.split():
        if w in b:
            s.push(w)
        elif not s.isEmpty() and (w in c) and (w.replace('/', '') == s.peek()):
            s.pop()
    return s.isEmpty()

text = '''<html>
<head>
<title>
Example
</title>
</head>
<body>
<h1>Hello, world</h1>
</body>
</html>''' 

print(check_html_balance(text))
