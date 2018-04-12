class Pathfinder() :
    def __init__(self, smart_data, node_map) :
        self.from_home = False
        self.smart_data = smart_data
        self.node_map = node_map
        self.foretrace = []
        self.backtrace = []
        self.path = []

    def force_path(self, switch_index, start_node, end_node) :
        nodes = self.smart_data
        result = []
        switch_options = [
            [[],[],False],
            [[],[],False],
            nodes.are_neighbors,
            nodes.is_triad,
            nodes.is_quatrain,
            nodes.is_quintrain
            ]
        result = switch_options[switch_index](start_node, end_node)
        return result

    def call_path(self, start_node, end_node) :
        result = []
        for i in range (2,5) :
            result = self.force_path(i, start_node, end_node)
            if (result[2] == True) :
                break
        return result

    def format_path_data(self, last_report) :
        key_val = {}
        key_val_end = {}
        data = []
        for i in range (len(last_report[1])) :
            if (i % 2 == 0) :
                key_val[last_report[1][i]] = last_report[1][i+1]
                data.append(key_val)
        return data

    def assoc_path(self, true_report) :
        report = []
        stage_datum = []
        home_node = self.backtrace[0][0]
        goal_node = self.foretrace[0][0]
        #central_triad = [true_report[0],int(true_report[1][0]),int(true_report[1][2])]

        print "backtrace: ", self.backtrace
        print "foretrace: ", self.foretrace
        print "true_report: ", true_report
        #print "central_triad: ", central_triad
        self.reset()
        return report

    def path_logic(self, test_node_neighbors, control_nodes) :
        path_logic_report = []
        inner_break = False
        for neighbor_name in test_node_neighbors :
            for control_node in control_nodes :
                if (control_node not in self.node_map.dead_ends.keys() and neighbor_name not in self.node_map.dead_ends.keys()) :
                    path_logic_report = self.call_path(int(control_node),int(neighbor_name))
                    print ("call_triad(%i,%i)" % (int(control_node),int(neighbor_name)))
                    print "log_path_logic_report: ", path_logic_report
                    if (((type(path_logic_report) == bool) and (path_logic_report)) or (path_logic_report[2])) :
                        self.assoc_path(path_logic_report)
                        inner_break = True
                        break
            if (inner_break) :
                break
        return path_logic_report

    def find_path(self, home_node, goal_node) :
        formatted_data = []
        path_report = [[],[],False]
        if (self.smart_data.are_neighbors(home_node, goal_node)) :
            formatted_data = [{str(goal_node):self.smart_data.data[home_node].distance_index[str(goal_node)]}]
            return formatted_data
        self.backtrace.append([str(home_node)])
        self.foretrace.append([str(goal_node)])
        while (len(self.backtrace) >= 1 or len(self.foretrace) >=1) :
            if (self.from_home) :
                path_report = self.path_logic(self.backtrace[-1], self.foretrace[-1])
                print "backtrace_appending_home_neighbors: ", path_report[0]
                print "from_home: ", self.from_home
                print "log_toggling_path_report:", path_report
                self.toggle_direction()
                self.backtrace.append(path_report[0])
            else :
                path_report = self.path_logic(self.backtrace[-1], self.foretrace[-1])
                print "foretrace_appending_goal_neighbors: ", [path_report[1]]
                print "from_home: ", self.from_home
                print "log_toggling_path_report:", path_report
                self.toggle_direction()
                self.foretrace.append(path_report[1])
        print "path_report:"
        print path_report
        return formatted_data

    def toggle_direction(self) :
        self.from_home = not self.from_home

    def reset(self) :
        self.foretrace = []
        self.backtrace = []
        self.path = []
        self.from_home = False
