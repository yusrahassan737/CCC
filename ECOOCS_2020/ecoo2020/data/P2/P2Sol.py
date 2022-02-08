# Name: Yusra Hassan
# Date: March 25-29, 2021
# Description: Solution to ECOO 2020 P2 (Find lowest cost to pay given prices and quantities of items at different stores) WITHOUT FILE HANDLING - does not yet work for data.in
# Purpose: Practice for ECOO

T = int(input())
# Loop for each test case
for i in range(T):
    # Variables
    itmNames = []
    itmPrices = []
    itmNums = []
    itmsWanted = []
    numWanted = []
    
    N = int(input())
    # Loop for each number of stores
    for j in range(N):
        M = int(input())
        # Loop for each number of different items sold
        for k in range(M):
            # Record the item's name, price and quantity in stock
            storeInfo = input()
            S, P, Q = storeInfo.split()
            itmNames.append(S)
            itmPrices.append(int(P))
            itmNums.append(int(Q))
    
    K = int(input())
    # Loop for each item she wants and how many of it
    for i in range(K):
        wantedInfo = input()
        itmsWanted.append(wantedInfo[:wantedInfo.find(" ")])
        numWanted.append(int(wantedInfo[wantedInfo.find(" ") + 1:]))
    
    costs = []
    total = 0
    for i in range(len(itmsWanted)):
        matches = []
        
        # find all instances of this item in stores
        for j in range(len(itmNames)):
            if itmNames[j] == itmsWanted[i]:
                matches.append(j)
        
        # create list with just that item's prices and sort from least to greatest
        matchPrices = []
        matchNums = []
        for j in matches:
            matchPrices.append(itmPrices[j])
            matchNums.append(itmNums[j])
        comparedPrices = sorted(matchPrices)
        
        # Find the price in the price list and its corresponding quantity, then record the price * quantity as a cost
        for j in comparedPrices:
            cheapestNum = matchNums[matchPrices.index(j)]
            if numWanted[i] > cheapestNum:
                costs.append(cheapestNum * j)
                numWanted[i] -= cheapestNum
            else:
                costs.append(numWanted[i] * j)
                numWanted[i] = 0
                break
               
    # Add up total lowest cost of items for the test case and print
    for i in costs:
        total += i
    print(total)
