paridad = False
print("paridad:")
print(paridad)

def checkParidad(p):
    global paridad
    suma = 0
    for i in p:
        suma += int(i)
    if paridad:
        if suma % 2 == 0:
            p = "0" + p
        else:
            p = "1" + p
    else:
        if suma % 2 == 0:
            p = "1" + p
        else:
            p = "0" + p
    return p

def hamming(entrada):
    data = list(entrada)



    mat = [["" for y in range(17)] for x in range(7)]
    d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12 = [i for i in data]

    p1 = checkParidad(d1 + d2 + d4 + d5 + d7 + d9 + d11 + d12)
    p2 = checkParidad(d1 + d3 + d4 + d6 + d7 + d10 + d11)
    p3 = checkParidad(d2 + d3 + d4 + d8 + d9 + d10 + d11)
    p4 = checkParidad(d5 + d6 + d7 + d8 + d9 + d10 + d11)
    p5 = checkParidad(d12)

    pList = [p1, p2, p3, p4, p5]
    c = 1
    cont = 0

    # Linea Original
    for x in range(17):
        if x == 2 ** c:
            for y in range(2 ** c - 1):
                if cont < 12:
                    mat[0][x + y] = data[cont]
                    cont += 1
            c += 1

    # For para llenar la tabla con los p
    for i in range(1, 6):  # Dejar la primera linea como esta
        p = (2 ** (i - 1) - 1)  # el -1 de la i es para compensar lo anterior
        escribir = True
        for j in range(17):
            if (j == p):
                casilla = 0
                cont = 0
                for k in range(p, 17):
                    if escribir:
                        mat[i][k] = pList[i - 1][cont]
                        cont += 1
                        casilla += 1
                    else:
                        casilla += 1
                    if casilla >= p + 1:
                        casilla = 0
                        escribir = not escribir
    # Resultado
    mat[6][0] = p1[0]
    mat[6][1] = p2[0]
    mat[6][3] = p3[0]
    mat[6][7] = p4[0]
    mat[6][15] = p5[0]

    cont = 0
    for j in mat[6]:
        if j == "":
            mat[6][cont] = mat[0][cont]
        cont += 1

    return mat

def errorCheckForP1 (hammingData):
    
    error = 0
    
    totalParity = 0
    totalParity += hammingData[0]
    totalParity += hammingData[2]
    totalParity += hammingData[4]
    totalParity += hammingData[6]
    totalParity += hammingData[8]
    totalParity += hammingData[10]
    totalParity += hammingData[12]
    totalParity += hammingData[14]
    totalParity += hammingData[16]

    print(totalParity)

    if paridad == True:
        if totalParity%2 == 0:
            print ("P1 es par, no hay error")
            return error
        else:
            error += 1
            print ("Hay error en P1 porque es impar")
            return error
    
    else:
        if totalParity%2 != 0:
            print ("P1 es impar, no hay error")
            return error
        else:
            error += 1
            print ("Hay error en P1 porque es par")
            return error

def errorCheckForP2 (hammingData):
    
    error = 0
    
    totalParity = 0
    totalParity += hammingData[1]
    totalParity += hammingData[2]
    totalParity += hammingData[5]
    totalParity += hammingData[6]
    totalParity += hammingData[9]
    totalParity += hammingData[10]
    totalParity += hammingData[13]
    totalParity += hammingData[14]

    if paridad == True:
        if totalParity%2 == 0:
            print ("P2 es par, no hay error")
            return error
        else:
            error += 1
            print ("Hay error en P2 porque es impar")
            return error
    
    else:
        if totalParity%2 != 0:
            print ("P2 es impar, no hay error")
            return error
        else:
            error += 1
            print ("Hay error en P2 porque es par")
            return error

def errorCheckForP3 (hammingData):
    
    error = 0
    
    totalParity = 0
    totalParity += hammingData[3]
    totalParity += hammingData[4]
    totalParity += hammingData[5]
    totalParity += hammingData[6]
    totalParity += hammingData[11]
    totalParity += hammingData[12]
    totalParity += hammingData[13]
    totalParity += hammingData[14]

    if paridad == True:
        if totalParity%2 == 0:
            print ("P3 es par, no hay error")
            return error
        else:
            error += 1
            print ("Hay error en P3 porque es impar")
            return error
    
    else:
        if totalParity%2 != 0:
            print ("P3 es impar, no hay error")
            return error
        else:
            error += 1
            print ("Hay error en P3 porque es par")
            return error

def errorCheckForP4 (hammingData):
    
    error = 0
    
    totalParity = 0
    totalParity += hammingData[7]
    totalParity += hammingData[8]
    totalParity += hammingData[9]
    totalParity += hammingData[10]
    totalParity += hammingData[11]
    totalParity += hammingData[12]
    totalParity += hammingData[13]
    totalParity += hammingData[14]

    if paridad == True:
        if totalParity%2 == 0:
            print ("P4 es par, no hay error")
            return error
        else:
            error += 1
            print ("Hay error en P4 porque es impar")
            return error
    
    else:
        if totalParity%2 != 0:
            print ("P4 es impar, no hay error")
            return error
        else:
            error += 1
            print ("Hay error en P4 porque es par")
            return error

def errorCheckForP5 (hammingData):
    
    error = 0
    
    totalParity = 0
    totalParity += hammingData[15]
    totalParity += hammingData[16]

    if paridad == True:
        if totalParity%2 == 0:
            print ("P5 es par, no hay error")
            return error
        else:
            error += 1
            print ("Hay error en P5 porque es impar")
            return error
    
    else:
        if totalParity%2 != 0:
            print ("P5 es impar, no hay error")
            return error
        else:
            error += 1
            print ("Hay error en P5 porque es par")
            return error

def calcularBitErroneo (hammingData):
    bitErroneo = []
    bitErroneo.append(errorCheckForP1(hammingData))
    bitErroneo.append(errorCheckForP2(hammingData))
    bitErroneo.append(errorCheckForP3(hammingData))
    bitErroneo.append(errorCheckForP4(hammingData))
    bitErroneo.append(errorCheckForP5(hammingData))
    return bitErroneo

def cambiarBit (posicion):
    
    posicion -= 1
    if hammingData[posicion] == 0:
        print(hammingData)
        hammingData[posicion] = 1
        print(hammingData)
        print("bit cambiado a 1")
        
    else:
        print(hammingData)
        hammingData[posicion] = 0
        print(hammingData)
        print("bit cambiado a 0")

hammingData = [1,1,1,1,1,0,0,0,1,0,0,1,1,0,1,1,1]
print (len(hammingData))
    
    
