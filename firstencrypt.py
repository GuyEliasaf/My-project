import random,os
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

def encrypt(filename ,key):
    chunksize=64*1024
    outputfile="(encrypted)" + filename
    filesize= str(os.path.getsize(filename)).zfill(16)
    IV= ''

    for i in range(16):
        IV += chr(random.randint(0,0xFF))

    encryptor= AES.new(key,AES.MODE_CBC,IV)

    with open(filename, 'rb') as infile:
        with open(outputfile,'wb') as outfile:
            outfile.write(filesize)
            outfile.write(IV)

            while True:
                chunk=infile.read(chunksize)

                if len(chunk)==0:
                    break

                elif len(chunk)%16 !=0:
                    chunk +=' '*(16-len(chunk)%16)

                outfile.write(encryptor.encrypt(chunk))

def getkey(password):
    hasher= SHA256.new(password)
    return hasher.digest()


def main():
    filename = raw_input("file name:")
    password = raw_input("password:")
    encrypt(filename, getkey(password))
    print ("Done")


if __name__ == '__main__':
        main()





