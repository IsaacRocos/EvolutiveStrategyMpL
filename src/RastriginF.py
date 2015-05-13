'''
Created on 08/05/2015

@author: Isaac
'''
from math import cos, pi as PI
from EvolutivoMPL import EvolutivoMPL


class Rastrigin(EvolutivoMPL):
    '''
    classdocs
    '''

    def __init__(self):
        self.sigma = 0.2
        self.exitos = 0
        self.fracasos = 0
        self.CExplotar = 0.817
        self.CExplorar = 1.02
        self.numVar = 4
        self.nPadres = 10 
        self.nHijos = 5
        self.padres = []
        self.hijos = []
        self.MAX_ITER = 5000
        self.interInf = -5.12
        self.interSup = 5.12
    
    #@Override
    def aptitud(self,individuo):
        fxsum = 0
        for i in range(self.numVar):
            xi = individuo[i]
            sxi =  (xi**2) - 10*cos(2*PI*xi)
            fxsum = fxsum+sxi
        fx = 10*self.numVar + fxsum
        return fx

    def info(self,iter):
        if(iter==0):
            print '**********************************'
            print "|EJECUTANDO (2) RastriginFunction|"
            print '**********************************'
        else:
            print '========== Ejecucion',iter+1,'=========='

        
#prueba = Rastrigin()
#prueba.RUN()
