from Cw7.Cw7 import Graf



import numpy as np

class MacierzSom(Graf):
    def __init__(self):
        super().__init__()
        self.matrix = np.array([])
        self.vertexes = []
    
    def insertVertex(self, vertex):
        self.vertexes.append(vertex)
        self.matrix = np.c_[self.matrix, np.zeros(len(self.matrix[0]))]
        self.matrix = np.r_[self.matrix, [np.zeros(len(self.matrix[1]))]]

    def insertEdge(self, vertex1, vertex2, edge = 1):
        Idx1 = self.getVertexIdx(vertex1)
        Idx2 = self.getVertexIdx(vertex1)