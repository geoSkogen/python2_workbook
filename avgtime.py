import avgtime_data
import avgtime_node
import avgtime_nodes
import avgtime_pathfinder

def normalize_data(data) :
    nodes = {}
    vals = []
    paths = []
    find = []
    new_node = {}
    node_objs = [0]

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
        for keyname in nodes[nodename] :
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
    pathfinder = avgtime_pathfinder.Pathfinder()
    for node in nodes.data :
        temp_paths.append(find_node_paths(nodes, node, pathfinder))
    for i in range(len(temp_paths)-1) :
        






nodes.log_data()
hello = pathfinder.find_path(nodes,1,3)
hellno = pathfinder.find_path(nodes,1,9)
print hello
print hellno


'''
def force_path(start_node, end_node) :
    path_logic_report = []
    path_report = []
    node_backtrace = [end_node]
    node_home = [start_node]
    from_home = False
    error_report = []

    path_report = is_triad(start_node, end_node)

    def path_logic(path_report, from_home) :
        format_data =  []
        recourse = []
        index = 0

        def search_neighbors(this_bool, next_node, failed_node) :
            search_report = []
            this_bool = not this_bool
            search_report.append([next_node, failed_node])
            for path in get_neighbors(next_node) :
                search_report.append(is_triad(path, failed_node))
            return search_report

        if (path_report[2] == False ) :
            if (from_home == False) :
                node_backtrace.append(end_node)
                recourse.append(end_node)
                recourse.append(search_neighbors(from_home, end_node, start_node))
            else :
                node_home.append(start_node)
                recourse.append(start_node)
                recourse.append(search_neighbors(from_home, start_node, end_node))
        elif (path_report[2] == True) :
            format_data.append({path_report[1][0] : path_report[1][1]})
            if (len(node_backtrace) == 1 and len(node_home) == 1) :
                format_data.append({path_report[1][2] : path_report[1][3]})
                node_backtrace.pop()
                node_home.pop()
            else :
                if (from_home == False) :
                    from_home = True
                    index = len(node_backtrace) - 1
                    error_report.append(index)
                    for path in get_neighbors(node_backtrace[index]) :
                        path_report = is_triad(start_node, path)
                        error_report.append(path_report)
                else :
                    from_home == False
                    index = len(node_home) - 1
                    for path in get_neighbors(node_home[index]) :
                        path_report = is_triad(path, end_node)
        return format_data
    path_logic_report = path_logic(path_report, from_home)

    return path_logic_report



def get_triads(nodes) :
    report = []
    for nodename in nodes.keys() :
        for pathname in nodes[nodename]["find"] :
            report = force_path(int(nodename),int(pathname))
            print report

nodes = normalize_data(avgtime_data.data_set_1)
get_triads(nodes)
'''
