import numpy as np






class Tabuleiro():
    def __init__(self):
        self.tabuleiro = np.zeros((16,16),dtype=int)
        self.turn = 0 
        self.pnt_pl1 = 0
        self.pnt_pl2 = 0
        

    def show(self):
        print(self.tabuleiro)

    def add(self,aresta):
        self.tabuleiro[aresta] = 1
        self.tabuleiro[aresta[::-1]] = 1

    


#main
if __name__ == "__main__":
    a = [   (0,1),(1,2),(2,3),
         (0,4),(1,5),(2,6),(3,7),
            (4,5),(5,6),(6,7),
        (4,8),(5,9),(6,10),(7,11),
            (8,9),(9,10),(10,11),
        (8,12),(9,13),(10,14),(11,15)
        (12,13),(13,14),(14,15)
    ]