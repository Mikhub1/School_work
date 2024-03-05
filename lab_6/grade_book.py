class GradeBook:
    TERM_MARK_WT = 0.55
    FINAL_EXAM_WT = 0.45

    noOfStudents = 0

    def __init__(self, name="n/a", num=0, termMark=0, finalExamMark=0):
        GradeBook.noOfStudents += 1
        self.__stName = name
        self.__stNum = num
        self.__tMark = termMark
        self.__fExMark = finalExamMark
        self.__finalGrade = 0
        self.calcFinalGrade()

    def setFinalExamMark(self, marks):
        self.__fExMark  = marks
        self.calcFinalGrade()
        
    def getClassSize():
        return GradeBook.noOfStudents
    
    def calcFinalGrade(self):
        self.__finalGrade = self.__tMark * GradeBook.TERM_MARK_WT + self.__fExMark * GradeBook.FINAL_EXAM_WT
    
    def getInfo(self):
        return "Student Name: " + self.__stName + "\nStudent Name: " + str(self.__stNum) + "\nFinal Grade: " + str(self.__finalGrade) + "\n"

def main():
    st1 = GradeBook("Peter Pan",200963453, 85, 90)
    st2 = GradeBook("Penny Henny",200578463, 75, 90)
    st3 = GradeBook("Lenny Menny",201041346, 72, 65)
    st4 = GradeBook("Adam Padam",201071286, 80, 85)

    print(st1.getInfo())
    print(st2.getInfo())
    st2.setFinalExamMark(100)
    print(st2.getInfo())
    print(st3.getInfo())
    print(st4.getInfo())
    print("The number of students in class are:", GradeBook.getClassSize())

main()

