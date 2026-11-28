#1. find the largest number in the list without using max function.
n = [59, 21, 44, 34, 5, 70]
for i in n:
 if [i+1] > n:
  print("largest number:", i)
 else:
   print("smallest number:", i)
 output:largest number: 59
smallest number: 21
smallest number: 44
smallest number: 34
smallest number: 5
largest number: 70
   largest = n[0]
 for i in n:
   if i > largest:
     largest = i 
print("largest number:", largest)
output: largest number: 70

#2. find the common number from 2 lists.
n = [59, 21, 44, 34, 5, 70, 70, 23] 
n1 = [23, 66, 21, 59, 44, 70, 34]
num = n[0]
num = n1[0]
for i in n:
  if i in n1:
   print("common number:",i)
output:common number: 59
common number: 21
common number: 44
common number: 34
common number: 70
common number: 70
common number: 23
   
   
#3. Find the number of occurrences of a given number without using inbuilt functions
