block_length = 12
block_width = 9
house_length = 7
house_width = 6

MOW_RATE = 35.0

sum1 = block_length * block_width
sum2 = house_length * house_width

area = sum1 - sum2

mow = MOW_RATE * area

print("Mowing cost is" ,mow, "baht.")