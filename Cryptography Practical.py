import numpy as np


# Method used to encrypt a plain text message given a specific key.
# The stage will determine the number of time the transposition cipher
# needs to be completed on the plain text
def Transpose_Encrypt(key, stage, plaintext):
    # Removing non alphabetic characters
    # ===================================================
    # Removes special characters and converts the plaintext to upper case
    plaintext = ''.join(char for char in plaintext.upper() if 'A' <= char <= 'Z')
    # Print statement used for testing purposes
    # print("Plaintext, without special characters:\n", plaintext, end="\n")
    # ===================================================

    # Getting the lengths of the key and message
    # ===================================================
    # The length of the key is needed to determine how many
    # columns there needs to be
    kLen = len(key)
    # Print statement used for testing purposes
    # print("Key length:\n", kLen, end="\n")

    # The length of the plain text is need to determine if
    # padding needs to occur or not. This will also determine
    # the number of rows in the array
    sLen = len(plaintext)
    # Print statement used for testing purposes
    # print("Plaintext length:\n", sLen, end="\n")
    # ===================================================

    # Calculating and adding, if necessary, the padding
    # ===================================================
    # Number of characters that that will be appended to the plaintext
    padLen = 0

    # If the length of the plaintext modded with the key length is greater
    # than 0 then padding needs to occur
    if (sLen % kLen > 0):
        padLen = kLen - (sLen % kLen)
    # Print statement used for testing purposes
    # print("Padding length:\n", padLen, end="\n")
    # Checks if the pad amount is 0 or not, if it is not 0 then padding
    # will be added
    if (padLen > 0):
        # Adding the padding, the letter 'X' is used to pad the text
        plaintext = plaintext.ljust(sLen + padLen, 'X')

        # Getting the new length of the plaintext since padding was added
        sLen = len(plaintext)
        # Print statement used for testing purposes
        # print("New Plaintext length:\n", sLen, end="\n")
    # ===================================================

    # Getting the order in which the columns will be read
    # ===================================================
    # Splitting the key string into a list
    kList = [char for char in key.upper()]
    # Print statement used for testing purposes
    # print("Key in list format:\n", kList, end="\n")
    # Creating a copy of the key string in list from so it can be
    # sorted alphabetically
    kListSorted = [char for char in key.upper()]
    kListSorted.sort()
    # Print statement used for testing purposes
    # print("Sorted Key list:\n", kListSorted, end="\n")
    # Creating a column index list
    kIndex = []
    for i in range(kLen):
        kIndex.append(kList.index(kListSorted[i]))
    # Print statement used for testing purposes
    # print("Key index:\n", kIndex, end="\n")
    # ===================================================

    # For loop to do the encryption multiple times if the stage is
    # greater than 1
    # ===================================================
    for sNum in range(stage):
        # Print statement used for testing purposes
        # print("Stage ", sNum + 1, ":\n===================================================\n")
        # Variable for storing the encrypted text if stage is
        # greater than 1
        if (sNum < 1):
            sText = plaintext

        # Creating and populating the transposition matrix
        # ===================================================
        # Creating variables for the column and row size, respectively
        nCol = kLen
        nRow = sLen // kLen
        # Print statement used for testing purposes
        # print("Column and Row lengths:\n", nCol, "\t", nRow, end="\n")
        # Creating the transposition matrix with shape (nRow, nCol)
        trans = np.full((nRow, nCol), '')

        # Populating the transposition matrix with the plaintext message
        tCounter = 0
        for i in range(nRow):
            for j in range(nCol):
                trans[i][j] = sText[tCounter]
                tCounter += 1
        # Print statement used for testing purposes
        # print("Transposition Matrix:\n", trans, end="\n")
        # ===================================================

        # Encrypting the plaintext string
        # ===================================================
        # Looping through the transposition matrix and reading the columns
        # in order determined by the alphabetical order of the text
        encryptText = ""
        for i in range(nCol):
            for j in range(nRow):
                encryptText += trans[j][kIndex[i]]
        # Print statement used for testing purposes
        # print("Encrypted text:\n", encryptText, end="\n\n")
        # ===================================================

        if (stage > 1):
            sText = encryptText
    # ===================================================

    # Returning the encrypted string
    return encryptText


# Method used to decrypt a cipher text message given a specific key.
# The stage will determine the number of time the transposition cipher
# needs to be completed on the cipher text
def Transpose_Decrypt(key, stage, ciphertext):
    # Getting the lengths of the key and message
    # ===================================================
    # The length of the key is needed to determine how many
    # columns there needs to be
    kLen = len(key)
    # Print statement used for testing purposes
    # print("Key length:\n", kLen, end="\n")

    # The length of the cipher text will determine
    # the number of rows in the array
    sLen = len(ciphertext)
    # Print statement used for testing purposes
    # print("Plaintext length:\n", sLen, end="\n")
    # ===================================================

    # Getting the order in which the columns will be read
    # ===================================================
    # Splitting the key string into a list
    kList = [char for char in key.upper()]
    # Print statement used for testing purposes
    # print("Key in list format:\n", kList, end="\n")
    # Creating a copy of the key string in list from so it can be
    # sorted alphabetically
    kListSorted = [char for char in key.upper()]
    kListSorted.sort()
    # Print statement used for testing purposes
    # print("Sorted Key list:\n", kListSorted, end="\n")
    # Creating a column index list
    kIndex = []
    for i in range(kLen):
        kIndex.append(kList.index(kListSorted[i]))
    # Print statement used for testing purposes
    # print("Key index:\n", kIndex, end="\n")
    # ===================================================

    # For loop to do the decryption multiple times if the stage is
    # greater than 1
    # ===================================================
    for sNum in range(stage):
        # Print statement used for testing purposes
        # print("Stage ", sNum + 1, ":\n===================================================\n")
        # Variable for storing the decrypted text if stage is
        # greater than 1
        if (sNum < 1):
            sText = ciphertext

        # Creating and populating the transposition matrix
        # ===================================================
        # Creating variables for the column and row size, respectively
        nCol = kLen
        nRow = sLen // kLen
        # Print statement used for testing purposes
        # print("Column and Row lengths:\n", nCol, "\t", nRow, end="\n")
        # Creating the transposition matrix with shape (nRow, nCol)
        trans = np.full((nRow, nCol), '')

        # Looping through the transposition matrix and reading the columns
        # in order determined by the alphabetical order of the key
        tCounter = 0
        for i in range(nCol):
            for j in range(nRow):
                trans[j][kIndex[i]] = sText[tCounter]
                tCounter += 1
        # Print statement used for testing purposes
        # print("Transposition Matrix:\n", trans, end="\n")
        # ===================================================

        # Decrypting the ciphertext string
        # ===================================================
        # Looping through the transposition matrix and reading the rows
        decryptText = ""
        for i in range(nRow):
            for j in range(nCol):
                decryptText += trans[i][j]
        # Print statement used for testing purposes
        # print("Decrypted text:\n", decryptText, end="\n\n")
        # ===================================================

        if (stage > 1):
            sText = decryptText
    # ===================================================

    # Returning the decrypted string
    return decryptText


def Testing_Transposition_Cipher():
    # Encryption
    # ===================================================
    # keys = "Mat"
    # stages = 1
    # text = "Hey look! There is a dog!"
    # encrypt = "EOTRSOHLKEIDYOHEAG"
    # onlineText = "EOTRSOHLKEIDYOHEAG"
    # eText = Transpose_Encrypt(keys, stages, text)
    # print(encrypt == eText)
    # print(onlineText == eText, end="\n\n")

    # colText = Transposition_Encryption_Column(keys, stages, text)
    # rowText = Transposition_Encryption_Row(keys, stages, text)
    # print(colText)
    # print(rowText)
    # print(colText == rowText)

    #
    # keys = "Mat"
    # stages = 2
    # text = "Hey look! There is a dog!"
    # encrypt = "OSLIOAERHEYETOKDHG"
    # onlineText = "OSLIOAERHEYETOKDHG"
    # eText = Transpose_Encrypt(keys, stages, text)
    # print(encrypt == eText)
    # print(onlineText == eText, end="\n\n")
    #
    # keys = "Mat"
    # stages = 3
    # text = "Hey look! There is a dog!"
    # encrypt = "SORYOHOIEETDLAHEKG"
    # onlineText = "SORYOHOIEETDLAHEKG"
    # eText = Transpose_Encrypt(keys, stages, text)
    # print(encrypt == eText)
    # print(onlineText == eText, end="\n\n")
    # ===================================================

    # Decryption
    # ===================================================
    # keys = "Mat"
    # stages = 1
    # text = "EOTRSOHLKEIDYOHEAG"
    # decrypt = "HEYLOOKTHEREISADOG"
    # onlineText = "HEYLOOKTHEREISADOG"
    # dText = Transpose_Decrypt(keys, stages, text)
    # print(decrypt == dText)
    # print(onlineText == dText, end="\n\n")

    # colText = Transposition_Decryption_Column(keys, stages, text)
    # rowText = Transposition_Decryption_Row(keys, stages, text)
    # print(colText)
    # print(rowText)
    # print(colText == rowText)

    #
    # keys = "Mat"
    # stages = 2
    # text = "OSLIOAERHEYETOKDHG"
    # decrypt = "HEYLOOKTHEREISADOG"
    # onlineText = "HEYLOOKTHEREISADOG"
    # dText = Transpose_Decrypt(keys, stages, text)
    # print(decrypt == dText)
    # print(onlineText == dText, end="\n\n")
    #
    # keys = "Mat"
    # stages = 3
    # text = "SORYOHOIEETDLAHEKG"
    # decrypt = "HEYLOOKTHEREISADOG"
    # onlineText = "HEYLOOKTHEREISADOG"
    # dText = Transpose_Decrypt(keys, stages, text)
    # print(decrypt == dText)
    # print(onlineText == dText, end="\n\n")
    # ===================================================

    keys = "Jawbox"
    stages = 6
    text = "Look at that my cypher is working correctly"
    eText = Transpose_Encrypt(keys, stages, text)
    online = "OGCINREPHCYRRWOISKAOKLOTMATTHYLCTREY"

    dText = Transpose_Decrypt(keys, stages, eText)
    online2 = "LOOKATTHATMYCYPHERISWORKINGCORRECTLY"

    if (eText == online):
        print("Encryption Successful!!\n", eText, "\n", online, "\n\n")
    else:
        print("Encryption Unsuccessful!!\n")

    if (dText == online2):
        print("Decryption Successful!!\n", dText, "\n", online2, "\n\n")
    else:
        print("Decryption Unsuccessful!!\n")


Testing_Transposition_Cipher()
