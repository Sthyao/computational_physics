#One dimensional cellular machine
#S.wofram rules No.6

import numpy as np
import matplotlib.pyplot as plt
import copy

rules = np.array([0,1,1,0,0,0,0,0])
conditions = ['000','001','010','011','100','101','110','111']

def main(N):
    cells = np.zeros(N)
    cellsAll = np.zeros((50,N))
    cells[9]=cells[23]=cells[24]=cells[25]=cells[40] = 1
    for t in range(50):
        for i in range(50):
            if i == 0:
                string = str(int(cells[N-1]))+str(int(cells[0]))+str(int(cells[1]))
            elif i == N-1:
                string = str(int(cells[N-2]))+str(int(cells[N-1]))+str(int(cells[0]))
            else:
                string = str(int(cells[i-1]))+str(int(cells[i]))+str(int(cells[i+1]))
            #print(string)
            for j in range(7):
                
                if string == conditions[j]:
                    cells[i] = copy.deepcopy(rules[j])

        cellsAll[t] = cells
    return(cellsAll)

N = 50
cellsAll = main(N)
nArray = np.arange(N)
for t in range(50):
    for i in range(50):
        if cellsAll[t][i] == 0:
            cellsAll[t][i] = None
    plt.scatter(nArray,cellsAll[t]+t,marker=',',s = 40,c = 'k')

plt.ylabel('t')
plt.xlabel('N')
plt.title("One Dimensional Cellular Machine")
plt.show()
