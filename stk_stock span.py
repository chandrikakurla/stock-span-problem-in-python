#pushing element into stack
def push(stack,data):
    stack.append(data)
#checking for emptystack
def isEmpty(stack):
    if len(stack)==0:
        return True
    else:
        return False
#returns top element of stack
def peek(stack):
    if not isEmpty(stack):
        return stack[-1]
    else:
        return
#pops element from stack
def pop(stack):
    if not isEmpty(stack):
        stack.pop()
#function to find stock span using stack
def Stock_Span(price,span,n):
    #stack will store index of price
    stack=[]
    push(stack,0)
    #span of first element is always 1
    span[0]=1
    for i in range(1,n):
        while((not isEmpty(stack)) and price[peek(stack)]<price[i]):
            pop(stack)
        if(isEmpty(stack)):
            span[i]=i+1
        else:
            span[i]=i-peek(stack)
        push(stack,i)
if __name__=="__main__":
    price=[100, 80, 60, 70, 60, 75, 85]
    n=len(price)
    span=[0] *n
    Stock_Span(price,span,n)
    print(span)


