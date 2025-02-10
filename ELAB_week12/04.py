def correct_filename(filename):
    forbidden_chars = ['\\', '/', '*', ':', '|', '"', '<', '>', ' ']

    if '.' in filename:
        name_part, extension_part = filename.rsplit('.', 1)
    else:
        name_part, extension_part = filename, ''

    corrected_name = ''
    for char in name_part:
        if char in forbidden_chars:
            corrected_name += '_'
        else:
            corrected_name += char

    corrected_extension = ''
    for char in extension_part:
        if char in forbidden_chars:
            corrected_extension += '_'
        else:
            corrected_extension += char

    corrected_name = corrected_name.replace('.', '_')

    corrected_name = corrected_name[:15]

    corrected_extension = corrected_extension[:3]

    if corrected_extension:
        return f"{corrected_name}.{corrected_extension}"
    else:
        return corrected_name

filename = input()

corrected_filename = correct_filename(filename)

print(corrected_filename)
