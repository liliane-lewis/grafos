# -*- coding: utf-8 -*-

import sys, os, re
#import msvcrt 
#import copy


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


#######################################################
def le_arquivo():
    if len(sys.argv) == 1:
        nome_arq = input('Informe o nome do arquivo a ser usado\n')
    else:
        nome_arq= sys.argv[1]

    with open(nome_arq, 'r') as arq:
        todas_linhas = arq.readlines() #string que contem todas as linhas do arquivo
    return todas_linhas


#######################################################
def preenche_grafo(conteudo_arq):
    n_nos, n_arestas= ( int(x) for x in conteudo_arq[0].split())
    grafo1= Grafo(n_nos)
    
    for i in range(n_arestas):
        n1, n2, peso= ( int(x) for x in conteudo_arq[i+1].split())
        grafo1.adicionarAresta(n1, n2, peso)

    return grafo1


#######################################################
def menu_inicial():
    clear()
    print('Modulos:\n')
    print('1 - Execucão Simples')
    print('2 - Execucão Passo a Passo')

    opcao_menu_inicial = str(input('Opcao: '))
    if opcao_menu_inicial == '1':
        execucao_simples()
    elif opcao_menu_inicial == '2':
        execucao_passo_a_passo()
    else:
        print('Opcao invalida')

def execucao_simples():
    print('Execucao simples')

def execucao_passo_a_passo():
    print('Execucao passo a passo')

#######################################################
def clear():
#    os.system("clear")
    print (os.name)
    if os.name == 'nt':
        os.system("cls")
    elif os.name == 'posix':
        os.system("clear")

#######################################################

    
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

#######################################################

def script_entry():
    linhas= le_arquivo()
    grafo1= preenche_grafo(linhas)
    print(grafo1.imprimir())
    
    origem, destino= (int(x) for x in input('Informe o nodo de origem e destino: ').split())
        
    arestas= grafo1.getArestaNodo(origem)

    nodos_vizinhos=[]
    for a in arestas:
        nodos_vizinhos.append(a.getDestino())
#       print(a.getOrigem(), a.getDestino(), a.getRotulo())
    print("nodos_vizinhos: ",nodos_vizinhos)

    menu_inicial()


script_entry()

