from random import random

class CampoMinado:
    def __init__(self,tamanho):
        """ Inicicializando Objeto tabuleiro 5x5"""
        self.tamanho = tamanho
        self.quantidade_bombas = self.__total_bombas()
        self.__distribuir_bombas()
        self.coordenadas_bombas = []
        self.tabuleiro = [['X' for x in range(tamanho)] for j  in range(tamanho)]
        range(tamanho)

    def __distribuir_bombas(self):
        quantidade_bombas = self.quantidade_bombas
        while(quantidade_bombas > 0 ):
            coordenada = [randint(0,self.tamanho),randint(0,self.tamanho)]
            if coordenada not in self.coordenadas_bombas:
                self.coordenadas_bombas.append(coordenada)
                quantidade_bombas-=1



    def __total_bomas(self):
        return self.tamanho/2
    def __str__(self):
        return str(self.tabuleiro)




objeto = CampoMinado(5)
for linha in objeto.tabuleiro:
    print(str(linha))