class Node:
    def __init__(self, leaf=False):
        self.leaf = leaf    #czy komorka jest lisciem
        self.keys = []      #lista kluczy
        self.child = []     #list dzieci


class BTree:
    def __init__(self, t):
        #korzen na poczatku zawsze jest lisciem
        self.root = Node(True)
        #poziom drzewa
        self.t = t

    def insert(self, k):
        root = self.root
        #jesli w korzeniu jest zbyt duzo kluczy
        if len(root.keys) == (2 * self.t) - 1:
            temp = Node()
            self.root = temp
            temp.child.insert(0, root)
            self.split(temp, 0)
            self.insert_rek(temp, k)
        else:
            self.insert_rek(root, k)


    def insert_rek(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append((None, None))
            while i >= 0 and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            if len(x.child[i].keys) == (2 * self.t) - 1:
                self.split(x, i)
                if k > x.keys[i]:
                    i += 1
            self.insert_rek(x.child[i], k)


    #podziel na medianie
    def split(self, x, i):
        t = self.t
        y = x.child[i]
        z = Node(y.leaf)
        x.child.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t: (2 * t) - 1]
        y.keys = y.keys[0: t - 1]
        if not y.leaf:
            z.child = y.child[t: 2 * t]
            y.child = y.child[0: t - 1]

    #zwraca komorke jesli znajdzie, jesli nie zwraca None
    def search(self, k, x=None):
        #dla wywolania nierekurencyjnego
        if x is not None:
            i = 0

            while i < len(x.keys) and k > x.keys[i]:
                i += 1

            if i < len(x.keys) and k == x.keys[i]:
                return (x, i)
            elif x.leaf:
                return None
            else:
                return self.search(k, x.child[i])
        else:
            return self.search(k, self.root)


    def print_tree(self, x, l=0):
        print("Poziom w drzewie ", l, " ", len(x.keys), end=":  ") #domyslnie print konczy znak nowej lini
        for i in x.keys:
            print(i, end="  ")
        print()
        l += 1
        if len(x.child) > 0:
            for i in x.child:
                self.print_tree(i, l)


if __name__ == '__main__':
    B = BTree(3)


    for i in [6, 19, 17, 11, 3, 12, 8, 20, 22, 23, 13, 18, 14, 16, 1, 2, 24, 25, 4, 26, 5, 7, 10]:
        B.insert(i)

    if B.search(14) is not None:
        print("\nZnaleziono")
    else:
        print("\nNie znalezniono")



    print("\n")


    B.print_tree(B.root)


