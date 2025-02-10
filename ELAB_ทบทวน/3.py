def find_note_in_scale(scale, N):
    notes = scale.split(',')
    note_index = (N - 1) % len(notes)
    return notes[note_index]

scale_input = input().strip()
N_input = int(input().strip())

result_note = find_note_in_scale(scale_input, N_input)
print(result_note)