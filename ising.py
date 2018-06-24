import random as rn
import numpy as np
#Готовим решетку Изинга
L=16
Ising=np.zeros((L,L))
for i in range(L):
    for j in range(L):
        Ising[i][j]=2*rn.randint(0,1)-1
#Теперь начнем динамику
