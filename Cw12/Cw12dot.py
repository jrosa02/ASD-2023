import time
import math
import numpy as np

primes = [179,	181,	191,	193,	197,	199,	211,	223,	227,	229,	233,	239,	241,	251,	257,	263,	269,	271,	277,	281]

def hash(word: str, d=256, q=101):
    hw = 0
    N = len(word)
    for i in range(N):  # N - to długość wzorca
        hw = (hw*d + ord(word[i])) % q  # dla d będącego potęgą 2 można mnożenie zastąpić shiftem uzyskując pewne przyspieszenie obliczeń
    return hw

def Rabin_Karp(S: str, W: str):
    t_start = time.perf_counter()
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
    t_stop = time.perf_counter()
    return (len(outlist), t_stop-t_start)
    

def Rabin_Karp_Bloom(S: str, W: list):
    t_start = time.perf_counter()
    M = len(S)
    N = len(W[0])
    hsubs = set()
    nP = 0
    d = 256
    q = 101
    P = 0.001
    n = 20
    b = int(-1*n * math.log(P)/(math.log(2)**2))
    k = int(b/n*math.log(2))
    false_positive = []
    false_positive_n = 0
    
    wynik = {klucz: 0 for klucz in W}
    filtr = [0 for _ in range(b)]
    h = [1 for _ in range(k)]
    Sfiltri = [0 for _ in range(k)]
    for word in W:
        for prime in primes[:k]:
            filtr[hash(word, d, prime)] = 1
    for j in range(k):
        for i in range(N-1):  # N - jak wyżej - długość wzorca
            h[j] = (h[j]*d) % primes[j]

    for i in range(k):
        Sfiltri[i] = hash(S[:N], d, primes[i])
    
    for m in range(M-N+1):
        pasuje = True
        for index in Sfiltri:
            if filtr[index] != 1:
                pasuje = False
        if pasuje:
            if S[m:m+N] in W:
                wynik[S[m:m+N]] += 1
                nP += 1
            else:
                false_positive.append(S[m:m+N])
                false_positive_n += 1
        if m + N < M:
            for i in range(k):
                Sfiltri[i] = (d * (Sfiltri[i] - ord(S[m]) * h[i]) + ord(S[m + N])) % primes[i]
    t_stop = time.perf_counter()
    return nP, t_stop-t_start, false_positive_n, wynik

def main():
    with open("lotr.txt", encoding='utf-8') as f:
        text = f.readlines()

    S = ' '.join(text).lower()
    print(Rabin_Karp(S, "time."))
    subs = ['gandalf', 'looking', 'blocked', 'comment', 'pouring', 'finally', 'hundred', 'hobbits', 'however', 'popular', 'nothing', 'enjoyed', 'stuffed', 'relaxed', 'himself', 'present', 'deliver', 'welcome', 'baggins', 'further']
    print(Rabin_Karp_Bloom(S, subs))


if __name__ == "__main__":
    main()