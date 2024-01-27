from socket import *
import sys
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Cryptodome.Cipher import AES



PORT_NUMBER = int(input())


serverSock = socket(AF_INET, SOCK_STREAM) 
serverSock.bind(('', PORT_NUMBER)) 
serverSock.listen(100)




while True:

	print("Waiting for clients to connect...")
	cliSock, cliInfo = serverSock.accept()
	print("Client connected from: " + str(cliInfo))
	cliMsg = cliSock.recv(16)	
	print("Client sent " + str(cliMsg.decode()))
	key = b'128 bit key'
	#encCipher = AES.new(key, AES.MODE_ECB)
	#cipherText = encCipher.encrypt('h4jlf123fj676s0d1114311150114s11f2')
	#print("Cipher text: ", key)
	decCipher = AES.new(key, AES.MODE_ECB)
	plainText = decCipher.decrypt(cliMsg)
	#unpaddedDecryptedText = unpad(plainText,16)
	print("Decrypted text: ", plainText)
	cliSock.close()





