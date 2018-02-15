class Oil_Boil :

    count = 0
    mode = "f"

    def __init__(self, time, temp, control) :
        self.time_str = time
        self.temp = temp;
        self.control = control
        self.serial = hex(Oil_Boil.count)
        self.mode = Oil_Boil.mode
        #self.time_arr = self.to_time_array(self.time_str)
        Oil_Boil.count += 1

    def dump_data(self) :
        print ("\r\nno: %s\r\ntime: %s\r\ntemp: %i %s\r\ncontrol: %s\r\n" % (self.serial, self.time_str, self.temp, self.mode, self.control))

    def rescale(self, str_arg) :
        import temps
        if (str_arg == "f") :
            if (self.mode == "f") :
                return
            elif (self.mode == "c") :
                self.temp = temps.c_to_f(self.temp)
                self.mode = "f"
            elif (self.mode == "k") :
                self.temp = temps.k_to_f(self.temp)
                self.mode = "f"
        elif (str_arg == "c") :
            if (self.mode == "f") :
                self.temp = temps.f_to_c(self.temp)
                self.mode = "c"
            elif (self.mode == "c") :
                return
            elif (self.mode == "k") :
                self.temp = temps.k_to_c(self.temp)
                self.mode = "c"
        elif (str_arg == "k") :
            if (self.mode == "f") :
                self.temp = temps.f_to_k(self.temp)
                self.mode = "k"
            elif (self.mode == "c") :
                self.temp = temos.c_to_k(self.temp)
                self.mode ="k"
            elif (self.mode == "k") :
                return
        else :
            return
