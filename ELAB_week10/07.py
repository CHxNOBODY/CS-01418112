total_practice = int(input())
percent = float(input())
num_students = int(input())

student_scores = []
for _ in range(num_students):
    student_scores.append(int(input()))

percentages = [score / total_practice * 100 for score in student_scores]

ineligible_students = [i + 1 for i, percentage in enumerate(percentages) if percentage < percent]

print(len(ineligible_students))

for i, (student, percentage) in enumerate(zip(range(1, num_students + 1), percentages)):
    if i + 1 in ineligible_students:
        print(f"({student}) {percentage:.2f}")
    else:
        print(f"{student} {percentage:.2f}")