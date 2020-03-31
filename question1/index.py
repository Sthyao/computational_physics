import numpy as np
import matplotlib.pyplot as plt
import random

N = 101
T = 10000
m = 2
s = 2
result = np.zeros(T)
result[:5] =  [0,0,0,0,1]
def main(m):
    possible = np.zeros((2**m,m))
    strategy = np.zeros((2**(2**m),2**m))
    agentSrategy = np.zeros((N,s))
    agentSrategyPoint = np.zeros((N,s))
    agentNumber = np.zeros(T)


    for i in range(2**m):
        temp = i
        bintemp =  bin(temp).replace('0b','')
        temp1 = [int(j) for j in str(bintemp)]
        temp1 = np.array(temp1)
        num = abs(len(temp1) - m)
        for k in range(num):
            temp1 = np.insert(temp1,0,[0])
        possible[i] = temp1

    for i in range(2**(2**m)):
        temp = i
        bintemp =  bin(temp).replace('0b','')
        temp1 = [int(j) for j in str(bintemp)]
        temp1 = np.array(temp1)
        num = abs(len(temp1) - 2**m)
        for k in range(num):
            temp1 = np.insert(temp1,0,[0])
        strategy[i] = temp1

    for i in range(N):
        for j in range(s):
            agentSrategy[i][j] = random.randint(0,2**(2**m)-1)

    for i in range(m,T):
        temp = np.zeros(m)
        for j in range(m):
            temp[j] = result[i+j-m-1]
        for j in range(2**m):
            if (possible[j] == temp).all():
                possibleNum = j
        numberOfPeople = 0
        for j in range(N):
            resultTemp = np.zeros(s)
            for k in range(s):
                strategyNum = int(agentSrategy[j][k]) 
                #print(strategyNum)
                #print(possibleNum)
                resultTemp[k] = strategy[strategyNum][possibleNum]
            whoBetter = 0
            for k in range(s):
                if agentSrategyPoint[j][k] == agentSrategyPoint.max():
                    whoBetter = k
            #print(whoBetter)
            if resultTemp[whoBetter]:
                numberOfPeople = numberOfPeople+1
        
        agentNumber[i] = numberOfPeople
        if numberOfPeople <= 50:
            result[i] = 1

        for j in range(N):
            for k in range(s):
                if result[i] == resultTemp[k]:
                    agentSrategyPoint[k] = agentSrategyPoint[k] + 1
        return agentNumber.std()

resultMix = np.zeros(14)
for i in range(14):
    resultMix[i] =  main(i)

x = np.arange(14)
plt.plot(x,resultMix)
plt.show

