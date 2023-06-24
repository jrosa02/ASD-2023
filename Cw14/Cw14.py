import matplotlib.pyplot as plt

def skret(p1, p2, p3):
    return (p2[1] - p1[1])*(p3[0] - p2[0]) - (p3[1] - p2[1])*(p2[0] - p1[0])

def find_leftmost(zbior_pkt: list):
    p = zbior_pkt[0]

    for pkt in zbior_pkt:
        if pkt[0] < p[0] or (pkt[0] == p[0] and pkt[1] < p[1]):
            p = pkt
    return p

def find_next(p, zbior_pkt: list):
    for prop_q in zbior_pkt:
        if prop_q != p:
            isValid = True

            for r in zbior_pkt:
                #for all r p-q-r should be left
                if r != prop_q and r != p:
                    if skret(p, prop_q, r) > 0:
                        isValid = False
                        break
                    elif skret(p, prop_q) == 0:
                        return

            if isValid:
                return prop_q
        
    return None


def jarvis(zbior_pkt: list):
    p = find_leftmost(zbior_pkt)
    first_p = p
    path = [p]

    while not (len(path) > 1 and path[-1] == path[0]):
        q = find_next(p, zbior_pkt)
        path.append(q)
        p = q
    return path

def unzip(list_tuples):
    return [
        [x[0] for x in list_tuples],
        [x[1] for x in list_tuples]
    ]

def main():
    plot = False
    t1 =  [(0, 3), (0, 0), (0, 1), (3, 0), (3, 3)]
    if plot:
        plt.figure()
        plt.scatter(unzip(t1)[0], unzip(t1)[1])
        plt.waitforbuttonpress(10)
    t2 = [(0, 3), (0, 1), (0, 0), (3, 0), (3, 3)]
    print(jarvis(t1)) 
    print(jarvis(t2))

if __name__ == "__main__":
    main()