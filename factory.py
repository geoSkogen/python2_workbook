from sys import argv

def atom_smasher(arr) :
    storeval = 1
    int_elm = 0
    for elm in arr :
        int_elm = int(elm)
        storeval *= int_elm
    return storeval

def format_argv(arr) :
    if (len(arr) > 1) :
        arr.remove(arr[0])
        return arr
    else :
        return [1]

def init_smash() :
    arg_arr = format_argv(argv)
    result = atom_smasher(arg_arr)
    print result
    return result
#init_smash()

def keywordarg(mystr) :
    print ("the oil is in the %s" % mystr)
    return mystr

#keywordarg(mystr = "drill")

def overloader(arg1, *vartuple) :
    counter = 0
    print("this is arg1: %s" % arg1)
    for elm in vartuple :
        print("this is vartuple[%i]: %s" % (counter, elm))
        counter += 1

def calloverloader() :
    title = "we are your overloaders"
    data = []
    overloader(title,"you","could","have","a","dream","about", "drowning","in","oil")

#calloverloader()
