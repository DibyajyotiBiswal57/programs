print ("Calculate grades from your marks")
print ("[ \t90-100:A \t75-89:B \t50-74:C \t<50:Fail\t]")
a = int(input("\nPlease enter your marks: "))
if a>=90 and a<=100:
  print ("Your grade is A.")
elif a>=75 and a<90:
  print ("Your grade is B.")
elif a>=50 and a<75:
  print ("Your grade is C.")
elif a>=0 and a<50:
  print ("You have failed.")
else:
  print ("ERROR: Please enter marks between 0 to 100.")
