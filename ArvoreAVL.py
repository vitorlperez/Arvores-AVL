class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
class BSTTree:
    def __init__(self):
        self.root = None
        self.size = 0
        self.nos = []
        self.folha = []
    def setRoot(self, no):
        self.root = no
    def insert(self, key):
        n = BSTNode(key)
        self.nos.append(n)
        if self.root == None:
            self.root = n
        else:
            now = self.root
            while True:
                old = now
                if key >= now.key:
                    now = now.right
                    if now == None:
                        old.right = n
                        now = old.right
                        break
                else:
                    now = now.left
                    if now == None:
                        old.left = n
                        now = old.left
                        break
    def buscaNoFolha(self, subtree):
        if (subtree.right == None) and (subtree.left == None):
            self.folha.append(subtree)
        else:
            if subtree.left != None:
                self.buscaNoFolha(subtree.left)
            if subtree.right != None:
                self.buscaNoFolha(subtree.right )
    def Distancia(self, no, valor):
        if no.key == valor and no.left == None and no.right == None:
            return 0
        else:
            if valor > no.key and no.right != None:
                return self.Distancia(no.right, valor) + 1
            if valor <= no.key and no.left != None:
                return self.Distancia(no.left, valor) + 1
            else:
                return 0
            
nr_de_nos = int(input())
arvore = BSTTree()
for i in range(nr_de_nos):
    esquerda, chave, direita = raw_input().split()
    chave = int(chave)
    arvore.insert(chave)

arvoreAVL = True   
for i in range(nr_de_nos):
    distancias_esq = []
    arvore_aux = BSTTree()
    if arvore.nos[i].left == None:
        dis_esq_f = 0
    else:
        arvore_aux.setRoot(arvore.nos[i].left)
        arvore_aux.buscaNoFolha(arvore_aux.root)
        for j in arvore_aux.folha:
            distancias_esq.append(arvore_aux.Distancia(arvore_aux.root, j.key))
        dis_esq_f = max(distancias_esq)+1
    distancias_dir = []
    arvore_aux2 = BSTTree()
    if arvore.nos[i].right == None:
        dis_dir_f = 0
    else:
        arvore_aux2.setRoot(arvore.nos[i].right)
        arvore_aux2.buscaNoFolha(arvore_aux2.root)
        if len(arvore_aux.folha)== 0:
            distancias_dir.append(0)
        else:
            for k in arvore_aux.folha:
                distancias_dir.append(arvore_aux2.Distancia(arvore_aux2.root, k.key))
        dis_dir_f = max(distancias_dir)+1
    if abs(dis_dir_f - dis_esq_f) > 1:
        arvoreAVL = False
        break
if arvoreAVL:
    print("sim")
else:
    print("nao")
                                

                              
            
                                                      
    
