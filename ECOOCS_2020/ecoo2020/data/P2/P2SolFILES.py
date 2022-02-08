# Name: Yusra Hassan
# Date: March 29 - April 30, 2021
# Description: Solution to ECOO 2020 P2 (Find lowest cost to pay given prices and quantities of items at different stores) WITH FILE HANDLING
# Purpose: Practice for ECOO

openFile = open("data.in", "r")

# Main loops to read file and calculate lowest cost
## Num Test Cases
T = int(openFile.readline())
for i in range(T):
    ## Variables
    itmNames = []
    itmPrices = []
    itmNums = []
    itmsWanted = []
    numWanted = []
    costs = []
    total = 0
    
    ## Num Stores
    N = int(openFile.readline())
    for j in range(N):
        ## Num diff items in the store
        M = int(openFile.readline())
        for k in range(M):
            ## Item Names, Prices and Quantities In Stock
            storeInfo = openFile.readline()
            S, P, Q = storeInfo.split()
            itmNames.append(S)
            itmPrices.append(int(P))
            itmNums.append(int(Q))
    
    ## Num items wanted
    K = int(openFile.readline())
    for j in range(K):
        ## Item names, Quantity wanted of each
        wantedInfo = openFile.readline()
        itmsWanted.append(wantedInfo[:wantedInfo.find(" ")])
        numWanted.append(int(wantedInfo[wantedInfo.find(" ") + 1:]))
    
    # Get lowest prices for items and append to costs
    for j in range(len(itmsWanted)):
        matches = []
        matchPrices = []
        matchNums = []        
        
        # find all instances of this item in stores
        for k in range(len(itmNames)):
            if itmNames[k] == itmsWanted[j]:
                matches.append(k)
        
        # create list with just that item's prices and sort from least to greatest
        for k in matches:
            matchPrices.append(itmPrices[k])
            matchNums.append(itmNums[k])
        comparedPrices = sorted(matchPrices)
        
        # Find the price in the price list and its corresponding quantity, then record the price * quantity as a cost
        for k in comparedPrices:
            cheapestNum = matchNums[matchPrices.index(k)]
            if numWanted[j] > cheapestNum:
                costs.append(cheapestNum * k)
                numWanted[j] -= cheapestNum
                matchPrices[matchPrices.index(k)] = 0
            else:
                costs.append(numWanted[j] * k)
                numWanted[j] = 0
                break
               
    # Add up total lowest cost of items for the test case and print
    for j in costs:
        total += j

openFile.close()
