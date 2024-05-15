def ceil(x):
    return int(x) + int(x%1>0)

def floor(x):
    return int(x)

print("ceil")
print(ceil(3.4))
print(ceil(4.3))
print(ceil(4.5))
print(ceil(14.4))
print(ceil(324.1))
print(ceil(4))
print(ceil(5))

print("floor")
print(floor(3.4))
print(floor(4.3))
print(floor(4.5))
print(floor(14.4))
print(floor(324.1))
print(floor(4))
print(floor(5))