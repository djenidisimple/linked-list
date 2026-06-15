# I learn data structure and algorithm, and I want to implement tree data structure in python. I will implement tree using class and object.
# vocabulary:
# Node : contient les donnees qui peuvent etre des nombres, textes ou d'autres objets, et une liste de ses enfants.
# Root : Tout premier noeud d'un arbre, qui n'a pas de parent.
# Children and Parent : Si un node A pointe vers un node B, alors B est un enfant de A.
# Leaves : node qui n'a pas d'enfant.
# Edges : les connexions entre les nodes.
# Height : la distance maximale entre la racine et une feuille.
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def parcours_infixe(node):
    if node is None:
        return
    parcours_infixe(node.left)

    print(node.value, end=" ")
    
    parcours_infixe(node.right)

def parcours_prefixe(node):
    if node is None:
        return
    print(node.value, end=" ")
    parcours_prefixe(node.left)
    parcours_prefixe(node.right)

def parcours_postfixe(node):
    if node is None:
        return
    parcours_postfixe(node.left)
    parcours_postfixe(node.right)
    print(node.value, end=" ")

def bfs(node):
    pass

# Voici une manière de créer manuellement des arbres binaires
tree = Node(10, left=Node(5), right=Node(15))
parcours_infixe(tree)
print("")
parcours_prefixe(tree)
print("")
parcours_postfixe(tree)
'''
    10
   /  \
  5    15
'''