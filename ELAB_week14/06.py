def check_exam_eligibility():
    exercises = list(map(int, input().split()))
    total_exercises = sum(exercises)
    min_attendance, min_success = map(float, input().split())

    n = int(input())

    attendances = []
    for _ in range(n):
        attendances.append(list(map(int, input().split())))

    successes = []
    for _ in range(n):
        successes.append(list(map(int, input().split())))

    ineligible_students = []
    
    for i in range(n):
        
        total_attended = sum(attendances[i])
        total_classes = len(attendances[i])
        attendance_percent = (total_attended / total_classes) * 100

        total_completed = sum(successes[i])
        success_percent = (total_completed / total_exercises) * 100

        if attendance_percent < min_attendance and success_percent < min_success:
            ineligible_students.append(f"({i + 1}) {attendance_percent:.2f} {success_percent:.2f}")
        else:
            ineligible_students.append(f"{i + 1} {attendance_percent:.2f} {success_percent:.2f}")

    num_ineligible = sum(1 for student in ineligible_students if student.startswith('('))
    print(num_ineligible)
    for student in ineligible_students:
        print(student)

check_exam_eligibility()
