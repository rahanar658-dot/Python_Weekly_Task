name=str(input("Enter a name:"))
mark1=int(input("Mark for subject 1:"))
mark2=int(input("Mark for subject 2:"))
mark3=int(input("Mark for subject 3:"))
total=mark1+mark2+mark3
average=total/3
print("Total marks:",total)
print("Average:",average)
if average>90-100:
    print(" Grade A")
elif average>80-89:
    print(" Grade B")
elif average>70-79:
    print("Grade C")
elif average>60-69:
    print("Grade D")
else:
    print("Grade E ")

