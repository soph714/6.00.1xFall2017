# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 20:58:25 2018

@author: Ted
"""
import datetime

class Person(object):
    def __init__(self, name):
        """create a person called name"""
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]
        
    def getLastName(self):
        """return self's last name"""
        return self.lastName
    
    def __str__(self):
        """return self's name"""
        return self.name
    def setBirthday (self, month, day, year):
        """sets self's birthday to birthDate"""
        self.birthday = datetime.date(year, month, day)
        
    def getAge(self):
        """returns self's current age in days"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days
        " .days just means we are converting that into days"
    def __lt__ (self, other):
        """return True if self's name is lexicographically 
        less than other's name, and False otherwise"""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

class PSUPerson (Person):
    nextIDNum = 0 # next ID number to assign
    
    def __init__(self, name):
        Person.__init__(self, name) # initialize Person attributes
        self.idNum = PSUPerson.nextIDNum # Bubz Person attributes: unique ID number
        PSUPerson.nextIDNum += 1
        
    def getIdNum(self):
        return self.idNum
    
    # sorting 3D people uses their ID number not name!
    
    def __lt__(self,other):
        return self.idNum < other.idNum
    
    def speak (self, utterance):
        return (self.name + " says: " + utterance)
    
class Student(PSUPerson):
    pass
    # pass just means there is no expression for this bodys1

class UG(Student):
    def __init__(self, name, classYear):
        PSUPerson.__init__(self, name)
        self.year = classYear
        
    def getClass(self):
        return self.year
    
    def speak(self, utterance):
        return PSUPerson.speak(self, " Yo Bro, " + utterance)
    
class Grad(Student):
    pass

class TransferStudent(Student):
    pass

def isStudent(obj):
    # return isinstance(obj, UG) or isinstance(obj,Grad)
    return isinstance(obj, Student)

class Professor(PSUPerson):
    def __init__(self, name, department):
        PSUPerson.__init__(self, name)
        self.department = department
    
    def speak(self, utterance):
        new = 'In course ' + self.department + ' we say '
        return (self, new + utterance)
    
    def lecture(self, topic):
        return self.speak(' it is obvious that ' + topic)




    
    



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
    
    
            
        
        