#log colors
class lc:
    G = '\033[92m'  #Green
    Y = '\033[93m'  #Yellow
    R = '\033[91m'  #Red
    N = '\033[0m'   #Normal

# Test pojedynczych bitów
def singleBitTest(bitArray):
    count = 0
    for el in bitArray:
        if el == 1: count += 1

    print(f"Single bit test: ",end="")
    if 9725 < count < 10275:
        print(f"{lc.G}POSITIVE{lc.N}")
        return True
    else: 
        print(f"{lc.R}NEGATIVE{lc.N}")
        return False

# Test serii
def seriesTest(bitArray):
    series = {
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6+": 0 }

    count = 0
    for i in range(len(bitArray)):
        if bitArray[i] == 1: count += 1
        if bitArray[i] == 0 or i == len(bitArray) - 1:
            if count == 1: series["1"] += 1
            elif count == 2: series["2"] += 1
            elif count == 3: series["3"] += 1
            elif count == 4: series["4"] += 1
            elif count == 5: series["5"] += 1
            elif count >= 6: series["6+"] += 1
            count = 0

    # print(series)
    print(f"Series test: ",end="")
    if (2315 < series["1"]  < 2686 and 
        1114 < series["2"]  < 1386 and
        527  < series["3"]  < 723  and
        240  < series["4"]  < 384  and 
        103  < series["5"]  < 209  and 
        103  < series["6+"] < 209):
        print(f"{lc.G}POSITIVE{lc.N}")
        return True
    else: 
        print(f"{lc.R}NEGATIVE{lc.N}")
        return False

# Test długiej serii
def longSeriesTest(bitArray):
    print(f"Long series test: ",end="")

    count_0 = 0
    count_1 = 0
    for i in range(len(bitArray)):
        if bitArray[i] == 0: 
            count_0 += 1
            count_1 = 0
        if bitArray[i] == 1: 
            count_1 += 1
            count_0 = 0
        if count_0 >= 26 or count_1 >= 26:
            print(f"{lc.R}NEGATIVE{lc.N}")
            return False
        
    print(f"{lc.G}POSITIVE{lc.N}")
    return True

# Test pokerowy
def pokerTest(bitArray):
    segments = []
    segNr = 5000
    segSize = int(len(bitArray)/segNr)
    for i in range(segNr):
        segments.append(bitArray[i*segSize:(i+1)*segSize])
    
    segmentsDec = []
    for el in segments:
        decVal = 0
        for i in range(len(el)):
            decVal += el[i]*2**(len(el)-i-1)
        segmentsDec.append(decVal)

    s = []
    for i in range(2**segSize):
        count = 0
        for el in segmentsDec:
            if el == i: count += 1
        s.append(count)
        # print(i, s[i])

    x = 0
    for i in range(2**segSize):
        x+=s[i]**2
    x = (16/5000)*x - 5000
    # print(x)
    
    print(f"Poker test: ",end="")
    if 2.16 < x < 46.17:
        print(f"{lc.G}POSITIVE{lc.N}")
        return True
    else: 
        print(f"{lc.R}NEGATIVE{lc.N}")
        return False
    
    