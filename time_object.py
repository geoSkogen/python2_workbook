import time;

def weird_time_test() :
    ticks = time.time()
    localtime = time.localtime(ticks)
    asc_time = time.asctime(time.localtime(ticks))
    print localtime
    print asc_time

    for i in range(1000) :
        loopvar = time.clock()
        print i, " : ", loopvar
        print localtime
        print asc_time

weird_time_test()
