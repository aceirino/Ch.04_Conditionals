grade=float(input("what is your grade?"))
test=float(input("what will you get on the test?"))
worth=float(input("what is the test worth?"))

worth=worth/100
overall=test*worth+grade*(1-worth)
letter=""

if overall>=100 and worth==0:
    letter="A+ you are a lucky guesser"
elif overall>=90:
    letter="A"
elif overall>=80:
    letter="B"
elif overall>=70:
    letter="C"
elif overall>=60:
    letter="D"
else:
    letter="F please transfer to johnston!"

print("your overall grade is...",overall,"%", letter)