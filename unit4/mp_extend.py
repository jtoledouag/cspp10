# working with nicole
def extend(original, extension):
    for elememt in extension:
        original.append(elememt)

a = [24,23,13] 
b = [10,7,10]
extend(a,b)
print(a)
    