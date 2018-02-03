from stackLib import stack
from bc import bc
pancake = stack()

pancake.push('w')
pancake.push('a')
pancake.push('t')
print("Testing push")
print(pancake.store)


print("testing Pop")

for i in range(len(pancake.store)+1):
	out = pancake.pop()
	if  (out[0]):	
		print("top is " + out[1])

print("Bracket Checker")

out = bc("([{}])))")
print out
