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

# Voici une manière de créer manuellement des arbres binaires
tree = Node(10, left=Node(5), right=Node(15))
'''
    10
   /  \
  5    15
'''