class Pathfinder() :
    def __init__(self) :
        self.from_home = False
        self.forward_backtrace = []
        self.homeward_backtrace = []

    def find_path(self, smart_data, start_node, end_node) :
        self.forward_backtrace.append(end_node)
        self.homeward_backtrace.append(start_node)
        path_report = smart_data.is_triad(start_node, end_node)
        return path_report

    def toggle_direction(self) :
        self.from_home = not self.from_home
