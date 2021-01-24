import binascii
from itertools import cycle
import re
import sys
import ast


## Read Wordlist

wordlist = []

with open('wordlist.txt',"r") as f:
    for line in f:
        wordlist.extend(line.split())
wordlist = [element.lower() for element in wordlist]

## Read File and extract strings 

file_name = sys.argv[1]
fp = open(file_name)
contents = fp.read()

def extract_keys():
   
    match = re.compile(r'\n....\n')


    keys = re.findall(match, contents)
    keys = list(dict.fromkeys(keys))
    keys = [x[1:-1] for x in keys]

    return(keys)

keys = extract_keys()


def extract_strings():
   
    match = re.compile(r'\n.{8,15}\n')


    strings = re.findall(match, contents)
    strings = list(dict.fromkeys(strings))
    strings = [x[1:-1] for x in strings]

    return(strings)

strings = extract_strings()    


def main():

    relevant_strings =[]

## Iterations

    for i in strings:
        string = i
        for j in keys:
            key = j


## Converts strings to HEX and creates a list with each byte being a different Item; This will help later with bitwise operators
            def to_hex(string, key):

                st = binascii.hexlify(string.encode('utf-8'))
                st = str(st,'ascii')
                to_hex.sp = [st[i:i+2] for i in range (0, len(st), 2)]
    
                ky = binascii.hexlify(key.encode('utf-8'))
                ky = str(ky,'ascii')
                to_hex.kp = [ky[i:i+2] for i in range (0, len(ky), 2)]
    
            to_hex(string, key)

            hex_string = to_hex.sp
            hex_key = to_hex.kp

## Performs Part 1 of the algorithm
            def AND_op(Bytes):
                l = []
                for s in Bytes:
        
                    c_s = int(s, 16)
                    s_1 = int('F', 16)
                    o_1 = hex(c_s & s_1)
                    l.append(o_1)
                return (l)
  
            trans_string = AND_op(hex_string)
            trans_key = AND_op(hex_key)

            trans_string = [int(x,16) for x in trans_string]
            trans_key = [int(y,16) for y in trans_key]

## Performs the XOR Op
            def XOR_op():


                short, long = sorted ((trans_string,trans_key), key=len)
                XOR_op.xored = list(hex(a^b) for a,b in zip(long, cycle(short)))
        
    
            XOR_op()

            xor_string = XOR_op.xored

## Brings the results together and generates a list

            xor_string = [x[2:] for x in xor_string]
            hex_string = [x[:-1] for x in hex_string]
            part_1_result =[''.join(z) for z in zip(hex_string,xor_string)]


            def List_to_String(s):

                str1=""
                for element in s:
                    str1+= element
                return str1
    
            part_1_result = List_to_String(part_1_result)
        
            decoded_result = bytearray.fromhex(part_1_result).decode()
        
            relevant_strings.append(decoded_result)

# Making all elements Lower Case for better match

    relevant_strings = [element.lower() for element in relevant_strings]
   

    def intersect(wordlist, relevant_strings):

        ret = []
        for i in wordlist:
            for j in relevant_strings:
                if i in j:
                    ret.append(j)
        return ret
    print(intersect(wordlist, relevant_strings))
    

if __name__ == "__main__": 
    main()
