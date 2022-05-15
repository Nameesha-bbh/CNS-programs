def encrypt(n):

	plainText = input("Enter the text to be encrypted: ")
	cipherText = ""

	for letter in plainText:
		if letter == " ":
			cipherText += " "
			continue
		asciiValue = ord(letter)
		
		if letter.isupper():
			asciiValue =  asciiValue - ord('A')
			asciiValue += n 
			asciiValue = asciiValue % 26
			cipherText += chr(asciiValue + ord('A'))
		else:	
			asciiValue =  asciiValue - ord('a')
			asciiValue += n 
			asciiValue = asciiValue % 26
			cipherText += chr(asciiValue + ord('a'))
	
	print("Encrypted text is: {}".format(cipherText))
	print("")
	return 0

def decrypt(n):
	cipherText = input("Enter the encrypted text: ")
	plainText = ''
	
	for letter in cipherText:
		if letter == " ":
			plainText += " "
			continue
		asciiValue = ord(letter)
		
		if letter.isupper():
			asciiValue =  asciiValue - ord('A')
			asciiValue -= n 
			asciiValue = asciiValue % 26
			plainText += chr(asciiValue + ord('A'))
		else:	
			asciiValue =  asciiValue - ord('a')
			asciiValue -= n 
			asciiValue = asciiValue % 26
			plainText += chr(asciiValue + ord('a'))
	
	print("Decrypted text is: {}".format(plainText))
	print("")
	return 0
	

n = int(input("Enter shift value: "))
choice = 0

while(choice != 3):	
	choice = int(input("Enter the function to be performed (1: Encrypt, 2: Decrypt, 3: End): "))
	if choice == 1:
		encrypt(n)
	elif choice == 2:
		decrypt(n)
	elif choice == 3:
		break
	else:
		print("WRONG CHOICE")
		continue
