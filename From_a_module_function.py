#from a module 
import math
import random
print(math.sqrt(49))
print(math.factorial(5))
print(math.ceil(4.34))
print(math.floor(4.67))
print(random.random())
output:7.0
120
5
4
0.6965436056812466
#write school_name() that print your school or college name.call it 3 times.
def school_name():
    print("nitttr")
school_name()
output: nitttr
#Write square(n) that square of n.call it with 4 and 9.
def square(n):
    print(n*n)
square(4)
square(9)
output: 16
81
#write is_even(n) that print Even or odd. call it with 8 and 15.
def is_even(n):
  if n%2 == 0:
    print(n, "is even")
  else:
    print(n,"is odd")
is_even(8)
is_even(15)
output: 8 is even
15 is odd
