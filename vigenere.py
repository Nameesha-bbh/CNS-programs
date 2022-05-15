import string

def encrypt():
    
    cipherText = ""
    plainText = input("Enter the text to be encrypted: ")
    key = input("Enter the key: ")
    
    plainText = plainText.replace(" ","")
    plainText = plainText.lower()
    key = key.replace(" ","")
    key = key.lower()
    
    keyLen = len(key)
    letters = list(string.ascii_lowercase)
    
    for i in range(len(plainText)):
        
        keyIndex = i % keyLen
        cipherValue = letters.index(plainText[i]) + letters.index(key[keyIndex])
        cipherValue %= 26
        cipherText += letters[cipherValue]
        
    print("The cipher text is: {}".format(cipherText))

def decrypt():
    plainText = ""
    cipherText = input("Enter the text to be decrypted: ")
    key = input("Enter the key: ")
    
    cipherText = cipherText.replace(" ","")
    cipherText = cipherText.lower()
    key = key.replace(" ","")
    key = key.lower()
    
    keyLen = len(key)
    letters = list(string.ascii_lowercase)
    
    for i in range(len(cipherText)):
        
        keyIndex = i % keyLen
        plainValue = letters.index(cipherText[i]) - letters.index(key[keyIndex])
        plainValue %= 26
        plainText += letters[plainValue]
        
    print("The decrypted text is: {}".format(plainText))

choice = 0

while True:
    choice = int(input("Enter the choice (1: Encrypt, 2: Decrypt): "))
    
    if choice == 1:
        encrypt()
    elif choice == 2:
        decrypt()
    else: 
        break