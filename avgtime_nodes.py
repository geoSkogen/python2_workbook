class Nodes :
    def __init__(self, node_data) :
        self.data = node_data

    def log_data(self) :
        for i in range(1, len(self.data)) :
            print "\r\n%s" % self.data[i].name
            for keyname in self.data[i].distance_index.keys() :
                print ("\t%s:  %i" % (keyname, self.data[i].distance_index[keyname]))

    def are_neighbors(self, int1, int2) :
        result = False
        if str(int2) in self.data[int1].neighbors :
            result = True
        return result

    def is_triad(self, start_node, end_node) :
        this = self.data
        result = [[],['0',0,'0',0],False]
        start_neighbors = this[start_node].neighbors
        end_neighbors = this[end_node].neighbors
        for middle_node in start_neighbors :
           if (middle_node in end_neighbors) :
               result[2] = True
               result[0] = start_node
               result[1][0] = str(middle_node)
               result[1][1] = this[start_node].distance_index[middle_node]
               result[1][2] = str(end_node)
               result[1][3] = this[end_node].distance_index[middle_node]
               break
        if (result[2] == False or self.are_neighbors(start_node, end_node) or start_node == end_node) :
            result[0] = start_neighbors
            result[1] = end_neighbors
            result[2] = False
        return result
