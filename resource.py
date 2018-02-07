def demo(arg) :
    print ("I want all the %s" % arg)
    return arg

def rev_str(arg) :
    newstr = ""
    for i in range(len(arg)) :
        newstr += arg[len(arg) - (i + 1)]
    print ("your new string is: \"%s\"" % newstr)
    return newstr

def index_of(datum, arr) :
    result = -1
    for i in range(len(arr)) :
        if (arr[i] == datum) :
            result = i;
    return result
