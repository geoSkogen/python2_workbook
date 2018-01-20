#tried three methods for getting a ratio from this
#converting user input to integer to float. rounds down to 0 all the time

def jan_michaels(jans,quads):
    jans = jans + 0.0
    ratio = jans/quads
    print("In a world where there are only %d Jan-Michael Vincents--" % jans)
    print("and %d quadrants . . ." % quads)
    print("""there's only enough time for %d of a Jan-Michael to be in any
           quadrant.  He can't be in 2 quadrants at once.""" % ratio)

jan_in = input("# of Jan-Michaels: ")
quad_in = input("# of quadrants: ")
j_int = int(jan_in)
q_int = int(quad_in)

jan_michaels(j_int,q_int)
