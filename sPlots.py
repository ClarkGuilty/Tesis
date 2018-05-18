# -*- coding: utf-8 -*-
"""


@author: Javier Alejandro Acevedo Barroso
Script de Python para la visualización de la simulación.

"""
import numpy as np
#import seaborn as sns
import matplotlib.pyplot as plt
import scipy as sc

dat = np.loadtxt("grid.dat")
plt.imshow(dat)
density = np.loadtxt("density.dat")
h = plt.figure()
plt.scatter(range(len(density)),density)
#constantes = np.loadtxt("constants.dat", usecols = 1)
#inF = np.loadtxt("inF.dat")
#outF = np.loadtxt("outF0.dat")
#outF1 = np.loadtxt("outF1.dat")
#oI = np.loadtxt("oI.dat")
#oR = np.loadtxt("oR.dat")
#acce = np.loadtxt("acce.dat")

#x = np.linspace(constantes[0], constantes[1], int(constantes[4]))  
#        
#plt.pcolormesh(dat)



#for i in range(int(constantes[6])):
#    dat = np.loadtxt("./datFiles/grid{:d}.dat".format(i))
#    plt.imshow(dat, extent=[constantes[0],constantes[1],constantes[2],constantes[3]]) #Es mucho más rápido imshow
#    #plt.pcolormesh(dat)
#    #plt.pcolor(dat) Nunca usar para grandes grillas	
#    plt.savefig("./images/phase{:d}.png".format(i))
#    plt.clf()
#    dens = np.loadtxt("./datFiles/density{:d}.dat".format(i))
#    plt.plot(x,dens)
#    plt.savefig("./images/density{:d}.png".format(i))
#    plt.clf()
#    potential = np.loadtxt("./datFiles/potential{:d}.dat".format(i))
#    plt.plot(x,potential)
#    plt.savefig("./images/potential{:d}.png".format(i))
#    plt.clf()
#    acce = np.loadtxt("./datFiles/acce{:d}.dat".format(i))
#    plt.plot(x,acce)
#    plt.savefig("./images/acce{:d}.png".format(i))
#    plt.clf()
    
#xf = np.linspace(0,1-1/constantes[4],int(constantes[4])) #Espacio de frecuencias senoidal
#plt.plot(x,density)
#plt.savefig("densidad.png")
#plt.figure()
#sns.distplot(density, kde=False, rug=True);

#plt.plot(x,inF)
#plt.plot(x,oR, color = 'black')
#plt.savefig("potencial.png")
#plt.scatter(x,density, color ='g')

#Verifica que el arreglo final luego de un loop sea igual al inicial.
#diffPorc = sum(np.abs(oR -density)/density)*100
#print diffPorc
#print "La diferencia porcentual entre el arreglo original y el arreglo un loop de fourier después es: "+ str(np.floor(diffPorc*10000)/10000)+"%"


#h = plt.figure()
#plt.plot(outF)
#plt.savefig("Fourier.png")
#h = plt.figure()
#plt.plot(x,oR)
#plt.savefig("Potencial.png")
#h = plt.figure()
#plt.plot(x,acce)
#plt.savefig("Aceleracion.png")

#simps(simps(z, y), x)