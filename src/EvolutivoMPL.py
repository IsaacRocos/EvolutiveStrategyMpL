'''
Created on 05/05/2015

@author: Isaac
'''
import random
import sys


class EvolutivoMPL(object):

    '''
    Constructor
    '''
    def __init__(self):
        self.sigma = 0.2
        self.exitos = 0
        self.CExplotar = 0.817
        self.CExplorar = 1.01
        self.numVar = 2
        self.nPadres = 10 
        self.nHijos = 5
        self.padres = []
        self.hijos = []
        self.MAX_ITER = 5000
        self.interInf = -5
        self.interSup = 5
        self.fracasos = 0

    def RUN(self):
        self.__init__()
        #print '|NUMERO DE VARIABLES(d):',self.numVar,'| SIGMA:',self.sigma,'| MAX_ITER:',self.MAX_ITER,'|'
        self.generaPoblacionInicial(self.interInf,self.interSup)
        print 'Ejecutando generaciones...'
        for generacion in range(self.MAX_ITER):
            self.generarHijos()
            
            #self.nuevaPoblacionSort()      #Generar poblacion usando ordenamiento y tomando mejores
            #self.nuevaPoblacionmatchRand() #Generar poblacion usando competencia aleatoria
            self.nuevaPoblacionmatchSec()   #Generar poblacion usando competencia entre mejores hijos y padres
            
            if(generacion!=0 and (generacion%(10*self.numVar))==0):
                #print "====|ACTUALIZANDO SIGMA|===="
                if (self.exitos == 0):
                    self.fracasos += 1
                if(self.fracasos >= ((20*self.MAX_ITER) / 100)):
                    self.sigma = 0.2
                    print '__SigmaReset__'
                    self.fracasos = 0
                else:
                    self.modificarSigma()
        print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
        print ">MEJORES INDIVIDUOS ENCONTRADOS>"
        print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
        self.imprimirIndividuos()
        
        
    #Generar padres y calcular su aptitud. La lista de padres se ordena al finalizar la creacion
    def generaPoblacionInicial(self,li,ls):
        for npadre in range(self.nPadres): 
            padre = []
            genotipo = []
            for var in range(self.numVar):
                genotipo.append(random.uniform(li,ls))
            apt = self.aptitud(genotipo)
            padre.append([apt])
            padre.append(genotipo)
            self.padres.append(padre)
        self.padres.sort()
        #print 'POBLACION INICIAL'
        #self.imprimirIndividuos()
            
    
    #Calcula la aptitud de un individuo. 
    def aptitud(self,individuo):
        fxsum = 0
        for gen in individuo:
            sxi = ((gen)**4) - (16*(gen)**2) + (5*(gen))
            fxsum = fxsum+sxi
        fx = 0.5 * fxsum
        return fx
    
    
    def generarHijos(self):
        self.hijos = []
        for nHijo in range(self.nHijos):
            hijo = []
            numeroPadre = random.randint(0,self.nPadres-1)
            #print 'LI ',self.padres[numeroPadre][1], len(self.padres[numeroPadre])
            
            genomahijo = self.mutar(self.padres[numeroPadre][1])
            
            aptHijo = self.aptitud(genomahijo)
            hijo.append([aptHijo])
            hijo.append(genomahijo)
            self.hijos.append(hijo)
        self.hijos.sort()


    def mutar(self,individuo):
        nuevoIndividuo = []
        secuenciaM = []
        #secuenciaM.append(random.uniform(-1,1))
        for i in range(self.numVar):
            valAleat = random.normalvariate(0,1)#dist normal - media cero y desviacion estandar 1
            secuenciaM.append(valAleat)
        unGen = 0
        for gen in individuo:
            genMut = gen + (self.sigma * secuenciaM[unGen])
            nuevoIndividuo.append(genMut)
            unGen +=1
        return nuevoIndividuo
    
    #Generar poblacion usando ordenamiento y tomando mejores
    def nuevaPoblacionSort(self):
        nuevaPob = []
        nuevaPob = self.padres + self.hijos
        nuevaPob.sort()
        nuevaPob = nuevaPob[0:10]
        for i in range(self.nHijos):
            if(self.padres[i][0] != nuevaPob[i][0]):
                self.exitos += 1
        self.padres=nuevaPob[:] 
    
    #Generar poblacion usando competencia aleatoria
    def nuevaPoblacionmatchRand(self):
        for hijo in self.hijos:
            aleatorio = random.randint(0,self.nPadres-1)
            padre = self.padres[aleatorio]
            if(hijo[0]<padre[0]):
                self.padres[aleatorio] = hijo
                self.exitos += 1
        self.padres = self.padres[0:10]
        self.padres.sort()
     
     
    #Generar poblacion usando competencia entre mejores hijos y padres           
    def nuevaPoblacionmatchSec(self):
        indice = 0
        for hijo in self.hijos:
            padre = self.padres[indice]
            if(hijo[0]<padre[0]):
                self.padres[indice] = hijo
                self.exitos += 1
            indice += 1
        #self.padres = self.padres[0:10]
        self.padres.sort()
    
    
    def modificarSigma(self):
        #ps = self.exitos / ((10.0)*self.numVar)
        ps = self.exitos / (self.numVar+0.0)
        if(ps > 0.2):
            self.sigma = self.sigma / self.CExplotar
            #print "[ps > 0.2]Sigma actualizada: ", self.sigma
        elif(ps<0.2):
            self.sigma = self.sigma * self.CExplorar
            #print "[ps < 0.2]Sigma actualizada: ", self.sigma
        self.exitos = 0    
    
        
    def imprimirIndividuos(self):
        cont = 0
        for individuo in self.padres:
            print cont,'] APT: ',individuo[0]
            print '    VAL: ',individuo[1]
            cont +=1
        
        

#chispaVida = EvolutivoMPL()
#chispaVida.RUN()
