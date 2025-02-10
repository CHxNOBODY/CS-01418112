def calculate_score(elab_output, criteria):
    correct_answers = 0
    for char in elab_output[1:-1]:  # Remove the square brackets
        if char in criteria:
            correct_answers += 1
    total_answers = len(elab_output) - 2  # Remove the square brackets
    percentage = (correct_answers / total_answers) * 100
    return correct_answers, percentage

def main():
    elab_output = input()
    criteria = input()
    correct_answers, percentage = calculate_score(elab_output, criteria)
    print(f"{correct_answers}")
    print(f"{percentage:.2f}")

if __name__ == "__main__":
    main()