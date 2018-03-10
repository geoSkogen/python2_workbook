class Pathfinder() :
    def __init__(self, smart_data) :
        self.from_home = False
        self.smart_data = smart_data
        self.foretrace = []
        self.backtrace = []

    def path_logic(self, false_first_node_name, true_first_node_name, this_bool) :
        report = []
        if (this_bool == False) :
            for neighbor in self.smart_data.data[int(false_first_node_name)].neighbors :
                report = self.smart_data.is_triad(int(true_first_node_name), int(neighbor))
            print ("coming from  %s - seeking neighbor of %s " % (true_first_node_name, neighbor))

        else :
            for neighbor in self.smart_data.data[int(true_first_node_name)].neighbors :
                report = self.smart_data.is_triad(int(neighbor), int(false_first_node_name))
            print ("coming from  %s - seeking neighbor of %s " % (neighbor, false_first_node_name))
        return report

    def find_path(self, start_node, end_node) :
        formatted_data = []
        key_val = {}
        key_val_end = {}
        self.foretrace = []
        self.backtrace = []
        self.foretrace.append(end_node)
        self.backtrace.append(start_node)
        path_report = self.smart_data.is_triad(start_node, end_node)
        #while (len(self.foretrace) > 1 or len(self.backtrace) > 1) :
        #path_report = self.path_logic(self.foretrace[-1], self.backtrace[-1], self.from_home)
            #self.toggle_direction()
        if (path_report[2] == True) :
            if (len(self.foretrace) > 1 or len(self.backtrace) > 1) :
                key_val[path_report[1][0]] = path_report[1][1]
                formatted_data.append(key_val)
                self.toggle_direction()
            else :
                key_val[path_report[1][0]] = path_report[1][1]
                formatted_data.append(key_val)
                key_val_end[path_report[1][2]] = path_report[1][3]
                formatted_data.append(key_val_end)
                self.backtrace.pop()
                self.foretrace.pop()
                self.reset()
        else :
            if (not self.from_home) :
                self.foretrace.append(path_report[0])
                print "appending to foretrace: %s" % path_report[0]
            else :
                self.backtrace.append(path_report[0])
                print "appending to backtrace: %s" % path_report[0]
            self.toggle_direction()


        return formatted_data

    def toggle_direction(self) :
        self.from_home = not self.from_home

    def reset(self) :
        self.forward_backtrace = []
        self.homeward_backtrace = []
        self.from_home = False
