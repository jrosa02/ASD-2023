import numpy as np

def a_compare(P: str, T: str, i:int = None, j:int = None):
    if i is None: i = len(P) - 1
    if j is None: j = len(T) - 1

    # int string_compare(char *P, char *T, int i, int j) {
    # if (i == 0 ) return liczba_pozostałych_znaków_w_T
    if i == 0: return j
    # if (j == 0 ) return liczba_pozostałych_znaków_w_P
    if j == 0: return i
    # zamian    = string_compare(P,T,i-1,j-1) + (P[i]!=T[j]);
    zamian = a_compare(P, T, i-1, j-1) + (P[i] != T[j])
    # wstawień = string_compare(P,T,i,j-1) + 1;
    wstawien = a_compare(P, T, i, j-1) + 1
    # usunięć   = string_compare(P,T,i-1,j) + 1;
    usun = a_compare(P, T, i-1, j) + 1
    # najniższy_koszt = najmiejsza_z(zamian, wstawień, usunięć)
    min_cost = min([zamian, wstawien, usun])
    # return najniższy_koszt
    return min_cost

def init(i, j):
    D = np.zeros((i, j))
    for ii in range(i):
        D[ii, 0] = ii

    for jj in range(j):
        D[0, jj] = jj

    return D

def b_compare(P: str, T: str, showpath = False):
    i = len(P)
    j = len(T)
    D = init(i, j)

    parents = [["X"] * j for _ in range(i)]
    for ii in range(i):
        parents[ii][0] = 'D'
    for jj in range(j):
        parents[0][jj] = 'D'

    for ii in range(i):
        for jj in range(j):
            zamian = D[ii-1][jj-1] + (P[ii] != T[jj])
            wstawien = D[ii, jj-1] + 1
            usun = D[ii-1, jj] + 1

            D[ii][jj] = min(zamian, wstawien, usun)
            if D[ii][jj] == zamian and P[ii] != T[jj]:
                parents[ii][jj] = "S"
            elif D[ii][jj] == zamian:
                parents[ii][jj] = "M"
            elif D[ii][jj] == usun:
                parents[ii][jj] = "D"
            elif D[ii][jj] == wstawien:
                parents[ii][jj] = "I"
    if not showpath:
        return int(D[i-1][j-1])
    
    out = str()
    j -= 1
    i -= 1

    while len(out) < len(P):
        if parents[i][j] != 'X':
            out += str(parents[i][j])
        else:
            out += 'D'
        if parents[i][j] == 'M' or parents[i][j] == 'S':
            i -= 1
            j -= 1
        elif parents[i][j] == 'I':
            j -=1
        elif parents[i][j] == 'D':
            i -= 1
        else:
            raise ValueError("Wrong character in parents matrix")
        
    out = out[::-1]
    return out

def d_compare(P: str, T: str):
    i = len(P)
    j = len(T)
    D = init(i, j)

    parents = [["X"] * j for _ in range(i)]
    for ii in range(i):
        parents[ii][0] = 'D'
    for jj in range(j):
        D[0][jj] = 0

    for ii in range(i):
        for jj in range(j):
            zamian = D[ii-1][jj-1] + (P[ii] != T[jj])
            wstawien = D[ii, jj-1] + 1
            usun = D[ii-1, jj] + 1

            D[ii][jj] = min(zamian, wstawien, usun)
            if D[ii][jj] == zamian and P[ii] != T[jj]:
                parents[ii][jj] = "S"
            elif D[ii][jj] == zamian:
                parents[ii][jj] = "M"
            elif D[ii][jj] == usun:
                parents[ii][jj] = "D"
            elif D[ii][jj] == wstawien:
                parents[ii][jj] = "I"

#   goal
    out = None
    i -= 1
    for jj in range( i, j):
        if out is None or D[i][out] > D[i][jj]:
            out = jj

    return out - i

def longest_compare(P: str, T: str):
    #co tu się stało to ja nawet nie XD
    i = len(P)
    j = len(T)
    D = [[0] * (j+1) for _ in range(i+1)]
    parents = [["X"] * (j+1) for _ in range(i+1)]

    for ii in range(i+1):
        D[ii][0] = ii
    for jj in range(j+1):
        D[0][jj] = jj

    for ii in range(1, i+1):
        for jj in range(1, j+1):
            zamian = float('inf') if P[ii-1] != T[jj-1] else D[ii-1][jj-1] + (P[ii-1] != T[jj-1])
            wstawien = D[ii][jj-1] + 1
            usun = D[ii-1][jj] + 1

            D[ii][jj] = min(zamian, wstawien, usun)
            if D[ii][jj] == zamian and P[ii-1] != T[jj-1]:
                parents[ii][jj] = "S"
            elif D[ii][jj] == zamian:
                parents[ii][jj] = "M"
            elif D[ii][jj] == usun:
                parents[ii][jj] = "D"
            elif D[ii][jj] == wstawien:
                parents[ii][jj] = "I"

    out = str()
    ii = i
    jj = j
    while ii > 0 and jj > 0:
        if parents[ii][jj] == "M" or parents[ii][jj] == "S":
            out += str(P[ii-1])
            ii -= 1
            jj -= 1
        elif parents[ii][jj] == "I":
            jj -= 1
        elif parents[ii][jj] == "D":
            ii -= 1
        else:
            raise ValueError("Wrong character in parents matrix")

    out = out[::-1]
    #ale działa
    return out





def main():
    P1 = ' kot'
    T1 = ' koń'

    P2 = ' kot'
    T2 = ' pies'

    P3 = ' biały autobus'
    T3 = ' czarny autokar'

    P4 = ' thou shalt not'
    T4 = ' you should not'

    P51 = ' ban'
    P52 = ' bin'
    T5 = ' mokeyssbanana'

    P6 = ' democrat'
    T6 = ' republican'

    T7 = ' 243517698'
    P7 = ' 123456789'
    
    print(a_compare(P1, T1))
    print(a_compare(P2, T2))

    print(b_compare(P1, T1))
    print(b_compare(P2, T2))
    print(b_compare(P3, T3))

    print(b_compare(P4, T4, True))

    print(d_compare(P51, T5))
    print(d_compare(P52, T5))

    print(longest_compare(P6, T6))
    print(longest_compare(P7, T7))

if __name__ == "__main__":
    main()