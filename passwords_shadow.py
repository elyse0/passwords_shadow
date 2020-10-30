from crypt import crypt
from salt_hash import getSaltHash

def computeHash(password, salt):
    return crypt(password, salt)

def dictionaryAttack(linuxPassword, dictionaryFile="dictionary.txt"):

    salt, hash = getSaltHash(linuxPassword)
    dictionary = open(dictionaryFile, "r", encoding="utf_16")
    dictionaryContents = dictionary.read().split('\n')

    # Check for passwords in dictionary
    for password in dictionaryContents:
        if( salt + "$" + hash  == computeHash(password, salt)):
            print(linuxPassword + "  Cleartext: " + password)
            dictionary.close()
            return

    """
    # Check for passwords + number
    for password in contents:
        for i in range(100):
             if(linuxHash == getHash(password + str(i), salt)):
                print(linuxHash + " Cleartext: " + password)
                file.close()
                return
    """

    print("NOT FOUND!  " + linuxPassword)
    dictionary.close()

def main():

    file = open("shadow", "r")
    fileContents = file.read().split("\n")

    for line in fileContents:
        if(len(getSaltHash(line)) == 2):    # Valid Salt + Hash
            dictionaryAttack(line)

main()