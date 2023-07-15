def nMatMult(mats):
    res = [[1,0,0,0],
           [0,1,0,0],
           [0,0,1,0],
           [0,0,0,1]]
    
    for mat in mats:
        res = matMult(res,mat)
    return res

def matMult(m1,m2):
    res = [[0,0,0,0],
           [0,0,0,0],
           [0,0,0,0],
           [0,0,0,0]]
    for x in range(4):
        for y in range(4):
            for i in range(4):
                res[x][y] += m1[x][i] * m2[i][y]
    return res

def matVectMult(mat, vect):
    res = [0,0,0,0]
    for x in range(4):
        for y in range(4):
                res[x] += mat[x][y] * vect[y]
    return res