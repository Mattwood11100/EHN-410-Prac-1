import numpy as np
# import pillow as pl
import string as st


# Method used to encrypt a plain text message given a specific key.
# The stage will determine the number of time the transposition cipher
# needs to be completed on the plain text
def Transpose_Encrypt(key, stage, plaintext):
    # The length of the key, this is needed to determine how many
    # columns there needs to be
    kLen = len(key)

    # The length of the plain text, this is need to determine if
    # padding needs to occur or not. This will also determine
    # the number of rows in the array
    sLen = len(plaintext)

    trans = np.array([kLen, sLen//kLen])

    print(trans)


def Transpose_Decrypt(key, stage, ciphertext):
    pass


Transpose_Encrypt("maine", 1, "at four surveillance on enemy camp")
