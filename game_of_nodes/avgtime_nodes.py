class Nodes :
    def __init__(self, node_data) :
        self.data = node_data

    def log_data(self) :
        for i in range(1, len(self.data)) :
            print "\r\n%s" % self.data[i].name
            for keyname in self.data[i].distance_index.keys() :
                print ("\t%s:  %i" % (keyname, self.data[i].distance_index[keyname]))

    def format_print_log(obj,str) :
        print ("\r\n%s" % name)
        for keyname in obj :
            print ("\t%s %i" % (keynane, obj[keyname]))

    def log_descriptors(self):
        descriptors = [self.hubs, self.branches, self.dead_ends]
        strings = ["hubs", "branches", "dead_ends"]
        for descriptor in descriptors :
            format_print_log(descriptor,name)

    def is_node(self,int1) :
        if (type(int1) != int) :
            return False
        if (int1 >= len(self.data) or int1 <= 0) :
            return False
        return True

    def are_neighbors(self, int1, int2) :
        result = [[],[],False]
        if (self.is_node(int1) and self.is_node(int2)) :
            if str(int2) in self.data[int1].neighbors :
                result[0] = str(int1)
                result[1].append(str(int2))
                result[1].append(self.data[int1].distance_index[str(int2)])
                result[2] = True
        return result

    def is_triad(self, start_node, end_node) :
        this = self.data
        result = [[],['0',0,'0',0,],False]
        if (self.is_node(start_node) and self.is_node(end_node)) :
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

    def is_quatrain(self, start_node, end_node) :
        this = self.data
        result = [[],['0',0,'0',0,'0',0],False]
        inner_break = False
        if (self.is_node(start_node) and self.is_node(end_node)) :
            start_neighbors = this[start_node].neighbors
            end_neighbors = this[end_node].neighbors
            for start_neighbor in start_neighbors :
                if (inner_break) :
                    break
                for end_neighbor in end_neighbors :
                    if self.are_neighbors(int(start_neighbor),int(end_neighbor)) :
                        result[2] = True
                        result[0] = start_node
                        result[1][0] = str(start_neighbor)
                        result[1][1] = this[start_node].distance_index[start_neighbor]
                        result[1][2] = str(end_neighbor)
                        result[1][3] = this[int(start_neighbor)].distance_index[end_neighbor]
                        result[1][4] = str(end_node)
                        result[1][5] = this[int(end_neighbor)].distance_index[str(end_node)]
                        inner_break = True
                        break
            if (result[2] == False or self.are_neighbors(start_node, end_node) or start_node == end_node) :
                result[0] = start_neighbors
                result[1] = end_neighbors
                result[2] = False
        return result

    def is_quintrain(self, start_node, end_node) :
        this = self.data
        result = [[],['0',0,'0',0,'0',0,'0',0],False]
        inner_break = False
        middle_node = 0
        if (self.is_node(start_node) and self.is_node(end_node)) :
            start_neighbors = this[start_node].neighbors
            end_neighbors = this[end_node].neighbors
            for start_neighbor in start_neighbors :
                if (inner_break) :
                    break
                for end_neighbor in end_neighbors :
                    test_result = self.is_triad(int(start_neighbor),int(end_neighbor))
                    if (test_result[2]) :
                        result[2] = True
                        result[0] = start_node
                        result[1][0] = str(start_neighbor)
                        result[1][1] = this[start_node].distance_index[start_neighbor]
                        result[1][2] = test_result[1][0]
                        result[1][3] = test_result[1][1]
                        result[1][4] = test_result[1][2]
                        result[1][5] = this[int(test_result[1][0])].distance_index[end_neighbor]
                        result[1][6] = str(end_node)
                        result[1][7] = this[int(end_neighbor)].distance_index[str(end_node)]
                        inner_break = True
                        break
            if (result[2] == False or self.are_neighbors(start_node, end_node) or start_node == end_node) :
                result[0] = start_neighbors
                result[1] = end_neighbors
                result[2] = False
        return result
