import random

print(random.randint(5, 20))
# What did you see on line 1?
# The smallest number could see is 5, and the largest is 20 (both inclusive).

print(random.randrange(3, 10, 2))
# What did you see on line 2?
# The smallest number could see is 3, and the largest is 9.
# Could line 2 have produced a 4?
# No, because the step size is 2, starting at 3.

print(random.uniform(2.5, 5.5))
# What did you see on line 3?
# The smallest number could see is 2.5, and the largest is 5.5.

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100))
