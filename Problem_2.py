Name = input("Enter student name: ").capitalize()

Math = int(input("Enter Math marks: "))
Eng = int(input("Enter English marks: "))
Bio = int(input("Enter Biology marks: "))

Sum = Math + Eng + Bio

Average = Sum / 3

if  Average >= 80:
    Grade = "A+"
elif Average >= 70:
    Grade = "A"
elif Average >= 60:
    Grade = "A-"
elif Average >= 50:
    Grade = "B"
elif Average >= 40:
    Grade = "C"
else:
    Grade = "F"

print(f"Student Name: {Name}")
print(f"Average Marks: {Average}")
print(f"Final Grade: {Grade}")