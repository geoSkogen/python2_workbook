class Node :
    def __init__(self, name, neighbor_data, find) :
        self.neighbors = []
        self.distance_index = {}
        self.find = []
        self.name = str(name)
        self.find = find
        for neighbor in neighbor_data :
            self.neighbors.append(str(neighbor[0]))
            self.distance_index[str(neighbor[0])] = neighbor[1]

    def report(self) :
        print("%s" % self.name)
        for keyname in self.distance_index.keys() :
            print("\t%s:\t%i" % (keyname, self.distance_index[keyname]))
