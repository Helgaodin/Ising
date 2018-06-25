import random as rn
import numpy as np
#Готовим решетку Изинга
L=16
Ising=np.zeros((L,L))
for i in range(L):
    for j in range(L):
        Ising[i][j]=2*rn.randint(0,1)-1
#Теперь начнем динамику
Energy_full = 0
for i in range(L):
    for j in range(L):
        Energy_full=Energy_full-J*\
        (Ising[i][j]*Ising[(i-1+L)%L][j]+Ising[i][j]*Ising[i][(j-1+L)%L])
print(Energy_full)
for step in range(nsteps):
    f = open('Energy.txt', 'a')
    text = str(step) + '\t' + str(Energy_full) + '\n'
    f.write(text)
    f.close()
    i=rn.randint(0,L-1) 
    j=rn.randint(0,L-1) 
    E_oldspin=Ising[i][j]* \
    (Ising[(i+1+L)%L][j]+Ising[i][(j+1+L)%L]+Ising[(i-1+L)%L][j]+Ising[i][(j-1+L)%L])
    dE=2*E_oldspin
    #если уменьшилось
    if (dE>0):
        Energy_full=Energy_full-dE
        Ising[i][j] = -Ising[i][j]
    else:
        if(rn.random() < math.exp(-beta*dE)):#accepted
            Energy_full=Energy_full-dE
            Ising[i][j]=-Ising[i][j]           
        
import pylab
file = 'Energy - копия.txt'
x =[]
y =[]
k=0
for line in open(file):
    k=k+1
    line = line.split('\t')
    x.append(float(line[0]))
    y.append(float(line[1]))
k
pylab.plot(x, y)
pylab.show()
