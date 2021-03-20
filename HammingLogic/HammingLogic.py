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

    if totalParity%2 == 0:
        return error
        print ("P1 es par, no hay error")

    else:
        error += 1
        return error
        print ("Hay error en P1")

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

    if totalParity%2 == 0:
        return error
        print ("P2 es par, no hay error")

    else:
        error += 1
        return error
        print ("Hay error en P2")

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

    if totalParity%2 == 0:
        return error
        print ("P3 es par, no hay error")

    else:
        error += 1
        return error
        print ("Hay error en P3")

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

    if totalParity%2 == 0:
        return error
        print ("P4 es par, no hay error")

    else:
        error += 1
        return error
        print ("Hay error en P4")

def errorCheckForP5 (hammingData):
    
    error = 0
    
    totalParity = 0
    totalParity += hammingData[15]
    totalParity += hammingData[16]

    if totalParity%2 == 0:
        return error
        print ("P5 es par, no hay error")

    else:
        error += 1
        return error
        print ("Hay error en P5")

def calcularBitErroneo (hammingData):
    bitErroneo.append(errorCheckForP1(hammingData))
    bitErroneo.append(errorCheckForP2(hammingData))
    bitErroneo.append(errorCheckForP3(hammingData))
    bitErroneo.append(errorCheckForP4(hammingData))
    bitErroneo.append(errorCheckForP5(hammingData))

    print(bitErroneo)

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
    
bitErroneo = []
hammingData = [0,0,0,0,1,0,0,1,0,0,1,1,0,1,1,1,0]
print (len(hammingData))
    
    
