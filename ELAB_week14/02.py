def cloth_size(width_list):
    result = {'S': 0, 'M': 0, 'L': 0}
    for width in width_list:
        if width <= 36:
            result['S'] += 1
        elif width > 44:
            result['L'] += 1
        else:
            result['M'] += 1
    return result
