#Recently, Chef visited his doctor.
#The doctor advised Chef to drink at least 
#2000 ml of water each day.
#Chef drank X ml of water today.Determine if Chef followed the doctor's advice or not.

#sample input
# 3           #sample output
#2999         # yes
#1450         # no
#2000         # yes



T = int(input())
for i in range(T):
    X=int(input())
    if (X >= 2000):
        print("yes")
    else:
        print("no")
