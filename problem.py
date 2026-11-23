# what is the output of the following code ? write iterations.
x = 0
while x < 10:
  if x % 2 == 0:
    x += 3
  else:
    x += 1
print(x,end="")
'''Iterations
Initially, x = 0.
Iteration
x < 10
Condition x % 2 == 0
Update to x
1
True (0 < 10)
True (even)
0 + 3 = 3
2
True (3 < 10)
False (odd)
3 + 1 = 4
3
True (4 < 10)
True (even)
4 + 3 = 7
4
True (7 < 10)
False (odd)
7 + 1 = 8
5
True (8 < 10)
True (even)
8 + 3 = 11
6
False (11 < 10)
Loop stops
output:11 '''
print("""This is a multiline commments let's check this line what will be print""")
output:This is a multiline commments let's check this line what will be print
#Scenario 2: The Smart Cargo Inventory (Using while loops and continue)
#The Goal: Practice managing a loop variable while using continue inside a while loop without causing an infinite loop. 
 #• Scenario: A factory conveyor belt moves 10 boxes sequentially, labeled 1 to 10. However, boxes 4 and 7 fail the quality check. The robot arm needs to scan all boxes but must skip processing the broken ones.
  #• The Task: Use a while loop to count from box 1 to 10. If the current box number is 4 or 7, use continue to skip processing it. 
