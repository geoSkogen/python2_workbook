import Oil_Boil
import random

boils = []
alphabet = "fck"
controls = ["total","no","randomized","chaotic","turbulent","approximate","contained","relinquished"]
for i in range(32) :
    lmin = random.randint(1,5)
    rmin = random.randint(1,9)
    lsec = random.randint(1,5)
    rsec = random.randint(1,9)
    temp = float(random.randint(212, 2120))
    control_index = random.randint(0,len(controls)-1)
    controlstr = controls[control_index]
    timestr = str(lmin) + str(rmin) + ":" + str(lsec) + str(rsec)
    #tempstr = str(temp)
    this_boil = Oil_Boil.Oil_Boil(timestr,temp,controlstr)
    boils.append(this_boil)
    #print ("\r\nboiling for %s at %s at %s control" % (timestr,tempstr,controlstr))

for boil in boils :
    alph_index = random.randint(0,len(alphabet)-1)
    str_arg = alphabet[alph_index]
    boil.rescale(str_arg)
    boil.dump_data()
