import sys
import string

def findCipher(mat, key, n):
    
    cipherMatrix = []
    for i in range(n):
        sum1 = 0
        for j in range(n):
            sum1 = sum1 + int(key[i][j]) * mat[j]
        cipherMatrix.append(sum1 % 26)
    
    return cipherMatrix

def validText(plainText, n):
    length = len(plainText) 
    
    
    
    if length % n != 0:
        
        rem = length % n
        numBef = length - rem
        numAfter = numBef + n
        
        for i in range(numAfter - length):
            plainText += 'x'
        
        
    return plainText
            

def encrypt():
    
    plainText = input("Enter the plaintext: ")
    if len(plainText) == 0:
        print("ENTER VALID STRING!!!")
        sys.exit()
    plainText = plainText.lower()
    plainText = plainText.replace(" ","")
    print(plainText)
    n = int(input("Enter the key size: "))
    
    plainText = validText(plainText, n)
    
    

    key = list()
    
    for i in range(n):
        arr = input("Enter the {}th key row elements: ".format(i)).split()
        key.append(arr)
    
    cipherText = ""
    
    letters = list(string.ascii_lowercase)
    
    for i in range(0,len(plainText),n):
        mat = []
        for j in range(i,n+i,1):
            mat.append(letters.index(plainText[j]))
        
        
        cipherMatrix = findCipher(mat, key, n)
        for k in range(n):
            cipherText += letters[cipherMatrix[k]]
    
    return cipherText
            
    
def decrypt():
    cipherText = input(("Enter the cipher text: "))
    cipherText = cipherText.replace(" ","")
    cipherText = cipherText.lower()
    
    n = int(input("Enter the key size: "))
    key = list()
    for i in range(n):
        arr = input("Enter the {}th key row elements: ".format(i)).split()
        for i in range(n):
          arr[i] = int(arr[i])
        key.append(arr)
    plainText = ""
    
    letters = list(string.ascii_lowercase)

    if n == 2:
        print(key)
        a = int(key[1][1])
        b = -int(key[0][1])
        c = -int(key[1][0])
        d = int(key[0][0])
        
        key[0][0] = a
        key[0][1] = b
        key[1][0] = c
        key[1][1] = d
        det = 1/(a*d-b*c)
        
        det = 1/det
        multiply = 0
        for k in range(100):
            if (k * det) % 26 == 1:
                multiply = k
                break
        for i in range(n):
            for j in range(n):
                key[i][j] = (key[i][j] * multiply) % 26
        #print(key)
    else:
        #adj
        det = 0
        det = ( ( key[0][0] * ( (key[1][1]*key[2][2]) - (key[2][1]*key[1][2]) ) ) 
              - ( key[0][1] * ( (key[1][0]*key[2][2]) - (key[2][0]*key[1][2]) ) ) 
              + ( key[0][2] * ( (key[1][0]*key[2][1]) - (key[2][0]*key[1][1]) ) ) 
              )
        
        det = 1/det
        multiply = 0
        for k in range(100):
            if (k * det) % 26 == 1:
                multiply = k
                break
        for i in range(n):
            for j in range(n):
                key[i][j] = (key[i][j] * multiply) % 26

    for i in range(0,len(cipherText),n):
        mat = []
        for j in range(i,n+i,1):
            mat.append(letters.index(cipherText[j]))
        
        
        plainMatrix = findCipher(mat, key, n)
        for k in range(n):
            plainText += letters[plainMatrix[k]]
    
    return plainText
    

choice = 0

while True:
    
    choice = int(input())
    if choice == 0:
        cipherText = encrypt()
        print("Encrypted text is : {}".format(cipherText))
    elif choice == 1:
        plainText = decrypt()
        print("Decrypted text is : {}".format(plainText))
    else:
        sys.exit()
