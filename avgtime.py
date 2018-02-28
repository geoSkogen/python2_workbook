data1 = [
       [1,2,3],
       [2,3,4],
       [2,4,8],
       [3,4,6],
       [4,6,7],
       [4,5,10],
       [7,9,3],
       [7,8,6],
       [4,7,20],
       [5,7,15]
       ]

def normalize_data(data) :
    nodes = {}
    vals = []
    paths = []
    find = []

    for member in data :
    #insert data validation here --- each member must a list of three numbers
        if (not member[0] in vals) :
            nodes[str(member[0])] = {}
            vals.append(member[0])
        if (not member[1] in vals) :
            nodes[str(member[1])] = {}
            vals.append(member[1])
        nodes[str(member[0])][str(member[1])] = member[2]
        nodes[str(member[1])][str(member[0])] = member[2]

    for node in nodes.keys() :
        paths = [int(node)]
        find = []
        for connected_node in nodes[node].keys() :
            if connected_node != "find" :
                paths.append(int(connected_node))
                print ("node %s is connected to node %s by a distance of %i units" % (node, connected_node, nodes[node][connected_node]))
        for i in vals :
            if (not i in paths) :
                find.append(str(i))
        nodes[node]["find"] = find
    return nodes

def print_pretty(this_dict) :
    for keyname in this_dict.keys() :
        print ("node name: %s" % keyname)
        for sibname in this_dict[keyname].keys() :
            print ("\tsibling name: %s" % sibname )
            if (isinstance(this_dict[keyname][sibname],int)) :
                print ("\t\tvalue: %i" % this_dict[keyname][sibname])
            else :
                for lostnode in this_dict[keyname][sibname] :
                    print ("\t\t%s" % lostnode)
    return

def get_neighbors(node) :
    node_name = str(node)
    keys = []
    for member in nodes[node_name].keys() :
        if (member != "find") :
            keys.append(member)
    return keys

def are_neighbors(start_node, end_node) :
    result = False
    node_name = str(start_node)
    neighbors = get_neighbors(end_node)
    if (node_name in neighbors) :
        result = True
    return result

def force_path(start_node, end_node) :
    path_report = []
    format_data =  []
    node_backtrace = [end_node]
    node_home = [start_node]
    from_home = False
    index = -1

    while (len(node_backtrace) >= 1) :
        path_report = is_triad(start_node, end_node)
        if (path_report[2] == True) :
            format_data.append({path_report[1][0] : path_report[1][1]})
            if (len(node_backtrace) == 1) :
                format_data.append({path_report[1][2] : path_report[1][3]})
                node_backtrace.pop()
            else :
                if (from_home == False) :
                    from_home = True
                    index = len(node_backtrace) - 1
                    for path in get_neighbors(node_backtrace[index]) :
                        end_node = path
                else :
                    from_home == False
                    index = len(node_home) - 1
                    for path in get_neighbors(node_home[index]) :
                        start_node = path
        else :
            if (from_home == False) :
                from_home = True
                index = len(node_backtrace) - 1
                for path in get_neighbors(node_backtrace[index]) :
                    end_node = path
            else :
                from_home == False
                index = len(node_home) - 1
                for path in get_neighbors(node_home[index]) :
                    start_node = path
    return format_data

def is_triad(start_node, end_node) :
    result = [[],[],False]
    start_neighbors = get_neighbors(start_node)
    end_neighbors = get_neighbors(end_node)
    for middle_node in start_neighbors :
       if (middle_node in end_neighbors) :
           result[2] = True
           result[0].append(str(start_node))
           result[1].append(middle_node)
           result[1].append(nodes[str(start_node)][middle_node])
           result[1].append(str(end_node))
           result[1].append(nodes[str(end_node)][middle_node])
           break
    if (result[2] == False) :
        result[0] = start_neighbors
        result[1] = end_neighbors
    return result

def get_triads(nodes) :
    report = []
    for nodename in nodes.keys() :
        for pathname in nodes[nodename]["find"] :
            report = force_path(int(nodename),int(pathname))
            print report

nodes = normalize_data(data1)
get_triads(nodes)
