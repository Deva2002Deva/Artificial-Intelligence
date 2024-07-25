% Facts: student(StudentName, SubjectCode), teacher(TeacherName, SubjectCode), subject(SubjectCode, SubjectName)
student(alice, cs101).
student(bob, cs101).
student(charlie, cs102).
student(david, cs103).
student(eve, cs103).

teacher(dr_smith, cs101).
teacher(dr_jones, cs102).
teacher(dr_brown, cs103).

subject(cs101, 'Computer Science 101').
subject(cs102, 'Computer Science 102').
subject(cs103, 'Computer Science 103').

% Query to find the subject a student is enrolled in
student_subject(StudentName, SubjectName) :-
    student(StudentName, SubjectCode),
    subject(SubjectCode, SubjectName).

% Query to find the teacher of a particular student
student_teacher(StudentName, TeacherName) :-
    student(StudentName, SubjectCode),
    teacher(TeacherName, SubjectCode).

% Query to find all students taught by a particular teacher
teacher_students(TeacherName, StudentName) :-
    teacher(TeacherName, SubjectCode),
    student(StudentName, SubjectCode).

% Utility to print all students, teachers, and subjects
print_db :-
    findall((Student, SubjectCode), student(Student, SubjectCode), Students),
    findall((Teacher, SubjectCode), teacher(Teacher, SubjectCode), Teachers),
    findall((SubjectCode, SubjectName), subject(SubjectCode, SubjectName), Subjects),
    write('Students: '), nl, print_list(Students),
    write('Teachers: '), nl, print_list(Teachers),
    write('Subjects: '), nl, print_list(Subjects).

% Helper predicate to print a list of tuples
print_list([]).
print_list([(A, B)|T]) :-
    write(A), write(' - '), write(B), nl,
    print_list(T).

% Example queries
start :-
    % Find the subject Alice is enrolled in
    student_subject(alice, Subject1),
    write('Alice is enrolled in: '), write(Subject1), nl,

    % Find the teacher of Bob
    student_teacher(bob, Teacher1),
    write('Bob\'s teacher is: '), write(Teacher1), nl,

    % Find all students taught by Dr. Brown
    write('Students taught by Dr. Brown: '), nl,
    teacher_students(dr_brown, Student1), write(Student1), nl, fail; true,

    % Print all entries in the database
    write('Database entries: '), nl,
    print_db.
