student(pooja, ravi).
student(rahul, priya).
student(anjali, kumar).
student(karthik, ravi).

teacher(ravi, cs101).
teacher(priya, cs102).
teacher(kumar, cs103).

student_details(Student, Teacher, SubCode) :-
    student(Student, Teacher),
    teacher(Teacher, SubCode).
