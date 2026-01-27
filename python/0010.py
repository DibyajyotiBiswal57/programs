#Q10
print ("# Program to find out whether the angles are supplementary or complementary")
a1=int(input("Enter the first angle: "))
a2=int(input("Enter the second angle: "))

if a1+a2==180:
    print ("The angles are supplementary")
elif a1+a2==90:
    print ("The angles are complementary")
else:
    print ("The angles are neither complementary nor supplementary")
