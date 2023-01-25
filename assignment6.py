# -*- coding: utf-8 -*-
"""Assignment6.ipynb

#Assignment1
import json
class Employee:
    def __init__(self):
        self.emp_dic={}
    def creat_JSON(self):
        for i in range(5):
            name = input("Enter your name: ")
            dob = input('Enter your DOB: ')
            height = input('Enter your height: ')
            city = input('Enter your city: ')
            state = input('Enter your state: ')
            emp={'name':name,'dob':dob,'height':height,'city':city,'state':state}
            emp_id = len(self.emp_dic)+1
            self.emp_dic[emp_id]=emp
        with open("employee.json",'w') as f:
            json.dump(self.emp_dic,f)

    def data_print(self):
        with open("employee.json","r") as f:
            data = json.load(f)
        for i in data.values():
            l1 = []
            l1.append(i)
            print(l1)   

x =Employee()            
x.creat_JSON()
print("****************************************************************")
x.data_print()

import json
class State_Capital:
    def __init__(self):
        self.st_cap={}
    def creat_JSON(self):
        for i in range(7):
            s_name = input("Enter State Name: ")
            c_name = input("Enter Capital Name: ")
            print("-------------------")
            SC_dict={s_name:c_name}
            self.st_cap.update(SC_dict)
        with open("State_Capital.json",'w') as f:
            json.dump(self.st_cap,f)

    def print_JSON(self):
        with open("State_Capital.json",'r') as f:  
            data = json.load(f)
        for i,j in data.items():
            print('State: '+ i + '  Capital: '+ j)    


x = State_Capital()
x.creat_JSON()
x.print_JSON()

#Assignment 2
class Dog:
    def __init__(self,name,age,coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color
    def description(self):
        print('Dog name is: ',self.name)
        print('Age of ',self.name,' is: ', self.age)    
    def get_info(self):
        print('Coat color of ',self.name,' is: ',self.coat_color)

class JackRussellTerrier(Dog):
    def health(self):
        print('The breed has a reputation for being healthy.')
        print('Jack Russells can live from 13 to 16 years.')
    def Crossbreeds(self):
        print('Crossbreed of a Jack Russell terrier and a Beagle is called a Jackabee.')    
class Bulldog(Dog):
    def health(self):
        print('The average life span of the breed as 8 to 10 years.')
        print('Allergies and hip issues in older Bulldogs')
    def Appearance(self):
        print('Thick folds of skin on the brow, round, black, wide set eyes.')
        print('A rope or nose roll above the nose.')

dog = Bulldog('Jeff',5,'Black')
dog.description()
dog.get_info()        
dog.health()
dog.Appearance()

dog1 = JackRussellTerrier('Maddy',4,'Brown & White')
dog1.description()
dog1.get_info()
dog1.health()
dog1.Crossbreeds()
