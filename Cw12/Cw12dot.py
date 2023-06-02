import time

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
    P = 0
    h = 1
    d = 256
    q = 101

    for i in range(N-1):  # N - jak wyżej - długość wzorca
        h = (h*d) % q 

    for sub in W:
        hsubs.add(hash(sub, 256, 101))

    hS = hash(S[0:N], 256, 101)
    
    for m in range(M-N+1):
        if hS in hsubs and S[m:m+N] in W:
            P += 1
        if m + N < M:
            hS = (d * (hS - ord(S[m]) * h) + ord(S[m + N])) % q
    t_stop = time.perf_counter()
    return P, t_stop-t_start

def main():
    with open("lotr.txt", encoding='utf-8') as f:
        text = f.readlines()

    S = ' '.join(text).lower()
    print(Rabin_Karp(S, "time."))
    subs = ['gandalf', 'looking', 'blocked', 'comment', 'pouring', 'finally', 'hundred', 'hobbits', 'however', 'popular', 'nothing', 'enjoyed', 'stuffed', 'relaxed', 'himself', 'present', 'deliver', 'welcome', 'baggins', 'further']
    print(Rabin_Karp_Bloom(S, subs))



if __name__ == "__main__":
    main()