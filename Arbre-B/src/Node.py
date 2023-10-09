class Node:

    """
    La classe Node représente un noeud dans une structure de données d'arbre b.

    Attributs:
    ----------
    keys (list): une liste triée des clés stockées dans ce nœud.
    childs (list): une liste des nœuds enfants de ce nœud.

    Méthodes:
    ----------
    add_key(self, value): ajoute une clé dans la liste triée des clés.
    add_childs(self, value): ajoute un enfant à la fin de la liste des enfants.
    add_childs_idx(self, i, value): ajoute un noeud enfant à l'indice donné.
    childSearch(self, val): recherche la position de l'enfant où la valeur doit être insérée.
    search(self, val): recherche une valeur donnée dans un noeud et ses enfants directs.
    get_max(self) : Supprime et renvoie la plus grande clé dans le sous-arbre courant récursivement jusqu'à ce que le dernier enfant soit atteint.
    get_min(self) : Supprime et renvoie la plus petite clé dans le sous-arbre courant récursivement jusqu'à ce que le premier enfant soit atteint.
    """
    
    # ------------------------------ Constructeur ------------------------------
    
    def __init__(self):
     
        """
        Initialise un nouveau noeud (classe Node) avec une liste de clés vide et une liste d'enfants vide.
        """
        
        self.keys = []
        self.childs = []
        self.num_virtual_reads = 0
        self.num_virtual_write = 0


    # ------------------------------ Ajout d'une clé ------------------------------

    def add_key(self, value):
        
        """
        Ajoute une clé dans la liste triée des clés.

        Paramètres:
        -----------
        value : la valeur de la clé à ajouter.

        Renvoie:
        --------
        int: l'indice de la position de la clé ajoutée dans la liste.        
        """
        self.num_virtual_write += 1

        i = 0
        if not self.keys:
            self.keys.append(value)
        else:
            while i < len(self.keys) and value > self.keys[i]:
                i += 1
            self.keys.insert(i, value)
        return i

    # ------------------------------ Ajout d'un fils ------------------------------
    
    def add_childs(self, value):
        
        """
        Ajoute un noeud enfant à la fin de la liste des enfants.

        Paramètres:
        -----------
        value (Node): le noeud enfant à ajouter.
        """
        self.num_virtual_write += 1

        self.childs.append(value)
        
    # ------------------------------ Ajout d'un fils à l'indice donné ------------------------------
     
    def add_childs_idx(self, i, value):
        
        """
        Ajoute un noeud enfant à l'indice donné dans la liste des enfants.

        Paramètres:
        -----------
        i (int): l'indice de la position où ajouter le nœud enfant.
        value (Node): le noeud enfant à ajouter.
        """
        self.num_virtual_write += 1

        self.childs.insert(i, value)
        
    # ------------------------------  Position enfant pour la recherche  ------------------------------
     
    def childSearch(self, val):
        
        """
        Recherche l'indice approprié pour la valeur val en parcourant les clés pour la recherche d'une valeur

        Paramètres:
        -----------
        val (int): la valeur à insérer.

        Renvoie:
        --------
        int: l'indice de l'enfant où la clé de l'enfant est la plus grande clé inférieure à val
        """
        for i in range(len(self.keys)):
            if val < self.keys[i]:
                return i
        return len(self.keys)
    
    # ------------------------------  Recherche  ------------------------------
    
    def search(self, val):
        
        """
        Recherche une valeur donnée dans les noeuds.

        Paramètres:
        -----------
        val (int): la valeur à rechercher.

        Renvoie:
        --------
        bool: True si la valeur est trouvée dans les noeuds, False sinon.
        """
        
        self.num_virtual_reads += 1

        if len(self.keys) == 0: 
            return False
        elif val in self.keys:
            return True
        else:
            i = self.childSearch(val)
            if i < len(self.childs):
                res = self.childs[i].search(val)
                if res: 
                    return res
            return False
    

    def get_max(self):
        
        """
        Supprime et renvoie la plus grande clé dans le sous-arbre courant récursivement jusqu'à ce que le dernier enfant soit atteint.
        
        Renvoie:
        --------
        La plus grande clé dans le sous-arbre courant en descendant récursivement jusqu'à ce que le dernier enfant soit atteint.
        
        """
        
        if len(self.childs) == 0:
            return self.keys.pop()
        return self.childs[-1].get_max()

    def get_min(self):
        
        """
        Supprime et renvoie la plus petite clé dans le sous-arbre courant récursivement jusqu'à ce que le premier enfant soit atteint.
        
        Renvoie:
        --------
        La plus petite clé dans le sous-arbre courant en descendant récursivement jusqu'à ce que le premier enfant soit atteint.
        
        """
                
        if len(self.childs) == 0:
            return self.keys.pop(0)
        return self.childs[0].get_min()


