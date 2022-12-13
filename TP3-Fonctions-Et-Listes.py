"""
1. Ecrire une fonction listeAleatoire qui prend un entier n en argument et renvoie une liste de
taille n contenant des nombres entre 1 et 10 tirés au hasard. Vous utiliserez pour ce faire la
fonction randint(a,b) du module random.
"""
from random import randint

def listeAleatoire(n):
   l=[]
   for i in range(n):
      l=l+[randint(i,n)]
   return l


"""   
2. Ecrire un programme qui crée une liste de taille 20 avec la fonction
listeAleatoire et l’affiche.
"""
L=listeAleatoire(20)
print("L =",L)
print("\n\n")
"""
3. Ecrire une fonction maxListe qui prend une liste L en argument et renvoie le plus
grand entier apparaissant dans la liste. Par exemple, maxListe([1,2,4,1]) renverra 4.
"""
def maxListe(l):
   m=l[0]
   for i in range(len(l)):
      if m<l[i]:
         m=l[i]
   return m

"""
4. Compléter le programme de la question 2 pour qu’il affiche en plus le maximum de la liste.
"""
print("Le Max est : ",maxListe(L))
print("\n\n")
"""
5. Ecrire une fonction singletons qui prend une liste d’entiers et renvoie la liste contenant
les mêmes nombres mais au plus une fois et dans le même ordre.
Par exemple, singletons([2,1,2,1,3,2,1,4] renverra la liste [2,1,3,4].
"""
def singletons(l):
   L=[]
   for i in l:
      if i not in L:
         L.append(i)
   return L

"""
6. Compléter le programme de la question 4 pour qu’il affiche en plus la liste sans doublons.
"""

l=singletons(L)
print("la liste sans répititions :",l)
print("\n\n")


"""
7. Ecrire une fonction nbOccurences qui prend un nombre n et une liste L et renvoie le nombre de 
fois que l’entier n apparaît dans la liste L.
Par exemple :
nbOccurences(1,[1,2,4,1])==> 2 
nbOccurences(5,[1,2,4,1])==> 0
nbOccurences(2,[1,2,4,1])==> 1
"""
def nbOccurences(l,n):
   compteur=0
   for i in l:
      if n==i:
         compteur+=1
   return compteur

"""
8. Compléter le programme de la question 6 pour qu’il affiche pour chaque élément de la
liste le nombre de fois où il apparaît dans la liste.
"""

for i in range(len(l)):
   print(l[i]," apparait ",nbOccurences(L,l[i])," fois ")
print("\n\n")

"""
9. Ecrire une fonction plusFrequent qui prend une liste L d’entiers en argument et qui
renvoie le nombre qui apparaît le plus de fois dans la liste. Si plusieurs nombres
sont possibles, on renverra le plus grand.
"""

def plusFrequent(l):
   p=nbOccurences(l,l[0])
   plusfrequent=L[0]
   for i in range(len(l)):
      if p < nbOccurences(l,l[i]):
         plusfrequent=l[i]
         p=nbOccurences(l,l[i])
      
      if p==nbOccurences(l,l[i]) and plusfrequent<l[i]:
         plusfrequent=l[i]
         p=nbOccurences(l,l[i])
   return plusfrequent

print("le nombre qui apparaît le plus de fois dans la liste ",plusFrequent(L))
         
         
   










   
