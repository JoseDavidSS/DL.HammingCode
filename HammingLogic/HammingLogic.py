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

    if par == True:
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

    if par == True:
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

    if par == True:
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

    if par == True:
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

    if par == True:
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
    

par = True
hammingData = [1,1,1,1,1,0,0,0,1,0,0,1,1,0,1,1,1]
print (len(hammingData))
    
    
