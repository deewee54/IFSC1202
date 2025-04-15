class Student:
    def __init__(self, firstname, lastname, tnumber, scores):
        self.FirstName = firstname.strip()
        self.LastName = lastname.strip()
        self.TNumber = tnumber.strip()
        self.Grades = [score.strip() for score in scores]

    def RunningAverage(self):
        valid_scores = [float(score) for score in self.Grades if score != '']
        if len(valid_scores) > 0:
            return sum(valid_scores) / len(valid_scores)
        return 0.0

    def TotalAverage(self):
        total_scores = [float(score) if score != '' else 0.0 for score in self.Grades]
        if len(total_scores) > 0:
            return sum(total_scores) / len(total_scores)
        return 0.0

    def LetterGrade(self):
        avg = self.TotalAverage()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'


def main():
    filename = '10.Project Student Scores.txt'
    students = []

    file = open(filename, 'r')
    lines = file.readlines()
    file.close()

    for line in lines:
        parts = line.strip().split(',')
        firstname = parts[0]
        lastname = parts[1]
        tnumber = parts[2]
        scores = parts[3:]
        student = Student(firstname, lastname, tnumber, scores)
        students.append(student)

    # Print header
    print(f"{'First':>12} {'Last':>12} {'ID':>12} {'Running':>12} {'Semester':>12} {'Letter':>12}")
    print(f"{'Name':>12} {'Name':>12} {'Number':>12} {'Average':>12} {'Average':>12} {'Grade':>12}")
    print('-' * 78)

    for student in students:
        print(f"{student.FirstName:>12} {student.LastName:>12} {student.TNumber:>12} "
              f"{student.RunningAverage():>12.2f} {student.TotalAverage():>12.2f} {student.LetterGrade():>12}")

if __name__ == "__main__":
    main()