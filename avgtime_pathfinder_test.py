def main() :
    alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    def is_triad(this_list,arg1,arg2) :
        my_neighbors1 = []
        my_neighbors2 = []
        neighbors = []
        path_report = [[],[],[],False]
        if (arg1 == this_list[0]) :
            my_neighbors1.append(this_list[1])
        elif (arg2 == this_list[0]) :
            my_neighbors2.append(this_list[1])
        elif (arg1 == this_list[len(this_list)-1]) :
            my_neighbors1.append(this_list[len(this_list)-2])
        elif (arg2 == this_list[len(this_list)-1]) :
            my_neighbors2.append(this_list[len(this_list)-2])
        else :
            my_neighbors1.append(this_list[this_list.index(arg1)-1])
            my_neighbors1.append(this_list[this_list.index(arg1)+1])
            my_neighbors2.append(this_list[this_list.index(arg2)-1])
            my_neighbors2.append(this_list[this_list.index(arg2)+1])
        for neighbor in my_neighbors1 :
            if neighbor in my_neighbors2 :
                path_report[0] = arg1
                path_report[1] = neighbor
                path_report[2] = arg2
                path_report[3] = True
                break
        return path_report

    def force_path(a_list) :
        from_a = False
        result = []
        backtrace = []
        foretrace = []
        backtrace.append(a_list[0])
        foretrace.append(a_list[len(a_list)-1])
        arg1 = backtrace[len(backtrace)-1]
        arg2 = foretrace[len(foretrace)-1]
        result = is_triad(alph,arg1,arg2)
        print result
        print arg1
        print arg2
        while (len(backtrace) >= 1 or len(foretrace) >= 1) :
            #if ((a_list.index(arg1) - a_list.index(arg2) == 1) or (a_list.index(arg1) - a_list.index(arg2) == -1)) :
            #    break
            if (result[3] == False ) :
                print arg1, "\t", arg2
                print backtrace;
                print foretrace;
                if (a_list.index(arg2) - a_list.index(arg1) > 0) :
                    if (not from_a) :
                        arg1 = a_list[a_list.index(arg1)]
                        arg2 = a_list[a_list.index(arg2)-1]
                        foretrace.append(arg2)
                        from_a = not from_a
                    else :
                        arg1 = a_list[a_list.index(arg1)+1]
                        arg2 = a_list[a_list.index(arg2)]
                        backtrace.append(arg1)
                        from_a = not from_a
                    result = is_triad(alph, arg1, arg2)
                    print arg1
                    print arg2
                    print result
                else:
                    if (not from_a) :
                        arg1 = a_list[a_list.index(arg1)-1]
                        arg2 = a_list[a_list.index(arg2)]
                        foretrace.append(arg1)
                        from_a = not from_a
                    else :
                        arg1 = a_list[a_list.index(arg1)]
                        arg2 = a_list[a_list.index(arg2)+1]
                        backtrace.append(arg2)
                        from_a = not from_a
                    result = is_triad(alph, arg1, arg2)
                    print arg1
                    print arg2
                    print result
            else :
                backtrace = []
                foretrace = []
                break
        return result

    result = force_path(alph)
    #result = is_triad(alph,'l','n')
    print result

main()
