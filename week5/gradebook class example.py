# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 20:20:40 2018

@author: Ted
"""

class Grades(object):
    """
    Example class 2 from edX MITx 6.00.1x
    A mapping from sutdents to a list of grades
    """
    def __init__(self):
        """ Create empty grade book """
        # list of student objects
        self.students = []
        
        # maps idNum -> list of grades
        self.grades = {}
        
        # true if self.students is sorted
        self.isSorted = True
        
    def addStudent(self, student):
        """
        Assumes: student is of type Student
        Add student to the gradebook
        """
        if student in self.student:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.gedIdNum()] = []
        self.isSorted = False
        
    def addGrade (self, student, grade):
        """
        Assumes: grade is a float
        Add grade to the list of grades for student
        """
        
        try:
            self.grades[student.getIdNum()].append(grade)
        except KeyError:
            raise ValueError('Student not in grade book')
            
    def getGrades(self, student):
        """
        Return a list of grades for student
        """
        # return copy of student's grades
        try:
            return self.grades[student.getIdNum()][:] # [:] returns a copy
        except KeyError:
            raise ValueError('Student not in grade book')
    
    def allStudents(self):
        """
        Return a list of the students in the grade book
        """
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:] # return copy of list of students
    
    def gradeReport(course):
        """
        Assumes: course is of type grades
        """
        report = []
        for s in course.allStudents(): # loop over collection of all students
            tot = 0.0
            numGrades = 0
            for g in course.getGrades(s): # iterating computation over all student's grades
                tot += g
                numGrades += 1
            try:
                average = tot/numGrades
                report.append(str(s) + '\'s mean grade is ' + str(average))
            except ZeroDivisionError:
                report.append(str(s) + ' has no grades')
        return '\n'.join(report)
    
    
            
        
        