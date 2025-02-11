distance = int(input())
fuel = int(input())

kaew = distance // (fuel * 0.5 * 15) + 1
kawn = distance // (fuel * 0.9 * 15) + 1

print(int(kaew))
print(int(kawn))