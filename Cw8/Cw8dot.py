import time
import random

class Node:
    # Element kolejki niech będzie obiektem klasy, której atrybutami będą __dane i __priorytet.
    # Ta klasa powinna mieć zdefiniowane 'magiczne' metody pozwalające na użycie na jej obiektach operatorów
    # < i >  (metody __lt__ i __gt__) oraz wypisanie ich print-em (__str__) w postaci
    # priorytet : dane.
    # Dzięki zastosowaniu operatorów < i > atrybuty __dane i  __priorytet mogą (i powinny być) prywatne.
    def __init__(self, priorytet, dane = None) -> None:
        self.__dane = dane
        self.__priorytet = priorytet
    
    def __gt__(self, other):
        if other == None:
           return True
        return self.__priorytet > other.__priorytet
    
    def __lt__(self, other):
        if other == None:
            return False
        return self.__priorytet < other.__priorytet

    def __str__(self) -> str:
        return str(self.__priorytet) + " : " + str(self.__dane)


def shell_sort(lst, shell_list):
    for gap in shell_list:
        for i in range(gap, len(lst)):
            temp = lst[i]
            j = i
            while(j>=gap and lst[j - gap]>temp):
                lst[j] = lst[j - gap]
                j-=gap
            lst[j] = temp


if __name__ == "__main__":
    org_shell = [64//(2**n) for n in range(7)]
    lst = []
    param =  [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    for elem in param:
        lst.append(Node(elem[0], elem[1]))
    shell_sort(lst, org_shell)
    for elem in lst:
        print("(", elem, ")", end = ' ')
    print()
    print("Sortowanie niestabilne")
    
    lst = []
    for i in range(100):
        lst.append(int(random.random() * 100))

    t_start = time.perf_counter()
    shell_sort(lst, org_shell)   
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))   
    #print(lst)