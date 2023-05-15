from collections import OrderedDict, Counter

Counter('murcielago')
counter = Counter('murcielago')
d = {'platano':3, 'manzana':4, 'pera':1, 'naranja':2}
print(d)

keys = d.keys()
print(keys)

keys = sorted(keys)
print(keys)

for key in keys:
    print(key, d[key])

new_d = OrderedDict(sorted(d.items()))
print(new_d)

for key in new_d:
    print(key, new_d[key])
for key in reversed(new_d):
    print(key, new_d[key])