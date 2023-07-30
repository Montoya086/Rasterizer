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

def barycentricCoords(A, B, C, P):
    areaPCB = (B[1]-C[1])*(P[0]-C[0])+(C[0]-B[0])*(P[1]-C[1])
    
    areaACP = (C[1]-A[1])*(P[0]-C[0])+(A[0]-C[0])*(P[1]-C[1])
    
    areaABC = (B[1]-C[1])*(A[0]-C[0])+(C[0]-B[0])*(A[1]-C[1])

    try:
        u= areaPCB/areaABC
        v= areaACP/areaABC
        w= 1-u-v
        return u,v,w
    except:
        return -1,-1,-1

   