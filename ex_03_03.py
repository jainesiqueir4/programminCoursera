# Write a program to prompt for a score between 0.0 and 1.0. If the score is
#out of range, print an error. If the score is between 0.0 and 1.0, print a
#grade using the following table:
sco = input("Enter Score: ")
score = float(sco)
if score < 0.0:
    print("Error!Me")
elif score > 1.0:
    print("Error!Ma")
elif score>=0.9:
    print("A")
elif score>=0.8:
    print("B")
elif score>=0.7:
    print("C")
elif score>=0.6:
    print("D")
else:
    print("F")
exit
