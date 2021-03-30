import numpy as np
import string
# import pillow

    # Convert lowercase letters to numbers, call Hill_Dict_ToNum[x]
Hill_Dict_ToNum = {'a':0,'b':1,'c':2,'d':3,
                   'e':4,'f':5,'g':6,'h':7,
                   'i':8,'j':9,'k':10,'l':11,
                   'm':12,'n':13,'o':14,'p':15,
                   'q':16,'r':17,'s':18,'t':19,
                   'u':20,'v':21,'w':22,'x':23,
                   'y':24,'z':25}

    # Convert numbers to lowercase letters, call Hill_Dict_ToLet['a']
Hill_Dict_ToLet = {0:'a',1:'b',2:'c',3:'d',
                   4:'e',5:'f',6:'g',7:'h',
                   8:'i',9:'j',10:'k',11:'l',
                   12:'m',13:'n',14:'o',15:'p',
                   16:'q',17:'r',18:'s',19:'t',
                   20:'u',21:'v',22:'w',23:'x',
                   24:'y',25:'z'}

def Hill_Encrypt(key,plaintext): #(key : String, plaintext : String or Int ndarray):
    if( isinstance(plaintext,str) == True):


        print("plaintext is string")

    else:

        print("plaintext is Int ndarray")


def Hill_Decrypt(key,ciphertext): # (key : String, ciphertext : String)


    print("Decrypting")

def Get_Hill_Encryption_Matrix():

    print("Return Matrix")
