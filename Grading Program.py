semgrade=int(input("semgrade:"))
finalexam=int(input("finalexam:"))
examworth=int(input("examworth:"))
print(((100-examworth)*semgrade+(examworth*finalexam))/100,"%")