#David Boyd
#CSC 500 - Project 1
#Binary to base10

#Below asks the user to input the information
Lm=int(input("Enter leftmost digit  (0 or 1): "))
snd=int(input("Enter the next digit (0 or 1: "))
trd=int(input("Enter the next digit (0 or 1: "))
fth=int(input("Enter the next digit (0 or 1: "))

#The conversion calulation will happen here
Lft=Lm*8
send=snd*4
third=trd*2
fourth=fth*1

lst=Lft+send+third+fourth

print("The value is " ,lst)
