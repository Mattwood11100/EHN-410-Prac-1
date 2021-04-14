    # Useful source
# https://crypto.interactive-maths.com/hill-cipher.html#2x2encypt

import numpy as np
import string
from PIL import Image

class Hill(object):
    def __init__(self):
        self.K_Matrix = None

    def set_K(self,K):
        self.K_Matrix = K

    def get_K(self):
        return self.K_Matrix

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

HillCipher = Hill()

# Generates array of possible inverse determinates, but returns smallest
def GetInverseDet26(det):
    if(det == 0):
        raise Exception("Inverse does not exist")
    temp = []
    for i in range(1000):
            # Using the congruency equation of (u)mod26=((a)^-1)mod26
                # gives (au)mod26=(1)mod26
                    # thus (au)mod26=1
                    # where u is the inverse determinate
        if((det*i)%26 == 1):
            temp.append(i)

    if ( len(temp) == 0):
        raise Exception("Inverse determinant does not exist")
    print("Inverse Mod of", det, "is:", temp[0])
    return temp[0]

def GetInverseDet256(det):
    if (det == 0):
        raise Exception("Inverse does not exist")
    temp = []
    for i in range(1000):
        if((det*i)%256 == 1):
            temp.append(i)
    if (len(temp) == 0):
        raise Exception("Inverse determinant does not exist")
    print("Inverse Mod of", det, "is:", temp[0])
    return temp[0]

def GetInverseMatrix26(m):
    det = int(np.round(np.linalg.det(m)))
    Det_I = GetInverseDet26(det)
        # Convert to adjoint matrix form then multiply (detK)^-1 to get modulo inverse of matrix
    if (len(m) == 2):
        T = GetCofactorMatrix2(m)
        Inverse = (np.round(T * Det_I)) % 26
        return Inverse
    elif (len(m) == 3):
        T = GetCofactorMatrix3(m)
        Inverse = (np.round(T * Det_I)) % 26
        return Inverse



def GetInverseMatrix256(m):
    det = int(np.round(np.linalg.det(m)))
    Det_I = GetInverseDet256(det)

    if (len(m) == 2):
        T = GetCofactorMatrix2(m)
        Inverse = (np.round(T * Det_I)) % 256
        return Inverse
    elif (len(m) == 3):
        T = GetCofactorMatrix3(m)
        Inverse = (np.round(T * Det_I)) % 256
        return Inverse
    # return Inverse

def GetCofactorMatrix2(M):
    Temp = np.zeros((2,2))
    Temp[0,0], Temp[1,1] = M[1,1], M[0,0]
    Temp[0,1], Temp[1,0] = M[0,1]*-1, M[1,0]*-1
    # print(Temp)
    return Temp

def GetCofactorMatrix3(M):
    Temp = np.zeros((3,3))
    a = M[0,0]
    b = M[0,1]
    c = M[0,2]
    d = M[1, 0]
    e = M[1, 1]
    f = M[1, 2]
    g = M[2, 0]
    h = M[2, 1]
    i = M[2, 2]

    Temp[0, 0] = e*i-f*h
    Temp[0, 1] = -(d*i-g*f)
    Temp[0, 2] = d*h-g*e
    Temp[1, 0] = -(b*i-h*c)
    Temp[1, 1] = a*i-g*c
    Temp[1, 2] = -(a*h-g*b)
    Temp[2, 0] = b*f-e*c
    Temp[2, 1] = -(a*f-d*c)
    Temp[2, 2] = a*e-d*b

    return Temp.T


def Hill_Encrypt(key,plaintext): # (key : String, plaintext : String or Int ndarray):

    Key = []

    key = key.lower()
    # Extract lowercase letters from the plaintext input
    key = ''.join(e for e in key if e.islower())

    Range = 0
        # Convert key to matrix
                # Can recode this to be dynamic -- Range = len(key) and resize(sqrt(range),sqrt(range))
                            # check if acceptable if sqrt(Range) is int
    if (len(key)==4):
        Range = 4
        for i in range(Range):
            Key.append(Hill_Dict_ToNum[key[i]])
        Key = np.asarray(Key)
        Key.resize((2,2))
        Key = np.asmatrix(Key)
        print("Key Matrix is:")
        print(Key)
        print("Key length is 4")
    elif (len(key)==9):

        Range = 9
        for i in range(Range):
            Key.append(Hill_Dict_ToNum[key[i]])
        Key = np.asarray(Key)
        Key.resize((3,3))
        # Key = np.asmatrix(Key)
        # print("Key Matrix is:")
        # print(Key)

        # print("Key length is 9")

    else:

        # print("Key length is not supported")
        raise Exception("Key length of {} is not supported".format(len(key)))

        # Set Key for recall from function
    HillCipher.set_K(Key)

    K_I = GetInverseMatrix26(Key)

    if( isinstance(plaintext,str) == True):

        print("plaintext is string")
            # Convert plaintext's letters to lowercase
        Text = plaintext.lower()
            # Extract lowercase letters from the plaintext input
        Text = ''.join(e for e in Text if e.islower())

            # Convert plaintext to numbers
        P_Temp = []
        for i in range(len(Text)):
            P_Temp.append(Hill_Dict_ToNum[Text[i]])

        OriginalLength = len(P_Temp)

            # Appends random letters to end of cyphertext to fill up groupings
                    # Appends random letters to prevent detection of appended letters
        Append = int(np.sqrt(Range))-len(P_Temp)%int(np.sqrt(Range))
        if (np.sqrt(Range)-Append!=0):
            print("Added",Append,"Letters at end of text")
            for i in range(Append):
                P_Temp.append(0)
                        # Cannot remove appended number of letters at the end after encryption without
                            # compromising the validity of the data that can be decrypted.
                            # This is because the data is encrypted in groups, and is thus difficult to
                            # decrypt the correct data without knowing what letter was added or which
                            # letter after encryption was removed.  This means that removing the
                            # appended number of letters after encryption can compromise up to sqrt(Range)
                            # number of original letters.  thus with and increase in the size of the
                            # key, more undecryptable data will be returned by the Hill Encrypt algorithm.
                            # This holds true for images aswell, but due to each pixel of an image having 3 values
                            # from 0 upto 255, it is rearly detectable with a persons eyes.  This problem will only
                            # be seen in the last sqrt(Range) values of the decrypted ciphertext/nd-array.
                            # For images it is difficult if you do not remove the appended values, due to
                            # very few values being added it is not possible to change the size of the nd-array to
                            # accomodate a way to recover the original size when decrypting, and thus makes the
                            # Hill Cipher a non loss-less encryption algorithm, however is neglectable in large images
                            # if the application does not require 100% loss-less encryption-decryption

            # Set P matrix for matrix multiplication
        P = np.asarray(P_Temp)
        # P = np.asmatrix(P_Temp)
        Length = len(P)
        # print("Length:",len(P))
        # print(P)

            # Resize P for easy matrix multiplication
                # Also cuts of data that wont fit in the range of sqrt(Range)
                            # Verify if you should append data rather than cutting data of
        P.resize((int(len(P)/np.sqrt(Range)),int(np.sqrt(Range))))
        # print(P)

        Output = []
        for i in range(len(P)):
            C = np.matmul(P[i],Key) %26
            Output.append(C)
        # for i in range()
        Output = np.asarray(Output)
        Output.resize((1,Length))
        # print(Output)

        Output_Str = ""
        for i in range(Length):
            Output_Str += Hill_Dict_ToLet[Output[0][i]]

        # print(Output_Str)
        # print("plaintext is string")
        return Output_Str

    # ===========================================================================
        # else plaintext is nd-array
    else:
        print("plaintext is nd-array")
        try:
            ndArray_Size = plaintext[0][0].size
        except:
            raise Exception("nd-array format not supported")

        if (ndArray_Size == 3):     # Alpha not included
            array = plaintext

        elif (ndArray_Size == 4):   # Alpha included
                # Exclude Alpha values.
            array = np.zeros((len(plaintext),len(plaintext[0]),3))
            for i in range(len(plaintext)):
                for j in range(len(plaintext[0])):
                    array[i][j] = plaintext[i][j][0:3]


        else:   # Not RGB image
            raise Exception("nd-array is not an RGB image array")

        # Resize to 2d array of size (n x sqrt(Range))
            # Used to return array to correct shape
        y_axis = len(array)
        x_axis = len(array[0])



        P = array
        # print(P)
        size = int(y_axis*x_axis*3)
        P.resize((1,size))

        Append = int(np.sqrt(Range)) - len(P) % int(np.sqrt(Range))
        if (np.sqrt(Range) - Append != 0):
            print("Added", Append, "0 at the end of array")
            for i in range(Append):
                P = np.append(P,0)
                # Not needed to remove these appended values due to the resize, resizing it to
                    # the original size and cuts of these values

        P.resize((int(len(P)/np.sqrt(Range)),int(np.sqrt(Range))))

        Length = len(P)
        # print("Length:",Length)
        Output = []
        for i in range(Length):
            C = np.matmul(P[i], Key) % 256
            Output.append(C)
        # for i in range()
        Output = np.asarray(Output)
        Output.resize((1, Length*int(np.sqrt(Range))))

        Output.resize((y_axis,x_axis,3))
        # print("Shape:", Output.shape)
        # print("{}x{}".format(y_axis,x_axis))
        # print(Output)
        # print("plaintext is nd-array")
        return Output


# -----------------------------------------------------------------------------------------------------


def Hill_Decrypt(key,ciphertext): # (key : String, ciphertext : String or Int ndarray )
    Key = []

    key = key.lower()
    # Extract lowercase letters from the plaintext input
    key = ''.join(e for e in key if e.islower())

    Range = 0
    # Convert key to matrix
            # Can recode this to be dynamic -- Range = len(key) and resize(sqrt(range),sqrt(range))
                    # check if acceptable if sqrt(Range) is int
    if (len(key) == 4):
        Range = 4
        for i in range(Range):
            Key.append(Hill_Dict_ToNum[key[i]])
        Key = np.asarray(Key)
        Key.resize((2, 2))
        Key = np.asmatrix(Key)
        # print("Key Matrix is:")
        # print(Key)
        print("Key length is 4")
    elif (len(key) == 9):

        Range = 9
        for i in range(Range):
            Key.append(Hill_Dict_ToNum[key[i]])
        Key = np.asarray(Key)
        Key.resize((3, 3))
        # Key = np.asmatrix(Key)
        # print("Key Matrix is:")
        # print(Key)

        print("Key length is 9")

    else:

        print("Key length is not supported")

    if (isinstance(ciphertext, str) == True):

        Key = np.asmatrix(Key)

            # Get Inverse key matrix
                # Check Inverse method for K  or A here
        K_I = GetInverseMatrix26(Key)
        # print("K.I:",K_I)

        # Convert ciphertext's letters to lowercase
        Text = ciphertext.lower()
        # Extract lowercase letters from the ciphertext input
        Text = ''.join(e for e in Text if e.islower())
        # Convert ciphertext to numbers
        P_Temp = []
        for i in range(len(Text)):
            P_Temp.append(Hill_Dict_ToNum[Text[i]])

        OriginalLength = len(P_Temp)

            # Appends random letters to end of cyphertext to fill up groupings
                    # Appends random letters to prevent detection of appended letters
        Append = int(np.sqrt(Range)) - len(P_Temp) % int(np.sqrt(Range))
        if (np.sqrt(Range) - Append != 0):
            print("Added", Append, "Letter/s at the end of text")
            for i in range(Append):
                P_Temp.append(0)

            # Set P matrix for matrix multiplication
        P = np.asarray(P_Temp)
        # P = np.asmatrix(P_Temp)
        Length = len(P)
        # print("Length:",len(P))
        # print(P)

        # Resize P for easy matrix multiplication
            # Also cuts of data that wont fit in the range of sqrt(Range)
                # Verify if you should append data rather than cutting data of
        P.resize((int(len(P) / np.sqrt(Range)), int(np.sqrt(Range))))

        Output = []
        for i in range(len(P)):
            C = np.matmul(P[i], K_I) % 26
            Output.append(C)
        # for i in range()
        Output = np.asarray(Output)
        # print("Output:",Output)
        Output.resize((1, Length))
        # print(Output)

        Output_Str = ""
        for i in range(Length):
            Output_Str += Hill_Dict_ToLet[Output[0][i]]

        # print(Output_Str)
        # print("plaintext is string")
        return Output_Str

        # ========================================================================

        # Ciphertext is nd-array
    else:

        Key = np.asmatrix(Key)

            # Get Inverse key matrix
        K_I = GetInverseMatrix256(Key)

        try:
            ndArray_Size = ciphertext[0][0].size
            print("Ciphertext is nd-array")
        except:
            raise Exception("nd-array format not supported")

        if (ndArray_Size == 3):     # Alpha not included
            array = ciphertext

        elif (ndArray_Size == 4):   # Alpha included
                # Exclude Alpha values.
            array = np.zeros((len(ciphertext),len(ciphertext[0]),3))
            for i in range(len(ciphertext)):
                for j in range(len(ciphertext[0])):
                    array[i][j] = ciphertext[i][j][0:3]


        else:   # Not RGB image
            raise Exception("nd-array is not an RGB image array")

        # Resize to 2d array of size (n x sqrt(Range))
            # Used to return array to correct shape
        y_axis = len(array)
        x_axis = len(array[0])

        P = array
        size = int(y_axis*x_axis*3)
        P.resize((1,size))

        Append = int(np.sqrt(Range)) - len(P) % int(np.sqrt(Range))
        if (np.sqrt(Range) - Append != 0):
            print("Added", Append, "0 at the end of array")
            for i in range(Append):
                P = np.append(P,0)
                # Not needed to remove these appended values due to the resize, resizing it to
                    # the original size and cuts of these values

        P.resize((int(len(P)/np.sqrt(Range)),int(np.sqrt(Range))))

        Length = len(P)
        # print("Length:", Length)
        Output = []
        for i in range(Length):
            C = np.matmul(P[i], K_I) % 256
            Output.append(C)
        # for i in range()
        Output = np.asarray(Output)
        Output.resize((1, Length*int(np.sqrt(Range))))
        # print("O", Length)

        Output.resize((y_axis, x_axis, 3))
        # print("Shape:", Output.shape)
        # print("{}x{}".format(y_axis, x_axis))
        # print(Output)
        # print("plaintext is nd-array")
        return Output


    print("Decrypting")

def Get_Hill_Encryption_Matrix():

    # print("Return Matrix")
    return HillCipher.get_K()


def TestHill(MyImage):
    ########### Call Functions ###########
    print("=======Text Encryption=======")
    Original = "Paymoremoney"
    # Original = "wearediscoveredsaveyourself"
    # Original = "This Is my Original Random Texts!."
    Original = "This is my Secret!."
    Original = "Do not tell anyone else"
    # Key_G = "rrfvsvcct"
    Key_G = "fird"
    # Key_G = "pdkhfbvsd"


    print("Original Text:",Original)
    print("Key is:",Key_G)
    Encrypted = Hill_Encrypt(Key_G,Original)
    print("Encrypted Text:",Encrypted)
    Decrypted = Hill_Decrypt(Key_G,Encrypted)
    print("Decrypted Text:",Decrypted)
    k = Get_Hill_Encryption_Matrix()
    print("Encryption Matrix:",k)

    print("=============================")

    print("=======Image Encryption=======")

    InputImage = np.asarray(Image.open(MyImage))
    Encrypted_Image = Hill_Encrypt(Key_G,InputImage)

    im = Image.fromarray(np.uint8(Encrypted_Image))
    im.save("Encrypted.png")

    Decrypted_Image = Hill_Decrypt(Key_G,Encrypted_Image)

    im = Image.fromarray(np.uint8(Decrypted_Image))
    im.save("Decrypted.png")

    k = Get_Hill_Encryption_Matrix()
    print("Encryption Matrix:", k)
    print("==============================")

TestHill('earth.png')