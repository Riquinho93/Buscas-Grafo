import os

class Vertice:
    def __init__(self, rotulo):
        self.rotulo = rotulo
        self.visitado = False

    def igualA(self, r):
        return r == self.rotulo

    def foiVisitado(self):
        return self.visitado

    def registrarVisitado(self):
        self.visitado = True

    def limpa(self):
        self.visitado = False


class Grafo:
    def __init__(self):
        self.numVerticesMaximo = 20
        self.numVertice = 0
        self.listaVertice = []
        self.matrizAdjacencias = []
        for i in range(self.numVerticesMaximo):
            linhaMatriz = []
            for j in range(self.numVerticesMaximo):
                linhaMatriz.append(0)
            self.matrizAdjacencias.append(linhaMatriz)

    def adicionaVertices(self, rotulo):
        self.numVertice += 1
        self.listaVertice.append(Vertice(rotulo))

    def adicionaArco(self, inicio, fim):
        self.matrizAdjacencias[inicio][fim] = 1
        self.matrizAdjacencias[fim][inicio]

    def mostraVertice(self, vertice):
        print(self.listaVertice[vertice].rotulo)

    def imprimirMatriz(self):
        print()
        print("----GRAFO-------")
        print()
        print(" ", end=" ")
        for i in range(self.numVertice):
            print(self.listaVertice[i].rotulo, end=" ")
        print()
        for i in range(self.numVertice):
            print(self.listaVertice[i].rotulo, end=" ")
            for j in range(self.numVertice):
                print(self.matrizAdjacencias[i][j], end=" ")
            print()
        print()

    def localizaRotulo(self, rotulo):
        for i in range(self.numVertice):
            if self.listaVertice[i].igualA(rotulo): return i
        return -1

    def obtemAdjacenteNaoVisitado(self, v):
        for i in range(self.numVertice):
            if self.matrizAdjacencias[v][i] == 1 and self.listaVertice[i].foiVisitado() == False:
                return i
        return -1  # se não encontrar o elemento

    def dfs(self, inicio, fim):
        pilha = []   #pilha em python funciona como lista
        self.listaVertice[inicio].registrarVisitado()
        pilha.append(inicio) # funciona como push
        while len(pilha) != 0:
            elementoAnalisar = pilha[len(pilha) - 1] # retina o elemento sem remover da pilha
            if elementoAnalisar == fim: # se não é o ultimo elemento
                print()
                print("------ BUSCA EM PROFUNDIDADE ------ ")
                print()
                print("Caminho encontrado: ", end=" ")
                for i in pilha:
                    print(self.listaVertice[i].rotulo,"->", end=" ")
                print()
                print()
                print()
                break
            v = self.obtemAdjacenteNaoVisitado(elementoAnalisar)
            if v == -1:
                pilha.pop()   # removendo o elemento da pilha
            else:
                self.listaVertice[v].registrarVisitado()
                pilha.append(v)
        else:
            print()
            print("Busca sem sucesso!")
            print()
        for i in self.listaVertice:
            i.limpa() # limpando para fazer outra busca

    def bfs(self, inicio, fim):
        for i in self.listaVertice:
            i.limpa()
        fila= []   #pilha em python funciona como lista
        if inicio == fim:
            print("Inicio igual ao fim")
            input()
            return
        self.listaVertice[inicio].registrarVisitado()
        print()
        print("------ BUSCA EM LARGURA ------ ")
        print()
        print("Caminho encontrado: ")
        self.mostraVertice(inicio)
        fila.append(inicio)
        while len(fila) != 0:
            elementoAtual = fila.pop(0) # remove o primeiro elemento da fila
            v = self.obtemAdjacenteNaoVisitado(elementoAtual)
            while v != -1:
                if v == fim:
                    self.mostraVertice(v)
                    return
                self.listaVertice[v].registrarVisitado()
                self.mostraVertice(v)
                fila.append(v)
                v = self.obtemAdjacenteNaoVisitado(elementoAtual)
            else:
                print("Caminho nao encontrado!")

if __name__ == "__main__":
  #  os.system("clear")
    grf = Grafo()
    while True:
        print("Escolha sua opção: ")
        print("(M)ostrar,(V)ertices, (A)rcos,(P)rofundidade, (L)argura ")
        escolha = str(input("Digite sua opção: ")).lower()
        if escolha == 'm':
            grf.imprimirMatriz()
        elif escolha == 'v':
            val = str(input("Digite o rotulo do arco: "))
            grf.adicionaVertices(val)
        elif escolha == 'a':
            rinicio = str(input("Digite o rotulo do vertice inicial: "))
            inicio = grf.localizaRotulo(rinicio)
            if inicio == -1:
                print("Vertice não existe!")
                input()
                continue
            rfim = str(input("Digite o rotulo do vertice final: "))
            fim = grf.localizaRotulo(rfim)
            if inicio == -1:
                print("Vertice não existe!")
                input()
                continue
            grf.adicionaArco(inicio, fim)
        elif escolha == 'p':
            rinicio = str(input("Digite o rotulo do vertice do arco inicial: "))
            inicio = grf.localizaRotulo(rinicio)
            if inicio == -1:
                print("Vertice nao cadastrado!")
                input()
                continue
            rfim = str(input("Digite o rotulo do vertice do arco final: "))
            fim = grf.localizaRotulo(rfim)
            if fim == -1:
                print("Vertice nao cadastrado!")
                input()
                continue
            grf.dfs(inicio, fim)
        elif escolha == 'l':
            rinicio = str(input("Digite o rotulo do vertice do arco inicial: "))
            inicio = grf.localizaRotulo(rinicio)
            if inicio == -1:
                print("Vertice nao cadastrado!")
                input()
                continue
            rfim = str(input("Digite o rotulo do vertice do arco final: "))
            fim = grf.localizaRotulo(rfim)
            if fim == -1:
                print("Vertice nao cadastrado!")
                input()
                continue
            grf.bfs(inicio, fim)
        elif escolha == 's':
            break
        else:
            print("Entrada invalida")
            input()
