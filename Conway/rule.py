def rule(val,box):

	sum = reduce(lambda x,y: x+y ,box);

	#for i in box:
	#	sum = sum + i
	
	if val == 1:
		if sum == 2 or sum == 3:
			return 1
		else:
			return 0
 
	else:
		if sum == 3:
			return 1
		else:
			return 0 
