import numpy as np
import cv2
import Cw9
import matplotlib.pyplot as plt

I = cv2.imread("download.png",cv2.IMREAD_GRAYSCALE)
graph = Cw9.lstGraf()

for row in range(I.shape[0]):
    for col in range(I.shape[1]):
        graph.insertVertex(Cw9.Vertex(I.shape[1] * row + col, I[row, col]))
for row in range(1, I.shape[0]-1):
    for col in range(1, I.shape[1]-1):
        for i in range(3):
            for j in range(3):
                if i!=1 or j!=1:
                    graph.insertEdge(Cw9.Vertex(I.shape[1] * row + col, I[row, col]),
                                    Cw9.Vertex(I.shape[1] * (row - 1 + i) + (col-1 + j), I[row - 1 + i, col-1 + j]),
                                    np.abs(np.int64(I[row, col]) - np.int64(I[row-1 + i, col-1 + j])))
                    
        
                    
primagraf, suma = Cw9.PrimaDżewo(graph)

maxval = -1
maxedge = [-1, -1]
for vertex1  in list(primagraf.index_dict.values()):
    for i in range(len(primagraf.prox_list[vertex1])):
        #print(vertex1, i)
        if maxval < primagraf.prox_list[vertex1][i][1]:
            maxval = primagraf.prox_list[vertex1][i][1]
            maxedge = [vertex1, i]
x = primagraf.prox_list[maxedge[0]][maxedge[1]][0] 
primagraf.prox_list[maxedge[0]].pop(maxedge[1])

IS = np.zeros(I.shape)
# implementujemy prostą trawersację grafu - np. z wykorzystaniem stosu, kolejki lub rekurencyjną  (nie ma to większego znaczenia w tym przypadku),
def traverse(graphh: Cw9.lstGraf, point, fn, val, img):
    visited = set([point])
    stos = [point]
    while len(stos):
        current = stos.pop()
        fn(graphh, current, val, img)
        visited.add(current)
        neighs = graphh.neighboursIdx(current)
        for neigh in neighs:
            if neigh not in visited:
                stos.append(neigh)

def color(graphh, indx, val, img):
    vertex = graphh.getVertex(indx)
    vertex.data = val
    img[vertex.key//img.shape[1], vertex.key%img.shape[1]] = vertex.data
    return img

img = np.zeros(I.shape)
# uruchamiamy przejścia po obu drzewach - zaczynamy od wierzchołków, które łączyła usunięta krawędź. Niech każde przeszukanie 'pokoloruje' piksele odpowiadające odwiedzanym wierzchołkom jednym 'kolorem' (proszę jako 'kolor' ustalić dwa poziomy szarości - np. 100 i 200)
#traverse(primagraf, x, color, 200, img)
traverse(primagraf, maxedge[0], color, 100, img)
# z “napotkanych” wierzchołków odczytujemy współrzędne piksela (y = klucz//XX, x = klucz % XX) i pod te współrzędne wpisujemy "kolor" do obrazu wyjściowego

# obraz wyświetlamy (przykładowo: cv2.imshow("Wynik",IS) oraz cv2.waitKey() )
cv2.imshow("Wynik", img)
cv2.waitKey()