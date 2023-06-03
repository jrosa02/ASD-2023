import time
import math
import numpy as np

def hash(word: str, d=256, q=101):
    hw = 0
    N = len(word)
    for i in range(N):  # N - to długość wzorca
        hw = (hw*d + ord(word[i])) % q  # dla d będącego potęgą 2 można mnożenie zastąpić shiftem uzyskując pewne przyspieszenie obliczeń
    return hw

def FastPrimeSieve(min, max):
    possible_primes =  range(min, max+1, 2)
    curr_index = -1
    max_index = len(possible_primes)
    for latest_prime in possible_primes:
        curr_index +=1
        if not latest_prime : continue
        for index_variable_not_named_j in range((curr_index+latest_prime),max_index, latest_prime): possible_primes[index_variable_not_named_j]=0
    possible_primes.insert(0,2)
    return [x for x in possible_primes if x > 0]

def Bloom(W: str, b=18, k=3):
    filtr = 0
    primes = FastPrimeSieve(30*k, 45*k)
    for i in range(k):
        x = hash(W, q=primes[k])%b
        filtr += 1<<b
    return filtr


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
    h = 1
    d = 256
    q = 101
    P = 0.001
    n = 20
    b = -1*n * math.log(P)/(math.log(2)^2)
    k = b/n*math.log(2)

    for i in range(N-1):  # N - jak wyżej - długość wzorca
        h = (h*d) % q 

    for sub in W:
        hsubs.add(hash(sub, 256, 101))

    hS = hash(S[0:N], 256, 101)
    
    for m in range(M-N+1):
        if hS in hsubs and S[m:m+N] in W:
            nP += 1
        if m + N < M:
            hS = (d * (hS - ord(S[m]) * h) + ord(S[m + N])) % q
    t_stop = time.perf_counter()
    return nP, t_stop-t_start

def main():
    with open("lotr.txt", encoding='utf-8') as f:
        text = f.readlines()

    S = ' '.join(text).lower()
    print(Rabin_Karp(S, "time."))
    subs = ['gandalf', 'looking', 'blocked', 'comment', 'pouring', 'finally', 'hundred', 'hobbits', 'however', 'popular', 'nothing', 'enjoyed', 'stuffed', 'relaxed', 'himself', 'present', 'deliver', 'welcome', 'baggins', 'further']
    print(Rabin_Karp_Bloom(S, subs))



if __name__ == "__main__":
    main()