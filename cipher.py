'''
Created on Aug 25, 2020

@author: Jonathon Schnell

@date: 8/25/2020

@version: 1.0.1

'''
import argparse
from _cffi_backend import string
from lib2to3.fixer_util import String

if __name__ == "__main__":
    #argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument("string", help="[string] to be ciphered or un-ciphered MUST CONTAIN ONLY LETTERS a-z in LOWERCASE, NO SPACES!")
    parser.add_argument("-e", "--encrypt", nargs='?', default='false', help="encrypt string")
    parser.add_argument("-d", "--decrypt", nargs='?', default='false', help="decrypt string")
    
    args = parser.parse_args()
    string = args.string
    
    #define character space
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    #shift right by length of string
    def encrypt(string):
        #output string
        string1 = ""
        for char in string:
            num = int(alphabet.index(char) + len(string))
            #reset to 0 if numbers exceed 25
            while num > 25:
                num -= 26
            string1 = string1 + alphabet[num]
        return string1
    
    #shift left by length of string 
    def decrypt(string):
        string1 = ""
        for char in string:
            num = int(alphabet.index(char) - len(string))
            #if number goes below 0 reset to 25
            while num < 0:
                num += 26
            string1 = string1 + alphabet[num]
        return string1
        
    #argument handling 
    if args.encrypt == "false":
        print(decrypt(string))
        
    elif args.decrypt == "false":
        print(encrypt(string))


    
        
    
