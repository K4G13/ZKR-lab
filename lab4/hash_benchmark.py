import random 
import hashlib
import re
import time

#generate array of random string
strings = []
for _ in range(10000):
    str = ""
    for _ in range( random.randint(10,255) ):
        random_letter = chr( random.randint(ord('a'),ord('z')) )
        str += random_letter
    strings.append(str)

def test(func): 
    timer_start = time.time()
    for str in strings:        
        func(str.encode())
    timer_stop = time.time()
    estimated_time = (timer_stop - timer_start)*1000

    length = 0
    for str in strings:        
        length += len(func(str.encode()).hexdigest())
    length = int(length/len(strings))

    test_str = "Hat"
    test_str2 = "Cat"
    hex_dict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'a': '1010', 'b': '1011', 'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'}
    binary = ''
    binary2 = ''
    for digit in func(test_str.encode()).hexdigest():
        binary += hex_dict[digit]    
    for digit in func(test_str2.encode()).hexdigest():
        binary2 += hex_dict[digit]     
    changed = 0

    for i in range(len(binary)):
        if binary[i]!=binary2[i]:
            changed += 1

    bits_changed_percentage = round(changed/len(binary) * 100,2)
    
    return (estimated_time,length,bits_changed_percentage)

statistics = {}
for methode in hashlib.algorithms_available:
    if re.search("^sha[0-9]+$",methode) or re.search("^sha3_[0-9]+$",methode) or methode=="md5":
        statistics[methode] = test(getattr(hashlib, methode))

statistics = dict(sorted(statistics.items(), key=lambda item: item[1][0]))
print(f"|{'Name:':<12}|{'Time[ms]:':<24}|{'Hash length:':<24}|{'Change %:':<24}|")
for _ in range(14+25*3): print("-",end="")
print("")
for item in statistics:
    print(f"|{item:<12}|",end="")
    for el in statistics[item]:
        print(f"{el:<24}|",end="")
    print("")
