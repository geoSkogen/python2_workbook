import avgtime_data_complex
#import avgtime_data
import avgtime_normalizer
import avgtime_node
import avgtime_nodes
import avgtime_map
import avgtime_pathfinder

def main() :
    result = {}
    data_set_1 = []
    nodes = []
    map = {}
    pathfinder = {}
    data_methods = avgtime_normalizer
    data_error = data_methods.validate_data(avgtime_data_complex.data_set_1)
    #data_error = data_methods.validate_data(avgtime_data.data_set_1)
    if (data_error) :
        return False
    else :
        data_set_1 = data_methods.normalize_data(avgtime_data_complex.data_set_1)
        #data_set_1 = data_methods.normalize_data(avgtime_data.data_set_1)
        nodes = avgtime_nodes.Nodes(data_set_1)
        map = avgtime_map.Map(nodes)
        pathfinder = avgtime_pathfinder.Pathfinder(nodes, map)
        nodes.log_data()
        map.log_data()
        '''
        for hub in map.hubs :
            for branch in map.branches :
                print "\r\nhubname: %s " % hub
                print "testing_path_to: %s " % branch
                temp_paths = pathfinder.find_path(int(hub),int(branch))
                print temp_paths
        '''        
        '''
        for i in range (1, len(nodes.data)) :
            for find_me in nodes.data[i].find :
                print "\r\nnodename: ", i
                print "testing_path_to: ", int(find_me)
                temp_paths = pathfinder.find_path(i,int(find_me))
                print temp_paths
        '''
        result = {"nodes" : nodes, "map" : map, "pathfinder" : pathfinder}
        return result
        #return data_set_1
avgtime = main()
