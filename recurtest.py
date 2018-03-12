def call_me(arg) :

    print arg
    while (arg > 0) :
        arg -= 1
        call_me(arg)

call_me(2)
