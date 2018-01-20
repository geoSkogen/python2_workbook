def print_info(arg1, *vartuple):
    print(arg1)
    for i in vartuple:
        print(i)
    return;

print_info("Suki plays with Theo")
print_info("Sasha plays with Britt", "Adolf builds the bonfire", "And Rico plays with it.")
