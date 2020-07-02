#Thanks Kim for helping with the algo, https://github.com/kimli42

def gradingStudents(grades):
    grade_list = []
    for grade in grades:
        if grade < 38:
            grade_list.append(grade)
        else:
            next_multiple_5 = grade + (5 - grade % 5)
            if next_multiple_5 - grade < 3:
                grade = next_multiple_5
            grade_list.append(grade)
    return grade_list
