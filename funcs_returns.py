def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return  a/b

def getInput(selectIn):
    left = int(raw_input("term 1 : "))
    right = int(raw_input("term 2 : "))
    if selectIn == "A":
        result = add(left, right)
        label = "sum"
    elif selectIn == "S":
        result = subtract(left, right)
        label = "difference"
    elif selectIn == "M":
        result = multiply(left, right)
        label = "product"
    elif selectIn == "D":
        result = divide(left, right)
        label = "product"
    print("%s: %d" % (label, result))
    initInput()

def initInput():
    prompt = "> "
    print ("type A, S, M, or D")
    selector = raw_input(prompt)
    if selector == "A" or selector == "S" or selector == "M" or selector == "D":
        getInput(selector)
    else:
        print ("unrecognized character")
        initInput()

initInput()
