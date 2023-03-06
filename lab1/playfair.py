print("\n  Playfair encoder/decoder\n")
print("Choose mode:\n  [1]: encode\n  [2]: decode")
mode = ""
while(True):
    mode = input()
    if mode == '1' or mode == '2': break

#ENCODE
if mode == '1':
    print("ENCODER")

#DECODE
elif mode == '2':
    print("DECODER")

else:
    print("???")