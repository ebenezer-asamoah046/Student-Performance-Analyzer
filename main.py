


def main():
    print("=" * 35)
    print("STUDENT PERFORMANCE ANALYZER")
    print("=" * 35)

    def get_student_name():
        return input("Enter name: ")

    name = get_student_name()

    def get_score():
        subject_list = []
        score_list = []

        number_of_subject = int(input("\nEnter number of subjects: "))

        for i in range(number_of_subject):
            student_subject = input(f"Enter subject {i+1} name: ")

            while True:
                score = int(input("Enter score: "))

                if score < 0 or score > 100:
                    print("Enter valid score between 0 and 100.")
                else:
                    break

            subject_list.append(student_subject)
            score_list.append(score)
        return subject_list, score_list
    subject, scores = get_score()


    def calculate_average(score_list):
        total_score = 0
        for score in score_list:
            total_score += score

        average = total_score / len(score_list)

        return average
    average_result = calculate_average(scores)

    def determine_grade(average):
        if 80 <= average <= 100:
            return f"Grade: A"
        elif 70 <= average <= 79:
            return f"Grade: B"
        elif 60 <= average <= 69:
            return f"Grade: C"
        elif 50 <= average <= 59:
            return f"Grade: D"
        else:
            return f"Grade: F"

    grade_result = determine_grade(average_result)


    def determine_status(average):
        if average > 50:
            return f"PASS"
        else:
            return f"FAIL"

    status_result = determine_status(average_result)

    print()

    def performance_remark(average):
        if 80 <= average <= 100:
            return f"Outstanding performance"
        elif 70 <= average <= 79:
            return f"Excellent performance"
        elif 60 <= average <= 69:
            return f"Very good performance"
        elif 50 <= average <= 59:
            return f"Good performance"
        else:
            return f"Poor performance"

    result_performance_remark = performance_remark(average_result)


    def display_report(student_name, student_subject, student_score, average_score, grade, status, remark):
        print("=" * 35)
        print("PERFORMANCE REPORT")
        print("=" * 35)



        print(f"\nStudent: {student_name}")
        print()

        for i in range(len(student_subject)):
            print(f"{student_subject[i]}: {student_score[i]}")

        print(f"\nAverage: {average_score:.2f}")
        print(f"Grade: {grade}")
        print(f"Status: {status}")
        print(f"Remark: {remark}")

        print()
        print("=" * 35)


    display_report(name, subject, scores, average_result, grade_result, status_result, result_performance_remark)

main()