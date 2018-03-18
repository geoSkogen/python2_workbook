class Pathfinder() :
    def __init__(self, smart_data) :
        self.from_home = False
        self.smart_data = smart_data
        self.foretrace = []
        self.backtrace = []

    def assemble_path(self, last_report) :
        key_val = {}
        key_val_end = {}
        data = []
        key_val[last_report[1][0]] = last_report[1][1]
        data.append(key_val)
        key_val_end[last_report[1][2]] = last_report[1][3]
        data.append(key_val_end)
        return data

    def path_logic(self, failed_node, static_node, this_bool) :
        report = []

        for neighbor in failed_node.neighbors :
            if (self.from_home) :
                report = self.smart_data.is_triad(neighbor, static_node)
            else :
                report = self.smart_data.is_triad(static_node, neighbor)
            if (report[2] == True) :
                self.assemble_path(report)
                break
        return report

    def find_path(self, start_node, end_node) :
        formatted_data = []
        self.path = []
        self.foretrace = []
        self.backtrace = []
        self.foretrace.append(end_node)
        self.backtrace.append(start_node)
        path_report = self.smart_data.is_triad(start_node, end_node)
        if (path_report[2] == True) :
            formatted_data = self.assemble_path(path_report)
            if (len(self.foretrace) > 1 and len(self.backtrace) > 1) :
                []
            else :
                self.foretrace.pop()
                self.backtrace.pop()
                self.reset()
        else :
            []
        
            '''
            if (self.from_home) :
                path_logic(nodes.data[start_node], nodes.data[end_node])
            else :
                path_logic(end_node, start_node)
            '''
        print path_report
        return formatted_data

    def toggle_direction(self) :
        self.from_home = not self.from_home

    def reset(self) :
        self.foretrace = []
        self.backtrace = []
        self.from_home = False
