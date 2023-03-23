import numpy as np


#função para criação da matriz a partir de um arquivo de instância
#entrada: nome do arquivo a ser aberto
#saida: matriz de adjacencia do arquivo
def leitura(nome):

    #Definindo o caminho de onde o arquivo será aberto
    path = "grafos_datasets\ "
    path = path[:16] + nome

    #abrindo arquivo de leitura
    arq = open(path, 'r')

    #gerando matriz com a biblioteca Numpy
    mat = np.genfromtxt(arq, dtype="int32")

    #fechando arquivo
    arq.close()

    #retornando matriz criada
    return mat

#função para escrever em arquivo e na tela o nome e dimensões da matriz de adjacencia de um arquivo
#entrada: matriz de adjacencia
#saida: print e arquivo externo com nome e dimensões de matriz de adjacencia
def saida(mat):

    #separando em duas strings simples as dimensões da matriz
    tam = str(np.shape(mat))
    tam = tam.split('(')
    tam = tam[1].split(')')
    tam = tam[0].split(',')

    #juntando nome e dimensões da matriz da maneira solicitada
    dadosI = nome + " " + tam[0] + tam[1]

    #abrindo ou criando arquivo onde resultados serão armazenados
    arq = open('tamanhos.txt', 'a+')

    #escrevendo resultados no arquivo
    arq.writelines(dadosI + '\n')
    
    #fechando arquivo
    arq.close()
    
    #mostrando resultados na tela
    print(dadosI)


#leitura do nome do arquivo a ser aberto
nome = input("Digite o nome da instância que deseja abrir (com extensão do arquivo): ")

#mat recebe a saida da função leitura
mat = leitura(nome)

#chamada da função de saida
saida(mat)