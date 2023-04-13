import hashlib
import sys
import re

if len(sys.argv) < 2: 
    print("\033[91mToo few arguments!\nExiting ...\033[0m")
    exit()

hash_func_name = sys.argv[1]
if hash_func_name not in hashlib.algorithms_available:
    print("\033[91mNo hash function found!")
    print("Available functions:")
    for methode in hashlib.algorithms_available:
        if re.search("^sha[0-9]+$",methode) or re.search("^sha3_[0-9]+$",methode) or methode=="md5":
            print(f"   {methode}")
    print("Exiting ...\033[0m")
    exit()

msg=""
if len(sys.argv) >= 3: 
    msg = "".join(sys.argv[2])
    for str in sys.argv[3:]:
        msg += " " + str
if msg == "":
    print("\033[91mNo text to hash!\nPass more arguments\nExiting ...\033[0m")
    exit()

def hash_func(func_name,msg):
    func = getattr(hashlib, func_name)
    return func(msg.encode()).hexdigest()

print(hash_func(hash_func_name,msg))