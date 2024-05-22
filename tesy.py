def ETCount() :
    file = open ('TESTFILE.TXT', 'r')
    lines = file.readlines()
    countE=0
    countT=0
    for w in lines :
        for ch in w:
            if ch in 'Ee':
                countE = countE + 1
            elif ch in 'Tt':
                countT=countT + 1
    print ("The number of E or e : ", countE)
    print ("The number of T or t : ", countT)
    file.close()
ETCount()
