level = int(input("Enter level pokemon: "))
ball_level = input("Enter level pokeball: ").upper()
distance = int(input("Enter distance: "))

if level <=100 and level >= 61:
    if ball_level == "H":
        x = 0.01
    elif ball_level == "M":
        x = 0.08
    else:
        x = 0.1
elif level <=60 and level >= 41:
    if ball_level == "H":
        x = 0.01
    elif ball_level == "M":
        x = 0.05
    else :
        x = 0.03
else:
    if ball_level == "H":
        x = 0.01
    elif ball_level == "M":
        x = 0.03
    else:
        x = 0.05

persent = 100 - (level*distance*x)
if persent < 0:
    persent = 0

print(f"{persent:.2f} percent.")