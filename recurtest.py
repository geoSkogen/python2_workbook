def call_me(arg) :
    arg -= 1
    print arg
    while (arg > 0) :
        call_me(arg)

call_me(10)         
