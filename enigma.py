"""

Aternative usage directly from python env :
>>> Rotors = <put rotors here>

>>> code(message, clef)
>>> decode(message, clef)

clef : string made of chars from alphabet (best length = number of rotors)
alphabet : all available chars (can be completed as necessary)
"""




import random as rd

Rotors = []
alphabet = """0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzéèêëàâäîïôöûüù-,.?;:!()'" \n"""
N = len(alphabet)
T = [k for k in range(N)]
nRotors = 10

cle = "defaut"



def melange(L1):
    L = L1[::]
    l = []
    while L:
        l.append(L.pop(rd.randint(0, len(L)-1)))
    return l



def crypt(k, rotors):
    for i in range(len(rotors)):
        k = rotors[i][k]
    tick(rotors)
    return k

def decrypt(k, rotors):
    n = len(rotors)
    for i in range(n):
        k = rotors[n-1-i].index(k)
    tick(rotors)
    return k

def creaRotors():
    Rotors = []
    for k in range(nRotors):
        Rotors.append(melange(T))
    return Rotors


#Rotors = creaRotors()
#Rotors = [[1, 35, 44, 66, 72, 33, 38, 17, 79, 20, 45, 23, 32, 67, 39, 51, 30, 57, 7, 87, 75, 54, 73, 40, 58, 0, 74, 56, 76, 9, 42, 22, 50, 36, 53, 48, 61, 52, 83, 78, 49, 10, 80, 84, 60, 68, 2, 34, 55, 41, 64, 31, 28, 81, 77, 43, 15, 37, 85, 71, 25, 70, 59, 5, 63, 3, 82, 27, 88, 65, 21, 47, 26, 4, 69, 86, 16, 11, 19, 12, 24, 13, 14, 62, 46, 29, 8, 18, 6], [6, 50, 40, 17, 74, 43, 72, 46, 15, 59, 85, 54, 38, 76, 9, 86, 69, 61, 7, 48, 77, 21, 75, 55, 62, 45, 1, 49, 36, 29, 34, 22, 80, 35, 57, 83, 42, 82, 8, 5, 33, 51, 3, 84, 65, 39, 11, 81, 47, 32, 71, 41, 31, 68, 18, 30, 27, 12, 26, 4, 79, 14, 24, 20, 58, 13, 78, 67, 37, 87, 16, 52, 66, 64, 23, 10, 73, 53, 25, 88, 56, 44, 60, 19, 70, 2, 63, 28, 0], [56, 44, 7, 39, 0, 23, 50, 86, 38, 22, 17, 32, 21, 25, 8, 42, 9, 30, 19, 40, 4, 61, 26, 63, 65, 75, 59, 34, 48, 46, 72, 20, 43, 57, 78, 74, 71, 3, 70, 83, 52, 37, 28, 80, 51, 82, 45, 18, 15, 68, 36, 53, 81, 33, 87, 62, 13, 27, 58, 12, 88, 47, 2, 66, 54, 76, 29, 85, 24, 69, 5, 49, 1, 84, 55, 11, 79, 6, 67, 14, 64, 35, 73, 60, 10, 16, 31, 41, 77], [59, 54, 72, 52, 39, 7, 55, 34, 71, 30, 62, 42, 35, 0, 83, 88, 81, 75, 17, 36, 87, 85, 9, 74, 73, 27, 4, 5, 47, 49, 26, 6, 18, 60, 40, 46, 13, 57, 19, 66, 67, 82, 84, 33, 56, 53, 41, 10, 50, 65, 12, 1, 29, 58, 31, 45, 38, 37, 3, 44, 11, 86, 80, 20, 21, 28, 32, 14, 64, 22, 63, 23, 68, 78, 15, 2, 24, 51, 16, 69, 43, 76, 79, 48, 77, 8, 25, 70, 61], [80, 8, 36, 72, 47, 87, 50, 58, 77, 84, 74, 76, 2, 27, 88, 0, 10, 79, 46, 37, 18, 78, 44, 25, 31, 35, 41, 53, 86, 11, 24, 52, 73, 26, 82, 48, 3, 83, 65, 70, 14, 64, 33, 30, 55, 28, 6, 75, 5, 9, 81, 56, 71, 16, 34, 68, 49, 1, 17, 20, 62, 4, 59, 54, 12, 19, 23, 57, 63, 69, 67, 51, 40, 39, 45, 7, 32, 66, 42, 21, 38, 43, 13, 22, 15, 85, 61, 60, 29], [70, 71, 22, 61, 69, 11, 2, 16, 83, 60, 6, 51, 3, 56, 76, 41, 86, 64, 66, 33, 32, 65, 77, 82, 24, 7, 63, 67, 84, 58, 88, 0, 26, 29, 19, 87, 35, 21, 27, 10, 49, 36, 39, 54, 14, 37, 45, 81, 30, 53, 15, 8, 72, 55, 68, 85, 28, 74, 44, 25, 46, 9, 23, 50, 48, 42, 80, 31, 4, 62, 20, 78, 73, 34, 18, 12, 57, 1, 79, 40, 52, 43, 75, 5, 17, 13, 38, 59, 47], [78, 4, 25, 57, 39, 67, 47, 77, 33, 75, 44, 60, 81, 43, 0, 6, 42, 71, 55, 76, 3, 7, 21, 85, 24, 41, 20, 80, 29, 87, 22, 54, 48, 32, 84, 40, 58, 12, 8, 72, 86, 52, 1, 38, 49, 51, 65, 82, 53, 30, 56, 15, 2, 35, 69, 28, 5, 23, 31, 46, 14, 26, 74, 63, 10, 18, 59, 19, 36, 16, 37, 64, 70, 13, 50, 34, 61, 9, 17, 11, 27, 45, 88, 83, 73, 66, 79, 62, 68], [5, 41, 64, 44, 14, 4, 38, 75, 77, 31, 63, 13, 51, 9, 3, 8, 6, 73, 40, 57, 50, 82, 83, 39, 20, 19, 46, 74, 49, 1, 30, 26, 11, 32, 48, 72, 43, 70, 60, 28, 59, 35, 23, 69, 37, 56, 52, 71, 67, 16, 42, 61, 86, 76, 2, 68, 24, 53, 34, 62, 54, 80, 22, 87, 88, 78, 27, 81, 17, 47, 79, 65, 25, 18, 29, 66, 33, 55, 84, 21, 15, 12, 58, 7, 45, 36, 0, 85, 10], [74, 59, 47, 56, 66, 60, 8, 46, 48, 68, 81, 14, 34, 32, 70, 3, 72, 84, 38, 43, 11, 61, 40, 21, 71, 25, 30, 36, 19, 0, 18, 4, 5, 23, 58, 80, 53, 65, 63, 17, 76, 78, 64, 86, 49, 79, 88, 24, 41, 83, 69, 87, 27, 50, 20, 39, 9, 2, 6, 1, 31, 57, 42, 45, 10, 12, 82, 16, 26, 22, 44, 29, 52, 77, 13, 54, 55, 67, 35, 15, 28, 51, 7, 62, 85, 33, 75, 37, 73], [2, 61, 40, 54, 24, 0, 86, 42, 33, 66, 72, 43, 23, 55, 34, 7, 31, 63, 82, 50, 62, 9, 88, 67, 21, 85, 27, 78, 64, 5, 70, 73, 11, 12, 20, 44, 35, 57, 65, 30, 26, 59, 84, 83, 39, 38, 3, 75, 16, 77, 60, 8, 41, 79, 87, 68, 28, 71, 80, 15, 25, 14, 47, 58, 81, 69, 4, 1, 29, 46, 36, 18, 53, 32, 51, 17, 19, 45, 52, 76, 49, 10, 56, 13, 48, 22, 37, 74, 6]]


def rotation(L):
    x = L.pop()
    L.insert(0,x)
    return L

def tick(rotors):
    b = 1
    i = 0
    n = len(rotors)
    while b and i < n:
        rotation(rotors[n-1-i])
        if rotors[n-1-i][0] != 0:
            b = 0
        i += 1
    return rotors

def toLisible(L):
    l = ""
    for i in L:
        l = l + alphabet[i]
    return l


def toChiffre(L):
    l = []
    for i in L:
        l.append(alphabet.index(i))
    return l

def code(entree,clef,rotors):
    placer(clef, rotors)
    E = toChiffre(entree)
    S = []
    for i in range(len(E)):
        S.append(crypt(E[i], rotors))
    return toLisible(S)

def decode(entree,clef, rotors):
    placer(clef, rotors)
    E = toChiffre(entree)
    S = []
    for i in range(len(E)):
        S.append(decrypt(E[i], rotors))
    return toLisible(S)
"""
def placer(clef):
    if len(clef) != len(Rotors):
        raise Exception("clef invalide")
    else:
        c = toChiffre(clef)
        for k in range(len(Rotors)):
            while Rotors[k][c[k]] != 0:
                rotation(Rotors[k])
    return Rotors
"""

def placer(clef, rotors):
    copie = clef
    while len(clef) < len(rotors): #clef trop courte -> concaténation
        clef = clef + copie
    else:
        c = toChiffre(clef)
        for k in range(len(rotors)):
            while rotors[k][c[k]] != 0:
                rotation(rotors[k])
    return rotors
