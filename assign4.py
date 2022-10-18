# imports
from Crypto.Hash import SHA256
import string
import random
import time
from bcrypt import *
import nltk
nltk.download('words')
from nltk.corpus import words

# global variables
COUNTER = 0

# SHA256 function
def hashSha256(string1):

    global COUNTER
    COUNTER = COUNTER + 1

    # create SHA256 hashing function
    h = SHA256.new()

    # encode string 1
    s1Encode = string1.encode()
    
    # hash the inputs
    h.update(s1Encode)

    print("String", COUNTER ,"hashed by SHA256: " , h.hexdigest())

def modifiedSha(string1, numOfBits):

     # create SHA256 hashing function
    h = SHA256.new()

    # encode string 1
    s1Encode = string1.encode()

    # hash the inputs
    h.update(s1Encode)

    # convert the hash output to a byte array
    stringArray = bytearray(h.hexdigest(), 'utf-8')

    #print(stringArray)

    #print(str(stringArray, 'utf-8')) 

    # convert the byte array to a string
    newStringArray = str(stringArray, 'utf-8')

    # create a bit array 
    bitArray = ' '.join(format(ord(x), 'b') for x in newStringArray)

    # remove bit array white space
    bitArray = bitArray.replace(" ", "")

    #print(bitArray)
    #print("")

    # truncate hash output to 8 bits
    #truncatedOutput = stringArray[:3]
    truncatedOutput = bytearray(bitArray[:numOfBits], 'utf-8')

    # convert truncated output to a string
    newTrunc = str(truncatedOutput, 'utf-8')

    # print the truncated output
    #print("String hashed by modified SHA256 (in bits): " , newTrunc)

    return newTrunc

def targetHashCollision(gString, nBits):

    # set notfound value to true
    notfound = 1

    # number of bits to select
    NumberOfBits = nBits

    # hash target value
    hashTarget = modifiedSha(gString, NumberOfBits)

    # initializing size of string
    N = 3

    # number of inputs
    numberOfInputs = 0

    STARTTIME = time.time()

    while(notfound):

        # using random.choices()
        # generating random strings
        res = ''.join(random.choices(string.ascii_letters, k=N))
        
        # create new hash of resulting random string
        newHash = modifiedSha(res, NumberOfBits)

        # increment number of inputs
        numberOfInputs = numberOfInputs + 1

        # hash collision found
        if(hashTarget == newHash):
            
            # print statements for hash collision
            print("Given string: Dog")
            print("Hash value of string Dog: ", hashTarget)
            print("String that hashed to same hash value: ", res)
            print("Hash value of string ", res, ": ", newHash)
            print("Number of inputs needed to find the collision: ", numberOfInputs)

            # get the time collision was found
            ENDTIME = time.time()

            # print the execution time of finding the collision
            print("Elapsed time to find collision for", NumberOfBits,"bits: ", ENDTIME - STARTTIME)

            print("")

            # update foundvalue to false
            notfound = 0

def breakingHash():
    print("")
    print("Break Real Hash function started.")

    # users full hash in bytes
    Bilbi = b"$2b$08$J9FW66ZdPI2nrIMcOxFYI.qx268uZn.ajhymLP/YHaAsfBGP3Fnmq"
    Gandalf = b"$2b$08$J9FW66ZdPI2nrIMcOxFYI.q2PW6mqALUl2/uFvV9OFNPmHGNPa6YC" 
    Thorin = b"$2b$08$J9FW66ZdPI2nrIMcOxFYI.6B7jUcPdnqJz4tIUwKBu8lNMs5NdT9q" 
    Fili = b"$2b$09$M9xNRFBDn0pUkPKIVCSBzuwNDDNTMWlvn7lezPr8IwVUsJbys3YZm"
    Kili = b"$2b$09$M9xNRFBDn0pUkPKIVCSBzuPD2bsU1q8yZPlgSdQXIBILSMCbdE4Im" 
    Balin = b"$2b$10$xGKjb94iwmlth954hEaw3O3YmtDO/mEFLIO0a0xLK1vL79LA73Gom" 
    Dwalin = b"$2b$10$xGKjb94iwmlth954hEaw3OFxNMF64erUqDNj6TMMKVDcsETsKK5be"
    Oin = b"$2b$10$xGKjb94iwmlth954hEaw3OcXR2H2PRHCgo98mjS11UIrVZLKxyABK" 
    Gloin = b"$2b$11$/8UByex2ktrWATZOBLZ0DuAXTQl4mWX1hfSjliCvFfGH7w1tX5/3q" 
    Dori = b"$2b$11$/8UByex2ktrWATZOBLZ0Dub5AmZeqtn7kv/3NCWBrDaRCFahGYyiq" 
    Nori = b"$2b$11$/8UByex2ktrWATZOBLZ0DuER3Ee1GdP6f30TVIXoEhvhQDwghaU12" 
    Ori = b"$2b$12$rMeWZtAVcGHLEiDNeKCz8OiERmh0dh8AiNcf7ON3O3P0GWTABKh0O" 
    Bifur = b"$2b$12$rMeWZtAVcGHLEiDNeKCz8OMoFL0k33O8Lcq33f6AznAZ/cL1LAOyK" 
    Bofur = b"$2b$12$rMeWZtAVcGHLEiDNeKCz8Ose2KNe821.l2h5eLffzWoP01DlQb72O" 
    Durin = b"$2b$13$6ypcazOOkUT/a7EwMuIjH.qbdqmHPDAC9B5c37RT9gEw18BX6FOay"

    # users name list
    userNames = ["Bilbi", "Gandalf", "Thorin", "Fili", "Kili", "Balin",
    "Dwalin", "Oin", "Gloin", "Dori", "Nori", "Ori", "Bifur", "Bofur",
     "Durin"]
    
    # user hash list
    userHashes = [Bilbi, Gandalf, Thorin, Fili, Kili, Balin,
     Dwalin, Oin, Gloin, Dori, Nori, Ori, Bifur, Bofur, 
     Durin]

    # create dictionary of user names and hashes
    dictionary = dict(zip(userNames, userHashes))

    # list of words in the nltk corpus
    #print(type(words.words()))

    # # iterate through dictionary
    # for uName, uHash in dictionary.items():

    #     # iterate through nltk corpus
    #     for w in words.words():

    #         # encode word
    #         newWord = w.encode('utf-8')

    #         # check if word is the password
    #         if( checkpw(newWord, uHash) ):

    #             # found the password
    #             print("Password for", uName, "was found.")
    #             print("Password: ", w)
    #             break

    # ------------------
    # - search for last six passwords

     # users name list
    newUserNames = ["Dori", "Nori", "Ori", "Bifur", "Bofur", "Durin"]
    
    # user hash list
    newUserHashes = [Dori, Nori, Ori, Bifur, Bofur, Durin]

    # count passwords found
    foundCount = 0

    # assign nltk corpus to new list
    wordsList = words.words()

    #print(len(wordsList))

    # filter words list 
    wordsList = list(filter(lambda x: len(x) >= 6, wordsList))
    wordsList = list(filter(lambda x: len(x) <= 10, wordsList))

    #print(len(wordsList))

    # iterate through nltk corpus
    for word in reversed(wordsList):

        # encode word
        newWord = word.encode('utf-8')

        # check if word is the password
        if( checkpw(newWord, newUserHashes[0]) ):

            # found the password
            print("Password for", newUserNames[0], "was found.")
            print("Password:", word)
            foundCount = foundCount + 1

        # check if word is the password
        if( checkpw(newWord, newUserHashes[1]) ):

            # found the password
            print("Password for", newUserNames[1], "was found.")
            print("Password:", word)
            foundCount = foundCount + 1

        # check if word is the password
        if( checkpw(newWord, newUserHashes[2]) ):

            # found the password
            print("Password for", newUserNames[2], "was found.")
            print("Password:", word)
            foundCount = foundCount + 1

        # check if word is the password
        if( checkpw(newWord, newUserHashes[3]) ):

            # found the password
            print("Password for", newUserNames[3], "was found.")
            print("Password:", word)
            foundCount = foundCount + 1

        # check if word is the password
        if( checkpw(newWord, newUserHashes[4]) ):

            # found the password
            print("Password for", newUserNames[4], "was found.")
            print("Password:", word)
            foundCount = foundCount + 1

        # check if word is the password
        if( checkpw(newWord, newUserHashes[5]) ):

            # found the password
            print("Password for", newUserNames[5], "was found.")
            print("Password:", word)
            foundCount = foundCount + 1

        # break out once 6 passwords were found
        if(foundCount == 6):
            break

    print("Break Real Hash function ended.")
            

# main function
def main():

    # -Task 1-

    # part a
    string1 = "hey look"
    string2 = "what is this"

    #hashSha256(string1)
    #hashSha256(string2)

    #print("")
    
    # part b

    # strings to test for hamming distance
    hamString1 = "Hello"
    hamString2 = "hello"
    hamString3 = "Jeremiah"
    hamString4 = "jeremiah"
    hamString5 = "Football"
    hamString6 = "football"

    # testing strings
    hashSha256(hamString1)
    hashSha256(hamString2)
    hashSha256(hamString3)
    hashSha256(hamString4)
    hashSha256(hamString5)
    hashSha256(hamString6)

    # part c

    # - test modified SHA256 function
    mString1 = "Hello"
    mString2 = "hello"

    # modifiedSha(mString1)
    # modifiedSha(mString2)

    # - find a target hash collision
    givenString = "Dog"

    # counter
    mcounter = 8

    # while loop to find number of collision for multiple of 2 bits
    # while(mcounter < 52):

    #     # call collision function
    #     targetHashCollision(givenString, mcounter)
    #     mcounter = mcounter + 2

    # Task 2
    # - breaking real hashes
    #breakingHash()




main()