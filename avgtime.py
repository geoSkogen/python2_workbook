import avgtime_data
import avgtime_node
import avgtime_nodes
import avgtime_pathfinder

def log_data_error(code_no, data_arr) :

    def redundant (data_arr) :
        print "error at data list [%i] - first and second list members cannot be equal" % data_arr[0]

    def zero (data_arr) :
        print "error at data list [%i][%i] - list members cannot be less than or equal to zero" % (data_arr[0], data_arr[1])

    def not_a_number (data_arr) :
        print "error at data list [%i][%i] - list members must be integers" % (data_arr[0], data_arr[1])

    def overflow (data_arr) :
        print "error at data list [%i] - lists must contain exactly three integers" % data_arr[0]

    options = {0: redundant, 1: zero, 2: not_a_number, 3: overflow}

    options[code_no](data_arr)

def normalize_data(data) :
    nodes = {}
    vals = []
    paths = []
    find = []
    new_node = {}
    node_objs = [0]
    inner_break = False

    for member in data :
        for datum in member :
            if (type(datum) != 'int') :
                log_data_error(2, [data.index(member),member.index(datum)])
                break
                return False
                inner_break = True
            elif (datum <= 0) :
                log_data_error(1, [data.index(member),member.index(datum)])
                break
                return False
                inner_break = True
        if (len(member) != 3) :
            log_data_error(3, [data.index(member)])
            break
            return False
        elif (member[0] == member[1]) :
            log_data_error(0, [data.index(member)])
            break
            return False
        elif (inner_break) :
            break
            return False


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
        node_objs.append({})
        paths = [int(node)]
        find = []
        for connected_node in nodes[node].keys() :
            if connected_node != "find" :
                paths.append(int(connected_node))
                #print ("node %s is connected to node %s by a distance of %i units" % (node, connected_node, nodes[node][connected_node]))
        for i in vals :
            if (not i in paths) :
                find.append(str(i))
        nodes[node]["find"] = find

    for nodename in nodes.keys() :
        paths = []
        find = []
        for keyname in nodes[nodename].keys() :
            if (keyname != "find") :
                paths.append([keyname,nodes[nodename][keyname]])
        find = nodes[nodename]["find"]
        new_node = avgtime_node.Node(nodename, paths, find)
        node_objs[int(nodename)] = new_node
        #new_node.report()
    del nodes
    del paths
    del find
    del vals
    del new_node
    return node_objs

def find_node_paths(nodes_obj, node_obj, connector) :
    paths = []
    for path_to in node_obj.find :
        paths.append(connector.find_path(nodes_obj, node_obj.name, path_to))
    return paths

def main() :
    temp_paths = []
    data_set_1 = normalize_data(avgtime_data.data_set_1)
    nodes = avgtime_nodes.Nodes(data_set_1)
    pathfinder = avgtime_pathfinder.Pathfinder(nodes)
    nodes.log_data()
    for i in range (1, len(nodes.data)) :
        for find_me in nodes.data[i].find :
            temp_paths = pathfinder.find_path(i,int(find_me))
            print "nodename: ", i
            print "testing_path_to: ", int(find_me)
            print temp_paths
    return nodes

nodes = main()
