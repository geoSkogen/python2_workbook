import imports_statmod
import imports_descmod

for i in range(0, len(imports_descmod.descs1)):
    desc = imports_descmod.descs1[i]
    stat = imports_statmod.stats1[i]
    print("%d: %s" % (stat, desc))
