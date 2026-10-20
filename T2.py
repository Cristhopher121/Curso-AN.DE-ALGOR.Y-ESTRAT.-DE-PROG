def imprime(mat):
    for x in mat:
        print(x)
    print()
 
 
def valido(lab, res, f, c):
    if f >= len(lab):
        return False
    if f < 0:
        return False
    if c >= len(lab[0]):
        return False
    if c < 0:
        return False
    if res[f][c] == 1:
        return False
    if lab[f][c] == 0:
        return False
    return True
 
 
def puntos(lab, res):
    for f in range(len(lab)):
        for c in range(len(lab[0])):
            if res[f][c] == 1 and lab[f][c] in (3, 4):
                total += lab[f][c]
    return total
 
 
def laberB(lab, res, f, c):
    if f == 0 and c == 0:
        if valido(lab, res, f, c):
            res[f][c] = 1
            imprime(res)       
            if puntos(lab, res) >= 23:
                return True
            res[f][c] = 0      
            return False
        else:
            return False
    else:
        if valido(lab, res, f, c):
            res[f][c] = 1
            imprime(res)       
            if laberB(lab, res, f-1, c):
                return True
            elif laberB(lab, res, f, c+1):
                return True
            elif laberB(lab, res, f+1, c):
                return True
            elif laberB(lab, res, f, c-1):
                return True
            else:
                res[f][c] = 0
                return False
        else:
            return False
 


lab = [
    ['F', 1, 1, 3, 0, 1, 1, 1, 4],
    [3, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 3, 1, 1],
    [3, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 3, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 4],
    ['I', 1, 3, 1, 0, 1, 1, 1, 1]
]
res = [[0 for _ in range(9)] for _ in range(9)]


if laberB(lab, res, 8, 0):
    print("=== MATRIZ SOLUCIÓN ===")
    imprime(res)
    print("Puntos:", puntos(lab, res))
    print("Salimos!")
else:
    print("Quedamos atrapados")