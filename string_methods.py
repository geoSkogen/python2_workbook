filenames = ["boiledinoil.boil", "cometotheoilboil.boil", "hello.bernarnd",
             "POP43kgtqoq.oil","POP4weq4gqebqq4q3.oil","POP34q4gqwbriewvdf.oil"]
dumpstring = """PO#.boil.oil \nPOPfewqeqqv.oil \nPOP434gb4vnre.oil \nPOPfef34fw34.dll \nPORP32f4qver.oil"""
newfiles = dumpstring.split( )
exts = (".boil", ".oil", ".oilyboilo", ".bernard", ".blurm")
formats = ("POP","PORP")
validfiles = []
for filename in filenames :
    if (filename.endswith(exts) and filename.startswith(formats)) :
        validfiles.append(filename)
for newfile in newfiles :
    if (newfile.endswith(exts) and newfile.startswith(formats)) :
        validfiles.append(newfile)
print validfiles
