digit = ('1','2','3','4','5','6','7','8','9','0')
op = ('+', '-', '*', '/', '^')

def Ncheck(numm):
    return all(char in digit for char in numm)

def prior(oper):
    if oper in ('+', '-'):
        return 0
    elif oper in ('*','/'):
        return 1
    elif oper == '^':
        return 2 
    
def Response(input):
    stack = []
    output = []
    
    for token in input.split(' '):
        if Ncheck(token):
            output.append(token)
            continue
            
        if token == '(':
            stack.append(token)
            continue
        
        if token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
            continue    
        
        if token in op:
            opPrior = prior(token)
            while stack and stack[-1] in op and prior(stack[-1]) >= opPrior:
                output.append(stack.pop())
            stack.append(token)
            
    while stack:
        output.append(stack.pop())
        
    return output

def mat(respons):
    stack = []
    
    for token in respons:
        if Ncheck(token):
            stack.append(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = 0
            
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2
            elif token == '^':
                result = operand1 ** operand2
                
            stack.append(result)
            
    return stack
    
    
if __name__ == '__main__':
    input = "3 + 4 * 2 / ( 1 - 5 ) ^ 2"
    respons = Response(input)
    
    print("Reverse: ", respons)
    print("Result: ", mat(respons))
                


        