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

keywordarg(mystr = "drill")
