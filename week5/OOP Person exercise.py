# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 20:53:11 2018

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




    
    