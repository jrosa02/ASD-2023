import numpy as np
import cv2
import Cw9

I = cv2.imread("sample.png",cv2.IMREAD_GRAYSCALE)
print(I)
graph = Cw9.lstGraf()

for row in range(I.shape[0]):
    for col in range(I.shape[1]):
        graph.insertVertex(Cw9.Vertex(I.shape[0] + row + col, I[row, col]))
for row in range(I.shape[0]-1):
    for col in range(I.shape[1]-1):
        for i in range(3):
            for j in range(3):
                if i!=1 and j!=1:
                    graph.insertEdge(Cw9.Vertex(I.shape[0] + row + col, I[row, col]),
                                    Cw9.Vertex(I.shape[0] + (row - 1 + i) + (col-1 + j), I[row - 1 + i, col-1 + j]),
                                    np.abs(I[row, col] - I[row-1 + i, col-1 + j]))
Cw9.printGraph(graph)
Cw9.PrimaDżewo()