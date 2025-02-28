from collections import namedtuple
# Named tuples are especially useful for assigning field names to result tuples 
# returned by the csv or sqlite3 modules i.e. any type of tabular form data 
# like in this problem it is a spreadsheet
if __name__=="__main__":
    total_students=int(input())
    column_names=input() # column names in any order
    Student=namedtuple("Student",column_names) # named tuple of type student
    total_marks=0
    for _ in range(1,total_students+1):
        student_details=input().split() # creates list with student details
        student= Student(*student_details) # values are under their respective column names. 
        # Pass the list as a tuple as we can pass a tuple only to a namedtuple object 
        # and create a namedtuple instance
        total_marks=total_marks+int(student.MARKS)
    average_marks=total_marks/total_students
    print(average_marks)
    