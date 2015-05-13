'''
Created on 09/05/2015

@author: Isaac
'''
from math import sin, cos
from EvolutivoMPL import EvolutivoMPL


class SchafferN4(EvolutivoMPL):

    def __init__(self):
        
        self.sigma = 0.2
        self.exitos = 0
        self.fracasos = 0
        self.CExplotar = 0.817
        self.CExplorar = 1.0005
        self.numVar = 2
        self.nPadres = 10 
        self.nHijos = 5
        self.padres = []
        self.hijos = []
        self.MAX_ITER = 5000
        self.interInf = -100
        self.interSup = 100
    
    #@Override
    def aptitud(self,individuo):
        x1 = individuo[0]
        x2 = individuo[1]
        fx = 0.5  +  (cos(sin(abs(x1**2 - x2**2)))  -  0.5) / ( 1.0 + (0.001*(x1**2 + x2**2)) )**2 
        return fx
    
    def info(self,iter):
        if(iter ==0):
            print '***********************************'
            print "|EJECUTANDO (4) SchafferFunctionN4|"
            print '***********************************'
        else:
            print '========== Ejecucion',iter+1,'=========='

    
#funSchafferN4 = SchafferN4()
#funSchafferN4.RUN() 
