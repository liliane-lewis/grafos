# -*- coding: utf-8 -*-

class Aresta:
    def __init__(self, origem, destino, rotulo):
        self.origem = origem
        self.destino = destino
        self.rotulo = rotulo
    
    def getOrigem(self):
        return self.origem
    
    def getDestino(self):
        return self.destino

    def getRotulo(self):
        return self.rotulo

#Não precisou dessa classe
#class Nodo:
#    def __init__(self, valor):
#        self.valor = valor
#    
#    def getValor(self)
#        return self.valor

class Grafo:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        #cria a matriz de adjacencia tamanho X tamanho
        self.matrizAdj = [[None for x in range(tamanho)] for y in range(tamanho)]
        self.marcados = []
    
    def adicionarAresta(self, origem, destino, rotulo):
        aresta1 = Aresta(origem, destino, rotulo)
        aresta2 = Aresta(destino, origem, rotulo)
        self.matrizAdj[origem][destino] = aresta1
        self.matrizAdj[destino][origem] = aresta2

    #retorna None se não existir a aresta
    def getAresta(self, origem, destino):
        temp = self.matrizAdj[origem][destino]
        if(temp == 0):
            return None
        return temp

    def getArestaNodo(self, nodo):
        resposta = []
        for x in range(0, self.tamanho):
            temp = self.matrizAdj[nodo][x]
            if(temp != None):
                resposta.append(temp)
        return resposta

    def marcarNodo(self, nodo):
        if(not nodo in self.marcados):
            self.marcados.append(nodo)
    
    def desmarcarNodo(self, nodo):
        if(nodo in self.marcados):
            self.marcados.remove(nodo)

    def verificarNodoMarcado(self, nodo):
        return nodo in self.marcados

    def imprimir(self):
        sResposta = ""
        for n in range(0, self.tamanho):
            for a in self.getArestaNodo(n):
                sResposta = sResposta + "Aresta: " + str(a.getOrigem()) + " - " + str(a.getDestino()) + " = " + str(a.getRotulo()) + "\n"
        return sResposta
    
#temp = Grafo(5)
#temp.adicionarAresta(0,0,5)
#temp.adicionarAresta(1,1,5)
#temp.adicionarAresta(1,2,5)
#print(temp.imprimir())
#print(temp.verificarNodoMarcado(2))
#temp.marcarNodo(2)
#print(temp.verificarNodoMarcado(2))
#temp.desmarcarNodo(2)
#print(temp.verificarNodoMarcado(2))
#print(temp.getArestaNodo(2))