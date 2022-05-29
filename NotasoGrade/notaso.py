from cgitb import text
from enum import Enum
from multiprocessing.sharedctypes import Value
from turtle import title
from typing import List
from bs4 import BeautifulSoup
import requests
import smethods

def ListProfessors():
    smethods.clear()
    department = input("\n Please choose the university department:")
    department2 = ''

    #modifies input to place into url

    for i in range(len(department)):
        if(department[i] == ' '):
            department2 = department2 + '-'
        else:
            department2 = department2 + department[i]

    department2 = department2.lower()

    count = 1
    professorlist = set()
    professordict = {}
    url = f"https://notaso.com/universities/urpm/{department2}/"

    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")

    btag = doc.find_all("b")

    for i in btag:
        for text in i:
            professorlist.add(text)

    #printed set to not allow duplicate professors 

    for i in professorlist:
        professordict.update({i : count})
        print(str(count) + ") ", i)
        count += 1

    if len(professorlist) < 1:
        print("That is an invalid department \n")
        restart = input("Would you like to go back to the menu?: ")
        restart = restart.lower()
        if restart == "yes":
            Menu()
        else:
            print("\n Thank you for trying out my notaso program! Have a great day :) \n ")
        
    
    
    picknum = int(input("\n Please choose the number of the professor to show the grade of: "))

    if picknum > len(professordict.items()):
        print("\n That number currently exceeds the number of professors \n")
        restart = input("Would you like to go back to the menu?: ")
        restart = restart.lower()
        if restart == "yes":
            Menu()
        else:
            print("\n Thank you for trying out my notaso program! Have a great day :) \n ")

    for key,value in professordict.items():
        if picknum == value:
            professorinput = key
            FindGradePercentage(professorinput)

#function that finds a specific professors grade percentage.

def FindGradePercentage(professorinput):

    try:
        professorinput2 = ''

        for i in range(len(professorinput)):
            if(professorinput[i] == ' '):
                professorinput2 = professorinput2 + '-'
            else:
                professorinput2 = professorinput2 + professorinput[i]

        professorinput2 = professorinput2.lower()

        proflink = f"https://notaso.com/professors/{professorinput2}/"

        profresult = requests.get(proflink)

        profdoc = BeautifulSoup(profresult.text,"html.parser")
        percent = profdoc.find('p', attrs={"class" : "professor-percent"})
        smethods.clear()
        grade = smethods.determineLetterGrade(percent.text)
        print("//////////////////////////////////////////////////\n")
        print(f"   {professorinput}'s grade is:",grade,"-", percent.text)
        print("///////////////////////////////////////////////// \n")
        restart = input("Would you like to go back to the menu?: ")
        restart = restart.lower()
        if restart == "yes":
            Menu()
        else:
            print("\n Thank you for trying out my notaso program! Have a great day :) \n ")

    except AttributeError:
        clear()
        print("That Professors name is incorrect, please try again")
        Menu()

#Main function

def Menu():
    smethods.clear()
    print("//////////////////////////////////////////////////////////////////////////////////////")
    print("//////////////////////////////////////////////////////////////////////////////////////")
    print("\n        Welcome to my Notaso Webscraping Program, please choose an option below: \n ")
    print("//////////////////////////////////////////////////////////////////////////////////////")
    print("////////////////////////////////////////////////////////////////////////////////////// \n")
    print("\n 1) List of Professors of a desired Department.\n ")

    try:
        option = (int(input("Please choose a number: ")))

        if(option == 1):
            ListProfessors()
        else:
            print("Incorrect option, please try again")
            Menu()
    except ValueError:
        Menu()

Menu()
