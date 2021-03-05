names = ("Moshe","Yossi","Elad","Moshe")
comps = ("Dell","Apple","MS","Dell")

#zip(names,comps)

#zipped = list(zip(names,comps))
#zipped = set(zip(names,comps))
#zipped = tuple(zip(names,comps))
#zipped = dict(zip(names,comps))

#print(zipped)

zipped =(zip(names,comps))

for (a,b) in zipped:
    print(a,b)
