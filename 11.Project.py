class Student:
    def __init__(self, firstname, lastname, tnumber):
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Grades = []

    def RunningAverage(self):
        scores = [float(g) for g in self.Grades if g != '']
        if scores:
            return sum(scores) / len(scores)
        return 0.0

    def TotalAverage(self):
        scores = [(float(g) if g != '' else 0.0) for g in self.Grades]
        if scores:
            return sum(scores) / len(scores)
        return 0.0

    def LetterGrade(self):
        avg = self.TotalAverage()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"


class StudentList:
    def __init__(self):
        self.Studentlist = []

    def add_student(self, firstname, lastname, tnumber):
        self.Studentlist.append(Student(firstname, lastname, tnumber))

    def find_student(self, tnumber):
        for i, student in enumerate(self.Studentlist):
            if student.TNumber == tnumber:
                return i
        return -1

    def print_student_list(self):
        print(f"{'First':>12} {'Last':>12} {'ID':>12} {'Running':>12} {'Semester':>12} {'Letter':>12}")
        print(f"{'Name':>12} {'Name':>12} {'Number':>12} {'Average':>12} {'Average':>12} {'Grade':>12}")

        print("-" * 78)
        for student in self.Studentlist:
            print(f"{student.FirstName:>12} {student.LastName:>12} {student.TNumber:>12} "
                  f"{student.RunningAverage():>12.2f} {student.TotalAverage():>12.2f} {student.LetterGrade():>12}")

    def add_student_from_file(self, filename):
        with open(filename, "r") as file:
            for line in file:
                firstname, lastname, tnumber = line.strip().split(",")
                self.add_student(firstname, lastname, tnumber)

    def add_scores_from_file(self, filename):
        with open(filename, "r") as file:
            for line in file:
                tnumber, score = line.strip().split(",")
                index = self.find_student(tnumber)
                if index != -1:
                    self.Studentlist[index].Grades.append(score)
                    

# Main Program
if __name__ == "__main__":
    sl = StudentList()
    sl.add_student_from_file("11.Project Students.txt")
    sl.add_scores_from_file("11.Project Scores.txt")
    sl.print_student_list()
