import avgtime_data_complex
#import avgtime_data
import avgtime_normalizer
import avgtime_node
import avgtime_nodes
import avgtime_pathfinder

def main() :
    temp_paths = []
    data_set_1 = []
    nodes = []
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
        pathfinder = avgtime_pathfinder.Pathfinder(nodes)
        nodes.log_data()
        '''
        for i in range (1, len(nodes.data)) :
            for find_me in nodes.data[i].find :
                print "\r\nnodename: ", i
                print "testing_path_to: ", int(find_me)
                temp_paths = pathfinder.find_path(i,int(find_me))
                print temp_paths
        '''        
        return nodes
        #return data_set_1
nodes = main()
