'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
score=0

question1=float(input("what does 100-50 equal? "))
if question1>=51:
    print("no not exactly")
elif question1<=49:
    print("nope")
else:
    print("you right")
    score+=1

question2=input("what is the last name of our teacher?")
if question2.lower()=="hermon":
    print("yah")
    score+=1
else:
    print("nah")

question3=input("what is the largest number? A. 567 B. 678 C. 543 D. 679")
if question3.lower()=="d":
    print("nice one")
    score+=1
elif question3.lower()=="a":
    print("not even close buddy")
elif question3.lower()=="b":
    print("not even close buddy")
elif question3.lower()=="c":
    print("not even close buddy")
else:
    print("alright buddy you should rethink your life")

question4=float(input("how old is Aidan?"))
if question4==18:
    print("you must have a 500 iq")
    score+=1
else:
    print("wow what a horrible frined you are")
question5=input("where is the muffin man?")
if question5.lower()=="anywhere and everywhere":
    print("wow thats deep")
    score+=1
else:
    print("well who could have guessed anyways")

grade=((score/5)*100)

print(grade,"%")