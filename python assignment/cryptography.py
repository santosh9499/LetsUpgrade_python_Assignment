
from cryptography.fernet import Fernet

def genratePassKey():
    key = Fernet.generate_key()
    print(key)
    print(type(key))
    abc = open("PasswordKey.key",'wb')
    abc.write(key)
    abc.close()
print(genratePassKey())

def getMyKey():
    abc = open("PasswordKey.key",'rb')
    return abc.read()
    print(getMyKey())

def getContentFromUser():
    return input("Enter the Content you want to Encrypt in your code: ")

getContentFromUser()
   
def encryptMessage(message_normal):
    key = getMyKey()
    k = Fernet(key)
    encrypted_Message = k.encrypt(message_normal)
    return encrypted_Message

encryptMessage(b"Hey santosh here.")
def decryptMessage(message_secret):
    key = getMyKey()
    k = Fernet(key)
    decrypted_Message = k.decrypt(message_secret)
    return decrypted_Message

decryptMessage(b"")