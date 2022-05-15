import string

def search(firEle, secEle, keyTable):
    firRow = 0
    firCol = 0
    secRow = 0
    secCol = 0
    for i in range(5):
        for j in range(5):
            if keyTable[i][j] == firEle:
                firRow = i
                firCol = j
            elif keyTable[i][j] == secEle:
                secRow = i
                secCol = j
    return firRow, firCol, secRow, secCol

def playFairEncrypt(plainText, keyTable):
    cipherText = ""
    
    for i in range(0,len(plainText),2):
        firEle = plainText[i]
        secEle = plainText[i+1]
        
        firRow, firCol, secRow, secCol = search(firEle, secEle, keyTable)
        
        if firRow == secRow:
            if firCol == 4:
                cipherText += keyTable[firRow][0]
            else:
                cipherText += keyTable[firRow][firCol + 1]
            
            if secCol == 4:
                cipherText += keyTable[secRow][0]
            else:
                cipherText += keyTable[secRow][secCol + 1]
                
        elif firCol == secCol:
            if firRow == 4:
                cipherText += keyTable[0][firCol]
            else:
                cipherText += keyTable[firRow+1][firCol]
            
            if secRow == 4:
                cipherText += keyTable[0][secCol]
            else:
                cipherText += keyTable[secRow+1][secCol]
                
        else:
            cipherText += keyTable[firRow][secCol]
            cipherText += keyTable[secRow][firCol]
    return cipherText

def seperateSameLetters(plainText):
    
    updatedPlainText = ""
    j = 0
    
    for i in range(0,len(plainText),2):
        j = i + 1
        print(i,j)
        if i == len(plainText)-1 and j == len(plainText):
            updatedPlainText += plainText[i]
            continue
        if plainText[i] == plainText[j]:
            updatedPlainText += plainText[i]
            updatedPlainText += 'x'
            updatedPlainText += plainText[j]
        else:
            updatedPlainText += plainText[i]
            updatedPlainText += plainText[j]
    #print("plain text: "+updatedPlainText)
    return updatedPlainText

def generateTable(key):
    
    table = [[0 for j in range(5)]for i in range(5)]
    keyAdded = []
    letters = list(string.ascii_lowercase)
    
    row = 0
    col = 0

    for ele in key:
        if ele not in keyAdded:
            table[row][col] = ele
            keyAdded.append(ele)
        else:
            continue
        
        if col == 4:
            col = 0
            row += 1
        else:
            col += 1
            
    #if "i" in keyAdded:
    #   keyAdded.append("j")
    #elif "j" in keyAdded:
    #    keyAdded.append("i")
        
    for ele in letters:
        if ele not in keyAdded:
            if ele == "j":
                continue
            table[row][col] = ele
        else:
            continue
        
        if col == 4:
            col = 0
            row += 1
        else:
            col += 1 
    print(table)
    return table

def checkIfEven(plainText):
    
    if len(plainText) % 2 != 0:
        plainText += 'z'
    return plainText

def encrypt(plainText, key):
    
    plainText = plainText.replace(" ","")
    key = key.replace(" ","")
    plainText = plainText.lower()
    key = key.lower()
    
    plainText = seperateSameLetters(plainText)

    plainText = checkIfEven(plainText)
    keyTable = generateTable(key)
    
    cipherText = playFairEncrypt(plainText, keyTable)
    
    return cipherText
    

plainText = input("Enter the plain text: ")
key = input("Enter the key: ")

if "i" in plainText and "j" in plainText:
    plainText = plainText.replace("j","i")
if "i" in key and "j" in key:
    key = key.replace("j","i")


cipherText = encrypt(plainText, key)
print("Text after encryption is: {}".format(cipherText))