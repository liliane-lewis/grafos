# -*- coding: utf-8 -*-

import sys, os, re


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


class Grafo:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        #cria a matriz de adjacencia tamanho X tamanho
        self.matrizAdj = [[None for x in range(tamanho)] for y in range(tamanho)]
        self.distancias= [(x, float('inf')) for x in range(tamanho)]
        self.marcados = []
    
    def getTamanho(self):
       return self.tamanho    

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
        print( str(n1) + " " + str(n2))
        grafo1.adicionarAresta(n1, n2, peso)

    return grafo1


#######################################################
def menu_inicial(grafo):
    clear()
    print('Modulos:\n')
    print('1 - Execucão Simples')
    print('2 - Execucão Passo a Passo')

    opcao_menu_inicial = str(input('Opcao: '))
    if opcao_menu_inicial == '1':
        execucao_simples(grafo)
    elif opcao_menu_inicial == '2':
        execucao_passo_a_passo(grafo)
    else:
        print('Opcao invalida')

def execucao_simples(grafo):
    dijkstra(grafo)
    #print('Execucao simples')

def execucao_passo_a_passo(grafo):
    dijkstra(grafo,1)
    #print('Execucao passo a passo')

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
    menu_inicial(grafo1)
 #   arestas= grafo1.getArestaNodo(origem)
    distancias= grafo1.getDistancias()
   # print(distancias)                  #valor inicial do array de tuplas


def dijkstraPasso(grafo, nodo):
    novos_vizinhos=[]
    if grafo.verificarNodoMarcado(nodo):   #nodo já tratado, seleciona o próximo nodo
        return novos_vizinhos

    grafo.marcarNodo(nodo)

    arestas= grafo.getArestaNodo(nodo)

    #verifica todos os vizinhos do respectivo nodo e atualiza o array de distancias
    for a in arestas:
        if grafo.verificarNodoMarcado(a.getDestino()):      #se essa aresta corresponde a um vizinho ja visitado, vai para o prox. vizinho
            continue
        distanciaVizinho= (grafo.getDistancia(a.getDestino()))  #seleciona a tupla do vizinho do nodo atual
        dist_nodo= grafo.getDistancia(a.getOrigem())[1]         #distancia da origem ate o nodo atual
        peso_aresta= a.getRotulo()
        dist_caminho= dist_nodo + peso_aresta                    #distancia da origem ate o vizinho, passando pelo nodo atual
        dist_atual= distanciaVizinho[1]  

        distanciaVizinho= (distanciaVizinho[0], min(dist_atual, dist_caminho)) #atualiza distancia do vizinho com o menor caminho
        grafo.setDistancia(distanciaVizinho[0], distanciaVizinho[1])          #atualiza o array
        novos_vizinhos.append(distanciaVizinho)

    return novos_vizinhos


def dijkstra(grafo, passo_a_passo=None):
    origem, destino= (int(x) for x in input('Informe o nodo de origem e destino: ').split())
    grafo.setOrigem(origem)
    
    d_n_viz=[]               #d_n_viz = distancia dos nodos vizinho: armazena tuplas do formato '(nodo, distancia_atual_em_relacao_a_origem)'

    d_n_viz.append(grafo.getDistancia(origem))

    while d_n_viz:
       nodo=d_n_viz.pop(0)[0]
       for nova_distancia in dijkstraPasso(grafo, nodo):              #seleciona o primeiro nodo da lista ordenada por tamanho de caminho
           d_n_viz.append(nova_distancia)
           d_n_viz= sorted(d_n_viz, key=lambda d_n_viz: d_n_viz[1])    #ordena a lista com os nodos de forma crescente de distancia
       if passo_a_passo:
           input("Digite Qualquer tecla para continuar\n")      
           printDijkstra(grafo, d_n_viz, nodo)
 
    distancias= grafo.getDistancias()    #valor final do array de tuplas com as distancias em relacao a origem.
    #print(distancias)
    print("Distancia de", origem, "a", destino, "=", grafo.getDistancia(destino)[1])


def printDijkstra(grafo, lista, nodo):
    print("Nodo Atual: " + str(nodo))
    print("Conjunto Fechado")
    str_fechado=""
    str_aberto=""
    for n in range(grafo.getTamanho()) :
        if grafo.verificarNodoMarcado(n):
            str_fechado= str_fechado + str(n) + " "              
    print(str_fechado)

    print("Conjunto Aberto")
    for n in lista:
        str_aberto= str_aberto+str(n[0])+ " "

    print(str_aberto)

    for t in grafo.getDistancias():
        str_marcado=" "
        if grafo.verificarNodoMarcado(t[0]):
            str_marcado= "\tclosed."
        print("Nodo: " + str(t[0]) +" distância: " + str(t[1])+ str_marcado) 
    print("\n")



script_entry()

