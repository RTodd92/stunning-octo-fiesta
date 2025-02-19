import matplotlib.pyplot as plt

'''
The Collatz Conjecture states that repeating two simple arithmatic operations will eventually transform every positive integer
into 1, such that:

f(n) = {n/2     if n = 0 (mod 2), 
        3n + 1  if n = 1 (mod 2)}

If the number is even, divide it by two.
If the number is odd, triple it and add one.

Form a sequence by performing this operation repeatedly, taking the result at each step as the input for the next.

This process will eventually reach the number 1, regarless of which positive integer is chosen initially.
'''

# Prompt the user for a starting integer
userInput = int(input("Enter any positive integer: "))
input = userInput

# List to hold each step
steps = []

# Add starting integer as first step
steps.append(input)

while input != 1:
	
	if input % 2 == 0:
		input = (input / 2)
		steps.append(input)
	
	elif input % 2 == 1:
		input = (3 * input + 1)
		steps.append(input)
	
	elif input == 1:
		break

print(f'Total steps to resolve to 1: ' + str(len(steps)))
print(steps)

plt.xlim(0, len(steps) -1)
plt.ylim(0, max(steps))
plt.plot(steps)
plt.show()