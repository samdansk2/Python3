#Input Format
#The first line of input will contain a single integer T, denoting the number of test cases.
#Each test case contains two space-separated integers 
#X and Y — the numbers Chef and Chefina got on their respective dice.
#Output Format
#For each test case, output on a new line, YES, if the turn was good and NO otherwise.
#Each character of the output may be printed in either uppercase or lowercase. That is,
#the strings NO, no, nO, and No will be treated as equivalent.

#sample input           #sample output
#4                      
#1 4                    no
#3 4                    yes
#4 2                    no
#2 6                    yes


T=int(input())
for i in range(T):
    X,Y=map(int,input().split())
    if( X+Y > 6 ):
        print("yes")
    else:
        print("no")

        
