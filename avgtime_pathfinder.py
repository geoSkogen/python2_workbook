class Pathfinder() :
    def __init__(self) :
        self.from_home = False
        self.foretrace = []
        self.backtrace = []
        self.key_val = {}
        self.formatted_data = []

    def find_path(self, smart_data, start_node, end_node) :

        def path_logic(data_obj, false_first_node, true_first_node, this_bool) :
            report = []
            if (not this_bool) :
                for neighbor in false_first_node.neighbors :
                    report = data_obj.is_triad(int(true_first_node.name), neighbor)
                print ("coming from  %s - seeking neighbor of %s " % (true_first_node.name, neighbor))
            else :
                for neighbor in true_first_node.neighbors :
                    report = data_obj.is_triad(neighbor, int(false_first_node.name))
                print ("coming from  %s - seeking neighbor of %s " % (neighbor, false_first_node.name)
           return report

        self.formatted_data = []
        self.foretrace.append(end_node)
        self.backtrace.append(start_node)
        path_report = smart_data.is_triad(start_node, end_node)
        while (len(self.foretrace) > 1 or len(self.backtrace) > 1)) :
            path_report = path_logic(smart_data, smart_data.data[int(self.foretrace[len(self.foretrace)-1])], smart_data.data[int(self.backtrace[len(self.backtrace)])],self.from_home)
            self.toggle_direction()
            if (path_report[2] == True) :
                if (len(self.foretrace) > 1 or len(self.backtrace) > 1))
                    key_val[path_report[1][0]] = path_report[1][1]
                    self.formatted_data.append(key_val)
                    if (not self.from_home) :
                        self.foretrace.append(path_report[0])
                    else :
                        self.backtrace.append(path_report[0])
                    self.toggle_direction()
                else :
                    self.key_val[path_report[1][0]] = path_report[1][1]
                    self.formatted_data.append(key_val)
                    self.key_val[path_report[1][2]] = path_report[1][3]
                    self.formatted_data.append(key_val)
                    self.backtrace.pop()
                    self.foretrace.pop()
                    self.reset()
        return self.formatted_data

    def toggle_direction(self) :
        self.from_home = not self.from_home

    def reset(self) :
        self.forward_backtrace = []
        self.homeward_backtrace = []
        self.from_home = False
