import time

def naiwe(S: str, W: str):
    t_start = time.perf_counter()
    counter = 0
    outlist = []
    for m in range(len(S)):
        ok = True
        for i in range(len(W)):
            counter += 1
            if S[m+i] != W[i]:
                ok = False
                break
        if ok:
            outlist.append(m)

    t_stop = time.perf_counter()
    return (len(outlist), t_stop-t_start, counter)


def hash(word, d=256, q=101):
    hw = 0
    for i in range(len(word)):  # N - to długość wzorca
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

    # let T[0] ← -1
    T[0] = -1
    while pos < len(W):
        if W[pos] == W[cnd]:
            T[pos] = T[cnd]
        else:
            T[pos] = cnd
            while cnd >= 0 and W[pos] != W[cnd]:
                cnd = T[cnd]
        pos = pos + 1
        cnd = cnd + 1
    T[pos] = cnd
    return T

def KMP(S:str, W:str):
    pass


def main():
    with open("lotr.txt", encoding='utf-8') as f:
        text = f.readlines()

    S = ' '.join(text).lower()

    output = naiwe(S, "time.")
    print(f"Number: {output[0]}, elapsed time: {output[1]*1e3:.0f} ms, counter {output[2]}")
    output = Rabin_karp(S, "time.")
    print(f"Number: {output[0]}, collisions: {output[1]}, counter {output[2]}")
    T = KMP_T("tite.")
    print(T)



if __name__ == "__main__":
    main()