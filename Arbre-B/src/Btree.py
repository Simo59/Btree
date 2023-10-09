from Node import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import graphviz
from graphviz import Digraph

class Btree:
    
    """
    Implémentation d'une structure de données : Arbre-B.

    Attributs:
    ----------
    L : int
        La taille minimale de fils et de L-1 clés dans chaque noeud de l'arbre B.
    U : int
        La taille maximale de fils et de U-1 clés dans chaque noeud de l'arbre B.
    root : Node
        Le noeud racine de l'arbre B.

    Méthodes:
    --------
    __init__(self, L, U): Initialise un nouvel arbre B avec une taille minimale L de fils et de L-1 clés et une taille maximale U de fils et de U-1 clés.
    search(self, value): Recherche la valeur spécifiée dans l'arbre B.
    insert(self, value): Insère la valeur spécifiée dans l'arbre B.
    _insert(self, node, value): Insère la valeur spécifiée dans le noeud spécifié de l'arbre B.
    _split_child(self, parent, child): Divise le noeud enfant spécifié du noeud parent spécifié en deux noeud distincts.
    delete(self, value) : Supprime la clé spécifiée de l'arbre B. Appelle la méthode privée _delete.
    _delete(self, node, value) : Supprime la clé du sous-arbre dans le noeud. Cette méthode est appelée de manière récursive pour rechercher la clé à supprimer et effectuer la suppression.
    display(self, node=None, dot=None): Affiche l'arbre B.
    
    """
   
    # ------------------------------ Constructeur ------------------------------
    
    def __init__(self, L, U):
        
        """
        Initialise un nouvel arbre B avec une taille minimale L de fils et de L-1 clés et une taille maximale U de fils et de U-1 clés.

        Paramètres:
        -----------
        L : int
            La taille minimale de fils et de L-1 clés dans chaque noeud de l'arbre B.
        U : int
            La taille maximale de fils et de U-1 clés dans chaque noeud de l'arbre B.
        """
       
        self.L = L
        self.U = U
        self.root = Node()

    # ------------------------------ Recherche ------------------------------
    
    def search(self, value):
        
        """
        Recherche la valeur spécifiée dans l'arbre B.

        Paramètres:
        -----------
        value : int
            La valeur à rechercher.

        Renvoie:
        --------
        bool : True si la valeur est trouvée, False sinon.
        """
        
        found = self.root.search(value)
        if found:
            return True
        else:
            for child in self.root.childs:
                res = child.search(value)
                if res:
                    return True
        return False
    
    # ------------------------------ Insertion ------------------------------
    
    def insert(self, value):
        
        """
        Insère la valeur spécifiée dans l'arbre B.

        Paramètres:
        -----------
        value : int
            La valeur à insérer.
        """
        if self.search(value) == False :
            
            self._insert(self.root, value)
            
            if len(self.root.keys) > self.U -1 :
                new_root = Node()
                new_root.add_childs(self.root)
                self._split_child(new_root, self.root)
                self.root = new_root


    def _insert(self, node, value):
        
        """
        Insère la valeur spécifiée dans le noeud spécifié de l'arbre B.

        Paramètres:
        -----------
        node : Node
            Le noeud dans lequel insérer la valeur.
        value : int
            La valeur à insérer.
        """
        
        i = node.childSearch(value)
        
        if len(node.childs) == 0:
            node.add_key(value)
        else:
            child = node.childs[i]
            self._insert(child, value)
            
            if len(child.keys) > self.U -1 :
                self._split_child(node, child)

    def _split_child(self, parent, child):
            
        """
        Divise le noeud enfant spécifié du noeud parent spécifié en deux noeud distincts.
        
        Paramètres :
        ------------
        parent : Node
            Le noeud parent dans lequel est situé le noeud enfant à diviser.
        child : Node
            Le noeud enfant à diviser.
        """
        
        # Nouveau noeud pour stocker les clés les plus grandes
        new_child = Node()
        mid = len(child.keys) // 2
        milieu = child.keys[mid]
        new_child.keys = child.keys[mid+1:]
        child.keys = child.keys[:mid]
        
        if len(child.childs) > 0:
            new_child.childs = child.childs[mid+1:]
            child.childs = child.childs[:mid+1]
        
        i = parent.add_key(milieu)
        
        parent.add_childs_idx(i+1,new_child)

    # ------------------------------ Supprimer ------------------------------
    
    def delete(self, value):
        
        """
        Supprime la clé spécifiée de l'arbre B. Appelle la méthode privée _delete
        
        Paramètres :
        ------------
        value : int
            La valeur à supprimer de l'arbre. 
        """

        if self.search(value):
            self._delete(self.root, value)

            if len(self.root.keys) == 0 and len(self.root.childs) > 0:
                self.root = self.root.childs[0]

    def _delete(self, node, value):
        
        """
        Supprime la clé du sous-arbre dans le noeud. Cette méthode est appelée de manière récursive pour rechercher la clé à supprimer et effectuer la suppression.
        
        Paramètres :
        ------------
        node : Node
            Le noeud du sous arbre où l'on part pour la recherche. 
        value : int
            La valeur à supprimer de l'arbre. 
        """

        if value in node.keys:
            idx = node.keys.index(value)

            if len(node.childs) == 0:  # Noeud feuille
                node.keys.pop(idx)
            else:
                if len(node.childs[idx].keys) >= self.L:  # Juste avant
                    node.keys[idx] = node.childs[idx].get_max()
                    self._delete(node.childs[idx], node.keys[idx])
                elif len(node.childs[idx + 1].keys) >= self.L:  # Juste aorès
                    node.keys[idx] = node.childs[idx + 1].get_min()
                    self._delete(node.childs[idx + 1], node.keys[idx])
                else:  # Fusionner
                    node.childs[idx].keys.extend([node.keys.pop(idx)] + node.childs[idx + 1].keys)
                    node.childs[idx].childs.extend(node.childs[idx + 1].childs)
                    node.childs.pop(idx + 1)
                    self._delete(node.childs[idx], value)
        else:
            idx = node.childSearch(value)
            if len(node.childs[idx].keys) <= self.L - 1:  # Cas où le Noeud a le nombre minimum de clés
                if idx > 0 and len(node.childs[idx - 1].keys) >= self.L:
                    node.childs[idx].keys.insert(0, node.keys[idx - 1])
                    node.keys[idx - 1] = node.childs[idx - 1].keys.pop()
                    if node.childs[idx - 1].childs:
                        node.childs[idx].childs.insert(0, node.childs[idx - 1].childs.pop())
                elif idx < len(node.childs) - 1 and len(node.childs[idx + 1].keys) >= self.L:
                    node.childs[idx].keys.append(node.keys[idx])
                    node.keys[idx] = node.childs[idx + 1].keys.pop(0)
                    if node.childs[idx + 1].childs:
                        node.childs[idx].childs.append(node.childs[idx + 1].childs.pop(0))
                else:  # Fusionner
                    if idx > 0:
                        idx -= 1
                    node.childs[idx].keys.extend([node.keys.pop(idx)] + node.childs[idx + 1].keys)
                    node.childs[idx].childs.extend(node.childs[idx + 1].childs)
                    node.childs.pop(idx + 1)

            self._delete(node.childs[idx], value)


    # ------------------------------ Affichage ------------------------------
    
    def display(self, node=None, dot=None):
        
        """
        Affiche l'arbre B.

        Paramètres:
        -----------
        node : Node, optionnel
            Le noeud à partir duquel afficher l'arbre. Si node=None, l'affichage commence à la racine de l'arbre.
        dot : Digraph, optionnel
            L'objet Digraph utilisé pour afficher l'arbre. Si dot=None, un nouvel objet Digraph est créé.
        """
        
        if node is None:
            node = self.root
        if dot is None:
            dot = Digraph(format='png')
        dot.node(str(id(node)), label=str(node.keys))
        for child in node.childs:
            dot.edge(str(id(node)), str(id(child)))
            self.display(child, dot)

        dot.render('btree')
        image = mpimg.imread("btree.png")
        return image


# ------------------------------------------------------------ Arbre Main  ------------------------------------------------------------

if __name__ == "__main__":

  
    btree = Btree(2, 3)
    
    btree.insert(2)
    btree.insert(4)
    btree.insert(5)
    btree.insert(6)        
    btree.insert(8)
    btree.insert(10)
    btree.insert(12)
    btree.insert(14)
    btree.insert(16)
    btree.insert(18)
    


    # AFFICHAGE
    image = btree.display()
    plt.imshow(image)
    plt.show()
