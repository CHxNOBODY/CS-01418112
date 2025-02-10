def print_pyramid(levels):
    for i in range(1, levels + 1): 
        spaces = ' ' * (levels - i) 
        stars = '*' * (2 * i - 1) 
        print(f"|{spaces}{stars}{spaces}|")

levels = int(input())
print_pyramid(levels)
