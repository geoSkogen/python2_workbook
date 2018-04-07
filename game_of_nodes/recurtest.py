

def logic_me(arg1, arg2, reverse) :
    result = [0,0,False]
    if (arg1 > arg2) :
        print ("%i greater than %i" % (arg1, arg2))
        if (reverse) :
            arg2 += 1
            print ("incremented %i to %i" % (arg2 - 1, arg2))
        else :
            arg1 -=1
            print ("decremented %i to %i" % (arg1 + 1, arg1))
    elif (arg2 > arg1) :
        print ("%i greater than %i" % (arg2, arg1))
        if (reverse) :
            arg1 +=1
            print ("incremented %i to %i" % (arg1 - 1, arg1))
        else :
            arg2 -= 1
            print ("decremented %i to %i" % (arg2 + 1, arg2))
    else :
        print "="
        result[2] = True
    if (arg1 == arg2) :
        print "="
        result[2] = True
    result[0] = arg1
    result[1] = arg2
    return result


def call_me(arg1, arg2) :
    myarr = [arg1, arg2]
    two = myarr[-1]
    one = myarr[-2]
    myresult = []
    reverse = False
    if (arg1 > arg2) :
        reverse =  True
    while (len(myarr) != 0) :
        print ("while my array has at least two members: %i and %i" % (one, two))
        if (reverse) :
            myresult = logic_me(two,one,reverse)
        else :
            myresult = logic_me(one,two,reverse)
        if (myresult[2]) :
            reverse = True
            for i in range(len(myarr)) :
              myarr.pop()
        else :
            myarr.append(myresult[0])
            myarr.append(myresult[1])
            reverse = not reverse
            two = myarr[-1]
            one = myarr[-2]
        print myresult
        print myarr

call_me(-12,24)
