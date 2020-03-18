# tempConvert.py
TempStr = input("Please input temperature with symbol (F or C): ")
if TempStr[-1] in ['F', 'f']:
    new = (eval(TempStr[0:-1]) - 32)/1.8
    print("After transformation: {:.2f}C".format(new))
elif TempStr[-1] in ['C', 'c']:
    new = 1.8*eval(TempStr[0:-1]) - 32
    print("After transformation: {:.2f}C".format(new))
else:
    print("Input error. E.x.: 10C, 80F")
