#Creating a function

def printtwice():
    print("hello")
    print("hello")

#Creating new function inside a function that we've made

def print4times():
    printtwice()
    printtwice()

print4times()

#Creating a function with x (if x is number, defined as an integer, and if it word defined as a string)

x = 2
def multiplyby2(x):
    x=x*2
    return x
result= multiplyby2(x)

print(result)

#Creating a function with desired input

z = input("Please enter a number to multiply !") #automaticaly defined as a string. Wether it is number or words
def multiplyby2(z):
    z=z*2
    return z
result= multiplyby2(z)
print(result)

#The input is considered as a STRING !

#Change the type to integer to begin mathematical multiplication

y = input("Please enter a number to multiply !")
y = int(y)
def multiplyby2(y):
    y=y*2
    return y
result= multiplyby2(y)
print(result)
