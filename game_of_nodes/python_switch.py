def init_funcs(int_arg,switch_index) :
    return_val = ""
    dec = []

    def english(int_in) :
        dec = ["zero","one","two","three","four","five","six","seven","eight","nine"]
        return dec[int_in]

    def spanish(int_in) :
        dec = ["cero","uno","dos","tres","cuatro","cinco","seis","siete","ocho","nueve"]
        return dec[int_in]

    switch = [english,spanish]
    #another way of doing it
    #switch = {0: english, 1: spanish}

    if (int_arg < 0 and int_arg > 9) :
        return_val = "decimal argument is out of range"
    elif (switch_index >= len(switch) - 1) :
        return_val = "switch index argument is out of range"
    else :
        return_val = switch[switch_index](int_arg)

    return return_val

result = init_funcs(1,0)
print result
