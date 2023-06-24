import matplotlib.pyplot as plt

def skret(p1, p2, p3):
    return (p2[1] - p1[1])*(p3[0] - p2[0]) - (p3[1] - p2[1])*(p2[0] - p1[0])

def find_leftmost(zbior_pkt: list):
    p = zbior_pkt[0]

    for pkt in zbior_pkt:
        if pkt[0] < p[0] or (pkt[0] == p[0] and pkt[1] < p[1]):
            p = pkt
    return p


def among_us(p1, p2, p3):
    isValid = False

    for i in [-1, 1]:

        for j in [-1, 1]:

            if (p1[0]*i < p2[0]*i < p3[0]*i) or (p1[1]*j < p2[1]*j < p3[1]*j):
                isValid = True

    return isValid


def find_next(p, zbior_pkt: list):
    q = zbior_pkt[(zbior_pkt.index(p) + 1) % len(zbior_pkt)]
    for r in zbior_pkt:
        sk = skret(p, r , q)
        if sk < 0:
            q = r

    return q

def find_next2(p, zbior_pkt: list):
    q = zbior_pkt[(zbior_pkt.index(p) + 1) % len(zbior_pkt)]
    for r in zbior_pkt:
        sk = skret(p, r , q)
        if sk < 0:
            q = r
        elif sk == 0 and among_us(p, q, r):
            q = r

    return q


def jarvis1(zbior_pkt: list):
    p = find_leftmost(zbior_pkt)
    path = []
    q = p

    while not (len(path) > 1 and q == path[0]):
        path.append(q)
        p = q
        q = find_next(p, zbior_pkt)  
    return path

def jarvis2(zbior_pkt: list):
    p = find_leftmost(zbior_pkt)
    path = []
    q = p

    while not (len(path) > 1 and q == path[0]):
        path.append(q)
        p = q
        q = find_next2(p, zbior_pkt)  
    return path

def unzip(list_tuples):
    return [
        [x[0] for x in list_tuples],
        [x[1] for x in list_tuples]
    ]

def main():
    plot = False
    t1 =  [(0, 3), (0, 0), (0, 1), (3, 0), (3, 3)]
    t2 = [(0, 3), (0, 1), (0, 0), (3, 0), (3, 3)]
    t3 = [(2, 2), (4, 3), (5, 4), (0, 3), (0, 2), (0, 0), (2, 1), (2, 0), (4, 0)]
    if plot:
        plt.figure()
        plt.scatter(unzip(t3)[0], unzip(t3)[1])
        plt.waitforbuttonpress(15)
    


    print(jarvis1(t3))
    print(jarvis2(t3))

if __name__ == "__main__":
    main()