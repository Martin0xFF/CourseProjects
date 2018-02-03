from stackLib import stack

def bc(Strin):
	count = 0
	theStack = stack()
	for i in Strin:
		if (i == '{') or (i=='[') or(i=='('):
			theStack.push(i)

		if i == '}' or i == ']' or i == ')':
			out = theStack.pop()
			topOfStack = out[1]
			


			if (topOfStack == '{') and (i == '}'):
 				None
			elif (topOfStack == '[') and (i == ']'):			
				None
			elif (topOfStack == '(') and (i == ')'):
				None
			else:
				theStack.push(topOfStack)
				return[False,count]	
	
		count = count + 1
	
	if theStack.numItems == 0 :
		return [True,"I Don't practice Santeria..."]
	else:
		return [False,count]
