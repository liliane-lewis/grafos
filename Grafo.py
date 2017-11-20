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
        self.distancias= [(x, float('inf')) for x in range(tamanho)]
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

    def getDistancias(self):    #somente para debugs
        return self.distancias

    def getDistancia(self, nodo):
        return self.distancias[nodo]

    def setDistancia(self, nodo, dist):
        self.distancias[nodo]= (nodo,dist)

    def setOrigem(self, origem):
        self.distancias= [(x, float('inf')) for x in range(self.tamanho)]
        self.distancias[origem]= (origem, 0)
    
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
#    print(grafo1.imprimir())
    
    menu_inicial()

    origem, destino= (int(x) for x in input('Informe o nodo de origem e destino: ').split())
        
 #   arestas= grafo1.getArestaNodo(origem)

    distancias= grafo1.getDistancias()
    print(distancias)                  #valor inicial do array de tuplas

    grafo1.setOrigem(origem)
    
    d_n_viz=[]                         #d_n_viz = distancia dos nodos vizinho

    d_n_viz.append(grafo1.getDistancia(origem))             #d_n_viz = distancia dos nodos vizinho
    

    while d_n_viz:
        nodo= d_n_viz.pop(0)[0]
        if grafo1.verificarNodoMarcado(nodo):   #nodo já tratado, seleciona o próximo nodo
            continue

        grafo1.marcarNodo(nodo)

        arestas= grafo1.getArestaNodo(nodo)

        #verifica todos os vizinhos do respectivo nodo e atualiza o array de distancias
        for a in arestas:
            if grafo1.verificarNodoMarcado(a.getDestino()):      #se essa aresta corresponde a um vizinho ja visitado, vai para o prox. vizinho
                continue
            distanciaVizinho= (grafo1.getDistancia(a.getDestino()))  #seleciona a tupla do vizinho do nodo atual
            dist_nodo= grafo1.getDistancia(a.getOrigem())[1]         #distancia da origem ate o nodo atual
            peso_aresta= a.getRotulo()
            dist_caminho= dist_nodo + peso_aresta                    #distancia da origem ate o vizinho, passando pelo nodo atual
            dist_atual= distanciaVizinho[1]  

            distanciaVizinho= (distanciaVizinho[0], min(dist_atual, dist_caminho)) #atualiza distancia do vizinho com o menor caminho
            grafo1.setDistancia(distanciaVizinho[0], distanciaVizinho[1])          #atualiza o array
            d_n_viz.append(distanciaVizinho)

        d_n_viz= sorted(d_n_viz, key=lambda d_n_viz: d_n_viz[1])     #ordena a lista com os nodos de forma crescente de distancia
                                                                     #sendo este o de menor caminho da lista
        
    distancias= grafo1.getDistancias()    #valor final do array de tuplas com as distancias em relacao a origem.
    print(distancias)

    print("Distancia de", origem, "a", destino, "=", grafo1.getDistancia(destino)[1])



script_entry()

