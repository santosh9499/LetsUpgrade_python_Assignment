# Question 1
print("=========================================")
print("\n")
print("QUESTION 1")
print("File Operations")
print("\n")
print("=========================================")
print("\n")
myFile = open("Hello.txt",'w')
myFile.write("i Love myself and Letsupgrade")
myFile.close()

myFile = open("Hello.txt",'r')
content = myFile.read()
myFile.close()
print(content)

myFile = open("Hello.txt",'a')

myFile.write(" & I also love Emma Watson")

myFile.close()

myFile = open("Hello.txt",'r')
print(myFile.read())
myFile.close()

#Question2
print("=========================================")
print("\n")
print("QUESTION 2")
print("FACTORIAL OF A NUMBER")
print("\n")
print("=========================================")
print("\n")

num = int(input("Enter the number: "))

factorial = 1

if num < 0:
   print("No negative numbers allowed")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
   print("=========================================")
   print("\n")
