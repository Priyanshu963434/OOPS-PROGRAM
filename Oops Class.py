# OOPs Object Oriented Programming
'''
#POP:- Procedure Oriented Programming
#Functional Programming
# class
# object
# Encapsulation
# Ineritance
# Polymorphism
# Abstraction
'''
# class is a keyword.
# class is virtual entity.
# class is a blue print of an object.
# object is a real world entity.


#class class_name:
#         class_properties

class mobile:
    color = 'blue'
    ram ='4GB'

#object
#object_name = class_name()
#object_name.class_property

mob1= mobile()
mob2= mobile()
mob3= mobile()

mob1.color= "Aqua"
mob2.ram="8GB"
print(mob1.ram)

class Demo:
    a= 100
    def myFun(self):
        print("I am in class demo and my name is mycrazy",self.a)

obj= Demo()
obj2= Demo()
obj2.a = 200

obj2.myFun()

# ENCAPSULATION
# this
# constructor
# constructor is a functionality of a method, A method will automatically when
# an object will be created.
class Emp:
    empid= ""
    empname= ""
    empsal= ""
    empcom= ""

    def setEmp(self,empid,empname,empsal,empcom):
        self.empid=empid
        self.empname= empname
        self.empsal= empsal
        self.empcom= empcom

    def displayEmp(self):
        print("Employee ID: ",self.empid)
        print("Employee Name: ",self.empname)
        print("Employee Salary: ",self.empsal)
        print("Employee Company Name: ",self.empcom)
emp1=Emp()
emp2=Emp()
emp1.setEmp(102,"Priyanshu sharma",23454,"Google")
emp1.displayEmp()
print("--------------------------------------------------")
emp2.setEmp(103,"Mukul",65432,"Google")
emp2.displayEmp()
print("-------------------------------------------------------")

# Data Shadowing
class Emp:
    empid= ""
    empname= ""
    empsal= ""
    empcom= ""

    def __init__(self):
        print("I am constructor")
        
         
    def __init__(self,empid,empname,empsal,empcom):
        self.empid=empid
        self.empname= empname
        self.empsal= empsal
        self.empcom= empcom

    def displayEmp(self):
        print("Employee ID: ",self.empid)
        print("Employee Name: ",self.empname)
        print("Employee Salary: ",self.empsal)
        print("Employee Company Name: ",self.empcom)

emp1=Emp(105,"Keshav",543,"Blinket")
emp1.displayEmp()

# Static method bcz they not use self.
class Demo:
    x = 100
    # Decorator
    @staticmethod
    def welcome():
        print("\nwelcome to my software")
obj=Demo()
obj.welcome()
# INHERITANCE [Single Inheritance | Multiple Inheritance | Multilevel Inheritance | Hierarchical Inheritance | Hybride Inheritance]
class A:
    def fun1(self):
        print("I am from class A and my name is fun1")
        
class B(A):
    def fun2(self):
        print("I am from class B and my name is fun2")

class C(A):
    def fun3(self):
        print("I am from class C and my name is fun3")

class D(B,C):
    def fun4(self):
        print("I am from class D and my name is fun4")

obj1= D()
obj1.fun1()
# POLYMORPHISM [POLY(MANY)+ MORPHISM(FORMS)]
# runtime(function overloading) function/method overriding
class A:
    def fun1(self):
        print("I am from class A ")
    def fun3(self):
         print("I am from class A ")
           
        
class B(A):
    def fun1(self):
        print("I am from class B")

obj= B()
obj.fun1()

# function overloading-:
def add(data1,data2):
    return data1+data2

print(add("PRIYANSHU","SHARMA"))

# ABSTRACTION
from abc import ABC, abstractmethod

class RBI(ABC):
    name=""
    def __init__(self,name):
        self.name= name
    @abstractmethod
    def getDocument(self):
        pass
    def welcome(self):
        print("Welcome to my bank ",self.name,"Regulated by RBI")
        
class SBI(RBI):
    def getDocument():
        pass
    def openAC(self):
        print("Account Open Successfully!")

obj= SBI("SBI")
obj.welcome()
















    
