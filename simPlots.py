# -*- coding: utf-8 -*-
"""


@author: Javier Alejandro Acevedo Barroso
Script de Python para la visualización de la simulación.

"""
import numpy as np
#import seaborn as sns
import matplotlib.pyplot as plt
import scipy as sc
import matplotlib.ticker as ticker
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

#plt.rcParams['image.cmap'] = 'PuBu'
#plt.rcParams['image.cmap'] = 'YlGnBu'
plt.rcParams['image.cmap'] = 'plasma'
rcParams.update({'font.size': 11})
plt.rcParams['image.cmap'] = 'plasma'
fsize = 16


JEANS = -137
GAUSS = -127

dat = np.loadtxt("./datFiles/grid0.dat").T
#density = np.loadtxt("density.dat")
constantes = np.loadtxt("constants.dat", usecols = 1)
TAU = int(constantes[8])
#inF = np.loadtxt("inF.dat")
#outF = np.loadtxt("outF0.dat")
#outF1 = np.loadtxt("outF1.dat")
#oI = np.loadtxt("oI.dat")
#oR = np.loadtxt("oR.dat")
#acce = np.loadtxt("acce.dat")

def fmt(x, pos):
    a, b = '{:.1e}'.format(x).split('e')
    b = int(b)
    return r'${} \times 10^{{{}}}$'.format(a, b)

x = np.linspace(constantes[0], constantes[1], int(constantes[4]))  
#        
figu = plt.gcf()
#figu.set_size_inches(18.5, 10.5)
#figu.set_dpi(300)
dpII = 300
velUnit = 1183 #m/s
estUnit = 50 #kpc

for i in range(int(constantes[6])):
    dat = np.loadtxt("./datFiles/grid{:d}.dat".format(i)).T
    dat = dat#/np.max(dat)/7
    plt.imshow(dat, extent=[constantes[0],constantes[1],constantes[2],constantes[3]], interpolation='nearest', aspect='auto') #Es mucho más rápido imshow	
    plt.yticks(plt.yticks()[0], [str(np.round(t*velUnit)) for t in plt.yticks()[0]]) 
    plt.ylabel("Velocity [km/s]",fontsize=fsize)
    plt.xticks(plt.xticks()[0], [str(t*estUnit) for t in plt.xticks()[0]])
    plt.xlabel("Position [kpc]",fontsize=fsize)
    if(constantes[7] == JEANS):
        plt.title("Jeans Instability $\\tau =$ {:d}".format(TAU),fontsize=fsize)
    elif(constantes[7] == GAUSS):
        plt.title("Gaussian Initialization $\\tau =$ {:d}".format(TAU),fontsize=fsize)
        #plt.title('Densidad de probabilidad ')
        #plt.title("Inicialización del espacio de fase")
        
    #plt.clim(0,1.35e5)
    plt.clim(0,1e5)
    cbar = plt.colorbar(format=ticker.FuncFormatter(fmt))
    cbar.set_label("Mass density [$M_{\odot}$ / kpc  $\\frac{km}{s}$]",fontsize=fsize)
    #plt.colorbar()
    #cbar.set_label("Probability Density")
    plt.savefig("./images/phase{:d}.png".format(i), dpi = dpII)
    plt.clf()
    
    
    dens = np.loadtxt("./datFiles/density{:d}.dat".format(i))
    
    plt.plot(x,dens)
    plt.xticks(plt.xticks()[0], [str(t*estUnit) for t in plt.xticks()[0]])
    plt.xlabel("Position [kpc]",fontsize=fsize)
    plt.ylabel("Linear Density $M_{\odot}$/kpc",fontsize=fsize)
    plt.title("Density $\\tau =$ {:d}".format(TAU),fontsize=fsize)
    plt.ylim(-0.75e9,6e10)   

    plt.savefig("./images/density{:d}.png".format(i), dpi = dpII)
    plt.clf()
    
    
#    potential = np.loadtxt("./datFiles/potential{:d}.dat".format(i))
#    plt.plot(x,potential)
#    plt.ylabel("Potential [J /kg]")
#    plt.title("Potential $\\tau =$ {:d}".format(TAU))
#    #plt.ylim(-6.6e10,-5.8e10)
#    plt.xticks(plt.xticks()[0], [str(t*estUnit) for t in plt.xticks()[0]])
#    plt.xlabel("Position [kpc]")
#    plt.savefig("./images/potential{:d}.png".format(i), dpi = dpII)
#    plt.clf()
#    
#    
#    acce = np.loadtxt("./datFiles/acce{:d}.dat".format(i))
#    plt.plot(x,acce)
#    plt.ylabel("Acceleration [kpc / $(mYears)^2$]")
#    plt.title("Acceleration $\\tau =$ {:d}".format(TAU))
#    #plt.yticks(plt.yticks()[0], [str(t*2754463327) for t in plt.yticks()[0]])
#    plt.xticks(plt.xticks()[0], [str(t*estUnit) for t in plt.xticks()[0]])
#    
#    plt.ylim(-0.0037,0.0037)
#    
#    plt.xlabel(" [kpc]")
#    plt.savefig("./images/acce{:d}.png".format(i), dpi = dpII)
#    plt.clf()
    

