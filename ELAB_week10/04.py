def find_mode(l):
    modes = []
    max_count = 0
    for i in l:
        count = 0
        for j in l:
            if i == j:
                count += 1
        if count > max_count:
            max_count = count
            modes = [i]
        elif count == max_count:
            modes.append(i)
    modes.sort()
    return set(modes)

scores = []

for i in range(20):
    while True:
        score = int(input("Enter score: "))
        if score < 0 or score > 10:
            print("Score is out of range.")
            continue
        else:
            scores.append(score)
            break

print("-----")
print("Original list:")
print(scores)
print("Mode of scores:")
for mode in find_mode(scores):
    print(mode)
    break