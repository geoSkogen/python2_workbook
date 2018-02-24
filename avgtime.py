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

def find_paths(nodes) :
    new_path = []
    data_loader = {}

    def path_back(node, destination) :
        result = [[], False]
        for nextnode_keyname in node.keys() :
            if (nextnode_keyname != "find") :
                if nextnode_keyname in nodes[destination].keys() :
                    result[0].append(nextnode_keyname)
                    result[0].append(node[nextnode_keyname])
                    result[0].append(destination)
                    result[0].append(nodes[destination][nextnode_keyname])
                    result[1] = True
                else :
                    for destination_keyname in nodes[str(destination)].keys() :
                        if (destination_keyname != "find") :
                            result[0].append(destination_keyname)

        return result

    for nodename in nodes :
        new_path = []
        for path in nodes[nodename]["find"] :
            data_loader = {}
            new_path = path_back(nodes[nodename], path)
            if (new_path[1] == True) :
                for i in range(len(new_path[0])-1) :
                    if (isinstance(new_path[0][i],str)) :
                        data_loader[new_path[0][i]] = new_path[0][i+1]
            print ("\r\nstarting at: %s --- destination: %s" % (nodename, path))
            print "path taken: ", new_path
            print data_loader
            

    return nodes

node_data = normalize_data(data1)
print_pretty(node_data)
data_set = find_paths(node_data)
print data_set
