import sys

secret_text = ""
key_as_num = 1

# Ascii Code Limits
upper_limit = 32
lower_limit = 126

# Cmdline Parameters
do_what = sys.argv[1]
raw_file = sys.argv[2]

def caesar_encode(text):
    global secret_text
    for char in text:
        secret_ascii = ord(char)
        if secret_ascii != lower_limit and secret_ascii != upper_limit:
            secret_ascii += key_as_num
        secret_text += chr(secret_ascii)
    return secret_text

def caesar_decode(text):
    global secret_text
    for char in text:
        secret_ascii = ord(char)
        if secret_ascii != lower_limit and secret_ascii != upper_limit:
            secret_ascii -= key_as_num
        secret_text += chr(secret_ascii)
    return secret_text

def fileWrite(methode):
    if methode == 0:
        with open(raw_file+".crypt", "w") as file:
             file.write(secret_text)
    else:
        with open(raw_file+".decrypt", "w") as file:
             file.write(secret_text)
        
def fileOpen(methode):
    with open(raw_file, "r") as file:
        raw_data = file.read()
        #print(caesar_decode(raw_data))
        if methode == 0:
            caesar_encode(raw_data)
        else:
            caesar_decode(raw_data)
        fileWrite()

if do_what == "encode":
    print("[+] File: " + raw_file + " encrypting...")
    fileOpen(0)
elif do_what == "decode":
    print("[+] File: " + raw_file + " decrypting...")
    fileOpen(1)
else:
    print("[-] Failure. Please start: python caesarCrypt.py [encode/decode] [file]")