class Map :
    def __init__(self, smart_data) :
        self.smart_data = smart_data
        self.hubs = {}
        self.hub_net = {}
        self.hub_suburbs = {}
        self.dead_ends = {}
        self.branches = {}
        self.hub_score = 4
        self.net_score = 0
        self.node_ranks = {}
        datum = {}
        data = self.smart_data.data
        nodes = self.smart_data
        for i in range(1, len(data)) :
            datum = data[i]
            if (not datum.node_score in self.node_ranks.keys()) :
                self.node_ranks[str(datum.node_score)] = []
            if (datum.node_score > self.net_score) :
                self.net_score = datum.node_score
            if (datum.node_score >= 3 and datum.node_score < self.hub_score) :
                self.branches[str(i)] = datum
            elif (datum.node_score == 1) :
                self.dead_ends[str(i)] = datum
            elif (datum.node_score >= self.hub_score) :
                self.hubs[str(i)] = datum
        for hubkeyname in self.hubs.keys() :
            self.hub_net[hubkeyname] = []
            for neighbor in self.hubs[hubkeyname].neighbors :
                if (neighbor not in self.hub_suburbs.keys() and neighbor not in self.dead_ends.keys()) :
                    self.hub_suburbs[neighbor] = data[int(neighbor)]
                if (neighbor in self.hubs) :
                    self.hub_net[hubkeyname].append(neighbor)

    def log_data(self) :
        print "\thubs:"
        print self.hubs.keys()
        print "\thub_net:"
        for keyname in self.hub_net.keys() :
            print "\t%s:" % keyname;
            for datum in self.hub_net[keyname] :
                print "\t\t%s" % datum
        print "\thub_suburbs:"
        print self.hub_suburbs.keys()
        print "\tbranches:"
        print self.branches.keys()
        print "\tdead_ends:"
        print self.dead_ends.keys()
        print "\tnode_ranks:"
        print self.node_ranks.keys()
