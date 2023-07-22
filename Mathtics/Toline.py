k = 1
point = [(1, 2), (2, 5), (5, 7), (10, 15)]
def toNient(pio, formulaK):
    result = 0
    for i in pio:
        result += (i[1]-formulaK * i[0])
    return result
for i in range(100):
    k += toNient(point, k) * 0.1
print(k)