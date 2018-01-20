#same as imports.py but with less code
from imports_descmod import descs1
from imports_statmod import stats1

for i in range(0, len(stats1)):
    print("%d: %s" % (stats1[i], descs1[i]))
