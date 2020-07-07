def valid_parentheses(string):
    open_p, close_p = 0,0
    ret = True
    for i in string: 
        if i == '(': open_p +=1
        elif i == ')' : close_p +=1
        if close_p > open_p: ret = False
    if close_p != open_p: ret = False
    return ret



print(valid_parentheses('(pewp'))
