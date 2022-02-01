#Examples of each coding structure


#Statement-an intruction
print("hello") #example
    # Conditionals - (if/while)

# Variable - a named value that can change
varName = 0.1
x = 1.1
print(varName,x)

#Loop-repeated actions # for/while
for num in [7,12,4,5,6,24,0,-50]:
    new = num+7
    print(num,new)

# Function - a group of statements that execute when units are called
def function():
    #Program to say how many fish there are from my Adventure assigment
    ans1=input("How many fish were there:")
    if ans1=="4":
       print("There are four fish")
    elif ans1=="3":
       print("Hint:Add one more number")
       question1()
    elif ans1=="5":
       print("go down one")
       question1()
    else:
       print("Read my story again")
       question1()
question1()

# Comment - organizes and does not affect code

