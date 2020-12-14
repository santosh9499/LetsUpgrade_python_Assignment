print('=======================================')
print("\n")
print('Student report card')
print("\n")
print('=======================================')
print("\n")
stud_name=input('Please enter Name :')
stud_age=int(input('Pleae enter Age :'))
english_marks=int(input('Please enter English marks :'))
maths_marks=int(input('Please enter Maths marks :'))
science_marks=int(input('Please enter Science marks :'))

stud_total_marks = maths_marks + science_marks + english_marks
stud_percentage = round(stud_total_marks/300 * 100,2)


if(stud_percentage>=75): 
  print('Distinction')
elif stud_percentage >=60 and  stud_percentage< 75:
  print('First Class')
elif (stud_percentage>35 and stud_percentage<60):
  print('Second class')
else:
  print('Fail')
print('=======================================')
print("\n")


print('=======================================')
print("\n")
print("QUESTION 2")
print("\n")
print('=======================================')
start = 1
end = 1000
 
for i in range(start,end):
  if i>1:
    for j in range(2,i):
        if(i % j==0):
            break
    else:
        print(i)
print('=======================================')
print("\n")

print('=======================================')
print("\n")
print("QUESTION 3")
print("\n")
print('=======================================')
for i in range(1,11):
    for j in range(1,11):
     print(i, 'x', j, '=', i*j)
print('=======================================')


print('=======================================')
print("\n")
print('=======================================')
n=int(input("Enter maximun range for  prime numbers:"))

x=int(input("Enter how many prime numbers to print:"))

c=0

f=2

while(c<x):

   if n>=2:

       for i in range(2,f):

           if f%i==0:

               break

       else:

           if f>=n:

               break

           else:

               print(f)

               c+=1      

   f+=1        
print('=======================================')
