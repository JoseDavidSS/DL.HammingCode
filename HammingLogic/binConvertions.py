def bin2dec(binNumber):
    dec = str(int(binNumber, 2))
    return dec

def bin2hex(binNumber):
    hexa = hex(int(binNumber,2))
    hexa = hexa[2:]
    return hexa

def bin2oct(binNumber):
    octa = oct(int(binNumber, 2))
    octa = octa[2:]
    return octa