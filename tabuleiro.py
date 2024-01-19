import numpy as np


class Tabuleiro():
    def __init__(self):
        self.tabuleiro = np.zeros((16,16),dtype=int)

    def show(self):
        print(self.tabuleiro)

    def add(self,aresta):
        self.tabuleiro[aresta] = 1 

    def has_ended(self):
        if np.all(self.tabuleiro == 1):
             print('YES')
        else:
            print('no')



#main
if __name__ == "__main__":
    t= Tabuleiro()
    a = (1,2)
    print(a[::-1])