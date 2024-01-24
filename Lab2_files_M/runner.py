#This program tests if a runner has covered more distance since the 
#last time they ran.
previousDist = float(input("Please enter the previous distance covered by the athlete: "))
currentDist = float(input("Please enter the current distance covered by the athlete: "))
improvement = currentDist - previousDist

#print(               )
if currentDist != 15 and previousDist == 10 :
    print("Try harder to improve.")
print( "Try to improve." )
