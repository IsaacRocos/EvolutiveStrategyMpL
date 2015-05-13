'''
Created on 07/05/2015

@author: Isaac
'''
from EvolutivoMPL import EvolutivoMPL

class DeJong(EvolutivoMPL):
    '''
    classdocs
    '''

    def __init__(self):
        self.sigma = 0.2
        self.exitos = 0
        self.fracasos = 0
        self.CExplotar = 0.817
        self.CExplorar = 1.2
        self.numVar = 2
        self.nPadres = 10 
        self.nHijos = 5
        self.padres = []
        self.hijos = []
        self.MAX_ITER = 5000
        self.interInf = -65.536
        self.interSup = 65.536
        a1 = [-32.0,-16.0,0.0,16.0,32.0]*5
        a2 = [-32.0]*5 + [-16.0]*5 + [0.0]*5 + [16.0]*5 + [32.0]*5
        self.a = []
        self.a.append(a1)
        self.a.append(a2)
        #print self.a
    
    #@Override
    def aptitud(self,individuo):
        fxsum = 0
        for i in range(25):
            sxi =  1.0 / ( (i+1) + (individuo[0] - self.a[0][i])**6 + (individuo[1] - self.a[1][i])**6 )
            fxsum = fxsum+sxi
        fx = 1.0 / ( 0.002 + fxsum )
        return fx
    
    def info(self,iter):
        if(iter ==0):
            print '**********************************'
            print "| EJECUTANDO (1) DeJoungFunction |"
            print '**********************************'
            print '|NUMERO DE VARIABLES(d):',self.numVar,'| SIGMA:',self.sigma,'| MAX_ITER:',self.MAX_ITER,'|'
        else:
            print '========== Ejecucion',iter+1,'=========='

#prueba = DeJong()
#prueba.RUN()

