#CostOfCall_sol.py
def main():
    distance = float(input("Please enter the distance (kms) for the call: "))
    minutes = int(input("Please enter the time (minutes) of the call: "))
    if distance <= 99:
        callCost = computeCost99k(minutes)
    elif distance <= 199:
        callCost = computeCost199k(minutes)
    else:
        callCost = computeCostOther(minutes)
    printCost(callCost)

def computeCost99k(m):
    if m <= 5:
        cost = m*.12
    else:
        cost = (m - 5)*.1 + 5*.12
    return cost

def computeCost199k(m):
    if m <= 5:
        cost = m*.15
    else:
        cost = (m - 5)*.13 + 5*.15
    return cost

def computeCostOther(m):
    return m*.18

def printCost(c):
    print("The cost of call is: $%.2f" % c)

main()