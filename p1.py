def f(expression):
    stack=[]
    right=0
    left=0
    stra=f'{expression}'
    values=stra.split()
    for val in values:
        if val not in ['+','-','/','*','^']:
            stack.append(int(val))
        else:
            right=stack.pop()
            left=stack.pop()
            print(left,val,right,end=" ")
            if val=='+':
                stack.append(left+right)
            elif val=='-':
                stack.append(left-right)
            elif val=='*':
                stack.append(left*right)
            elif val=='/':
                stack.append(left/right)
            elif val=='^':
                stack.append(left**right)
            print('=',stack[-1])
    return stack.pop()
if __name__=='__main__':
    print(f('2 3 +'))
    print(f('2 6 + 4 5 - +'))
    print(f('11 7 + 15 - 14 +'))