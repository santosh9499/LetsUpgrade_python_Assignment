print('=======================================')
print("\n")
print("QUESTION 1")
print("\n")
print('=======================================')
name = "jonathan"
surname = "wick"
print(name+" "+surname)
print(name.count('a'))
print(surname.find('k'))
print(name.isalpha())
x=surname.replace('w','k')
print(x)
print(name.capitalize()+" "+surname.capitalize())
print(name.index('a'))

print('=======================================')
print("\n")
print("QUESTION 2")
print("\n")
print('=======================================')
name = ["jonathan","wick",70,"Breaking Bad"]
print(name)
name.append(0.7)
print(name)
y= name.copy()
print(y)
c = name.count("wick")
print(c)
print(name.pop(3))
print(name)
name.remove(70)
print(name)


print('=======================================')
print("\n")
print("QUESTION 2")
print("\n")
print('=======================================')
sub = {"ds":"joshi","maths":"godbole","dbms":"joshi","history":"shete"}
print(sub)
sub.update({"maths":"Jadu"})
print(sub)
x=sub.values()
print(x)
sub.popitem()
print(sub)
x=sub.keys()
print(x)
sub.clear()
print(sub)

