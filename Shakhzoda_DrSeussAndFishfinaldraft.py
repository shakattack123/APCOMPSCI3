#Function to look at all coding instruction pt.2

def HelloWorld():
    print("Hello World")

#Function Call
    HelloWorld()

#+
def Add(input1,input2):
    print(input1+input2)

#Function Call

def question1():
    #Program to say how many fish there are
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

def question2():
    #Program to say who blue fish wants to go to
    ans2=input("Who does the blue fish wants to go to:")
    if ans2=="two fish":
       print("Correct")
    elif ans2=="Purple Fish":
       print("There is no purple")
       question2()
    elif ans2==("One Fish"):
       print("The answer in spanish is dos")
       question2()

    else:
       print("Please just re read the story")
       question2()
question2()

def question3():
    #What the fish were doing
    ans3=input("What was the red fish doing?:")
    if ans3==("eating the food"):
         print("Correct")
    elif ans3==("stealing the goods"):
         print("that's blue fish")
         question3()
    elif ans3==("swims away"):
         print("Thats two fish")
         question3()
    else:
         print("hint:it means comer in spanish")
         question3()
question3()

def question4():
    #Program explaning who else came while the fish were singing
    ans4=input("Who is itnroduced while the fish were singing along?:")
    if ans4=="Dr.Seuss":
       print("Yes!")
    elif ans4==("Purple fish"):
       print("Not in the story")
       question4()
    elif ans4==("Dr.McStuffins"):
       print("Hint:it's a doctor")
       question4()
    else:
       print("Hint:his name starts with an S")
       question4()
question4()

def question5():
    #Program explaining the conversation between blue fish and Dr.Seuss
    ans5=input("What does Dr.Seuss ask the blue fish?:")
    if ans5==("his name"):
       print("Good job!")
    elif ans5==("asks for his security number"):
       print("you're close, but it's not that personal")
       question5()
    elif ans5==("for his phone number"):
       print("it's not like that, it's more simple")
       question5()
    else:
       print("Hint:it starts with n and ends with e and it has four letters")
       question5()
question5()

def question6():
    #Program explaining the conversation between blue fish and Dr.Seuss
    ans6=input("What happens after?:")
    if ans6==("the blue fish tells him his name and swims away"):
       print("Good job!")
    elif ans6==("asks for his security number"):
       print("you're close, but it's not that personal")
       question6()
    elif ans6==("for his phone number"):
       print("it's not like that, it's more simple")
       question6()
    else:
       print("HOW DO YOU NOT KNOW THIS")
       question6()
question6()       

def question7():
    #Program asking what Dr.Seuss and the fish both hate
    ans7=input("What do Dr.Seuss and the fish both hate?:") 
    if ans7=="Fishing nets":
        print("Good, they're bad for the ocean")
    elif ans7==("pancakes"):
        print("dude, they LOVE pancakes")
        question7()
    elif ans7==("confetti"):
        print("um no")
        question7()
    else:
       print("Hint:they're bad for the ocean")
       question7()
question7()

def question8():
    # Program asking on what the fish want to do
    ans8=input("What do the fish want to do while swimming in the lake?:")
    if ans8==("bake"):
        print("Good job")
    elif ans8==("swim"):
        print("they already are swimming...")
        question8()
    elif ans8==("eat"):
        print("um i guess it's close but keep guessing")
        question8()
    else:
       print("Hint:it's a type of cooking")
       question8()
question8()

def question9():
    #Program asking the fish an odd thing they like
    ans9=input("what is an odd thing that they like?:")
    if ans9=="Confetti":
         print("That's odd, right?")
    elif ans9== "Milk":
         print("Wrong")
         question9()
    elif ans9==("pancakes"):
         print("that's not odd..")
         question9()  
    else:
        print("Hint: it has to do something with birthdays")
        question9()
question9()

def question10():
    #Program on who else makes the food besides Dr.Seuss and why
    ans10=input("Who else joins the fish on their baking:")
    if ans10=="Dr.Seuss":
       print("Good but I hope he knows how to cook")
    elif ans10==("Red fish"):
       print("Red fish is already there")
       question10()
    elif ans10==("dr.mcstuffins"):
       print("wrong")
       question10()
    else:
       print("hint:refer to question 3")
       question10()
question10()

def question11():
    #Program on what they do after baking
    ans11=input("What did they do after finishing their cooking?:")
    if ans=="sat near the lake and ate pancakes with milk":
      print("Correct!")
    elif ans11==("swam"):
        print("wrong")
        question11()
    elif ans11==("went to find fish nets"):
       print("wrong")
       question11()
    else:
       print("hint:it has something to do with food")
       question11()
question11()

 


