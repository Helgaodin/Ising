# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 20:57:43 2018

@author: Olga
"""

import random as rn
import numpy as np
import math
#Готовим решетку Изинга
L=16
J=1
nsteps=600000
beta=1
Ising=np.zeros((L,L))

def fillIsing():
    for i in range(L):
        for j in range(L):
            Ising[i][j]=2*rn.randint(0,1)-1
    return Ising
    
def justIsing():
    R=np.zeros((L,L,2))
    for i in range(L):
        for j in range(L):
            Ising[i][j]=2*rn.randint(0,1)-1
    #Теперь начнем динамику
    Energy_full = 0
    Magnet = 0
    for i in range(L):
        for j in range(L):
            Energy_full=Energy_full-J*\
            (Ising[i][j]*Ising[(i-1+L)%L][j]+Ising[i][j]*Ising[i][(j-1+L)%L])
            Magnet=Magnet+Ising[i][j]
    print(Energy_full)
    print(Magnet)
    f = open('Energy.txt', 'w')
    for step in range(nsteps):
        text = str(step) + '\t' + str(Energy_full) + '\t' + str(Magnet) + '\n'
        f.write(text)
        i=rn.randint(0,L-1) 
        j=rn.randint(0,L-1) 
        R[i][j][0] = R[i][j][0] + 1# попытка переворота
        E_oldspin=Ising[i][j]*\
        (Ising[(i+1+L)%L][j]+Ising[i][(j+1+L)%L]+Ising[(i-1+L)%L][j]+Ising[i][(j-1+L)%L])
        dE=-2*E_oldspin #прирост энергии
        #если уменьшилось
        if (dE<=0):
            Energy_full=Energy_full+dE
            Magnet=Magnet-2*Ising[i][j]
            Ising[i][j] = -Ising[i][j]
            R[i][j][1] = R[i][j][1] + 1# получилось перевернуть
        else:
            if(rn.random() < math.exp(-beta*dE)):#accepted
                Energy_full=Energy_full+dE
                Magnet=Magnet-2*Ising[i][j]
                Ising[i][j]=-Ising[i][j] 
                R[i][j][1] = R[i][j][1] + 1# получилось перевернуть
    R_aver = 0
    for i in range(L):
        for j in range(L):
            R_aver = R_aver+(R[i][j][1]/R[i][j][0])/(L*L)
    print(R_aver)     
    f.close()

def SwendsenWang():
    AdjectMat=np.zeros((L,L))
    #также треугольниками
    for i in range(L):
        for j in range(L):
            AdjectMat[i][j] = Ising[i][j]*Ising[(i-1+L)%L][j]
    
    
fillIsing()
justIsing()
        
import pylab
file = 'Energy.txt'
xE =[]
yE =[]
xM =[]
yM =[]
k=0
for line in open(file):
    k=k+1
    if (k>0):
        line = line.split('\t')
        xE.append(float(line[0]))
        yE.append(float(line[1]))
        yM.append(float(line[2]))
k
pylab.plot(xE, yE)
pylab.plot(xE, yM)
pylab.show()
