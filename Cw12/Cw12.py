import time

def naiwe(S: str, W: str):
    t_start = time.perf_counter()
    counter = 0
    outlist = []
    M = len(S)
    N = len(W)
    m = 0
    while m < M:
        ok = True
        n = 0
        while n < N:
            counter += 1
            if S[m+n] != W[n]:
                ok = False
                break
            n += 1
        if ok:
            outlist.append(m)
        m += 1

    t_stop = time.perf_counter()
    return (len(outlist), t_stop-t_start, counter)


def hash(word: str, d=256, q=101):
    hw = 0
    N = len(word)
    for i in range(N):  # N - to długość wzorca
        hw = (hw*d + ord(word[i])) % q  # dla d będącego potęgą 2 można mnożenie zastąpić shiftem uzyskując pewne przyspieszenie obliczeń
    return hw


def Rabin_karp(S: str, W: str):
    M = len(S)
    N = len(W)
    hS = hash(S[:N])
    hW = hash(W)
    counter = 0
    collision = 0
    outlist = []
    q =101
    d = 256

    h = 1
    for i in range(N-1):  # N - jak wyżej - długość wzorca
        h = (h*d) % q 

    for m in range(M-N+1):

        counter += 1
        if hS == hW:
            counter += N
            if S[m:m+N] == W[:N]:
                outlist.append(m)
            else:
                collision += 1
        if m + N < M:
            hS = (d * (hS - ord(S[m]) * h) + ord(S[m + N])) % q

    return (len(outlist), collision, counter)
    

def KMP_T(W: str) -> list:

    # an array of integers, T (the table to be filled)
    # an integer, pos ← 1 (the current position we are computing in T)
    # an integer, cnd ← 0 (the zero-based index in W of the next character of the current candidate substring)
    pos = 1
    
    cnd = 0
    N = len(W)
    T = [0 for _ in range(N + 1)]
    counter = 0
    # let T[0] ← -1
    T[0] = -1
    while pos < len(W):
        counter += 1
        if W[pos] == W[cnd]:
            T[pos] = T[cnd]
        else:
            T[pos] = cnd
            counter += 1
            while cnd >= 0 and W[pos] != W[cnd]:
                counter += 1
                cnd = T[cnd]
        pos = pos + 1
        cnd = cnd + 1
    T[pos] = cnd
    return T, counter


def KMP_S(S:str, W:str):
    t_start = time.perf_counter()
    M = len(S)
    N = len(W)
    P = []
    nP = 0
    m = 0
    i = 0
    T, counter = KMP_T(W)

    while m < M:
        counter += 1
        if W[i] == S[m]:
            m += 1
            i += 1
            if i == N:
                P.append(m)
                nP += 1
                i = T[i]
        else:
            i = T[i]
            if i < 0:
                m += 1
                i += 1
    t_stop = time.perf_counter()
    return nP, counter, T



def main():
    with open("lotr.txt", encoding='utf-8') as f:
        text = f.readlines()

    S = ' '.join(text).lower()

    output = naiwe(S, "time.")
    print(f"{output[0]}; {output[2]}")
    output = Rabin_karp(S, "time.")
    print(f"{output[0]}; {output[2]}; {output[1]}")
    output = KMP_S(S, "time.")
    print(f"{output[0]}; {output[1]}; {output[2]}")



if __name__ == "__main__":
    main()