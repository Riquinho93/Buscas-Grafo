import os


class Vertice:
    def __init__(self, rotulo):
        self.rotulo = rotulo

    def igualA(self, r):
        return r == self.rotulo


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
        print(self.matrizAdjacencias[vertice].rotulo)

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


if __name__ == "__main__":
  #  os.system("clear")
    grf = Grafo()
    while True:
        print("Escolha sua opção: ")
        print("(M)ostrar, (V)ertices e (A)rcos ")
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
        elif escolha == 's':
            break
        else:
            print("Entrada invalida")
            input()
