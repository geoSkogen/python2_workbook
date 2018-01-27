def its_her_factory (listarg1, listarg2) :
    local_list = []
    if (len(listarg2) == len(listarg1)) :
        for i in range(len(listarg1)) :
          local_list.append(listarg1[i] + listarg2[i])
          print len(local_list)
          print local_list
    else:
        print "lists of unequal length"
    return local_list

listylist1 = [1,2,3,4,5,6,7,8,9]
listylist2 = [1,35,2,67,3,94,5,67,1]

newobj = its_her_factory(listylist1, listylist2)

print newobj
