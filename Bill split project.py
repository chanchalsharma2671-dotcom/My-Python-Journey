#Bill split converter
#1.take input from user that how much the bill and how many freinds
Bill = float(input("Enter your total bill amount :"))
Freinds = float(input("How many freinds are you? :"))
#2.Make a formula using variable and arithmetic opreator
Split = float(Bill/Freinds)
#3.print the splited value
print("Each freind give",Split)
# 4.print the type of the Split
print(type(Split))