def jam (bottom, top) :
    summary_report = []
    counter = top - bottom
    if (counter % 2 != 0) :
        top += 1
        counter = top - bottom
    flip_mode = False
    while (counter > 0 or counter < 0) :
        report = exponentiate(bottom, top)
        summary_report.append(report)
        if (flip_mode) :
            top = bottom + 1
            bottom = top - 1
            flip_mode = True
        else :
            top =  top - 1
            bottom = bottom + 1
            flip_mode = False
        print_pretty(report)
        counter = top - bottom

    return summary_report

def print_pretty (a_list) :
    counter = 0
    for member in a_list :
        print ("\r\n\t[%i]" % counter)
        counter += 1
        for item in member :
            print ("\t\t%i" % item)
    #return False

def exponentiate (int1, int2) :
    results = []
    int1_scores = []
    int2_scores = []
    reps = int2 - int1

    for i in range(reps) :
        int1_scores.append(int1**i+1)
        int2_scores.append(int2**i+1)

    results.append(int1_scores)
    results.append(int2_scores)

    return results

data = jam(2,56)
print_pretty(data)
