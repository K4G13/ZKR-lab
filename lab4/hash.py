import hashlib
import sys

if len(sys.argv) < 2: 
    print("Too few arguments!\nExiting ...")
    exit()

hash_func_name = sys.argv[1]
if hash_func_name not in hashlib.algorithms_available:
    print("No hash function found!")
    print("Available functions:")
    for _ in hashlib.algorithms_available:
        print(f"   {_}")
    print("Exiting ...")
    exit()

msg=""
if len(sys.argv) >= 3: 
    msg = "".join(sys.argv[2])
    for str in sys.argv[3:]:
        msg += " " + str
if msg == "":
    print("No text to hash!\nExiting ...")
    exit()

def hash_func(func_name,msg):
    func = getattr(hashlib, func_name)
    return func(msg.encode()).hexdigest()

print(hash_func(hash_func_name,msg))