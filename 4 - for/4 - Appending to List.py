import random
n=int(input("Enter how many number "))
print("Enter", n , "numbers ")
num = []
for i in range(0, n):
    num.append(random.randint(0,100))


print ("-"*60)
print("The Number == > ", num)
print ("-"*60)
