def f_to_c(num_arg) :
    result = (float(num_arg) - 32) * (5.0/9.0)
    return result

def c_to_f(num_arg) :
    result = (float(num_arg) * (9.0/5.0) + 32)
    return result

def c_to_k(num_arg) :
    result = float(num_arg) + 273.15
    return result

def k_to_c(num_arg) :
    result = float(num_arg) - 273.15
    return result

def f_to_k(num_arg) :
    store_num = f_to_c(num_arg)
    result = c_to_k(store_num)
    return result

def k_to_f(num_arg) :
    store_num = k_to_c(num_arg)
    result = c_to_k(store_num)
    return result
