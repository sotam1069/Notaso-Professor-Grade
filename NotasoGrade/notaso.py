from enum import Enum
from multiprocessing.sharedctypes import Value
import os
from turtle import title
from typing import List
from bs4 import BeautifulSoup
import requests

#function that wipes console for better readability

def clear():
     os.system('cls' if os.name=='nt' else 'clear')
     return("   ")

#function that takes care of finding the list of professors in a specific department

def ListProfessors():

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
    url = f"https://notaso.com/universities/urpm/{department2}/"

    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")

    btag = doc.find_all("b")

    for i in btag:
        for text in i:
            professorlist.add(text)

    #printed set to not allow duplicate professors 

    for i in professorlist:
        print(str(count) + ") ", i)
        count += 1
    
    restart = input("Would you like to go back to the menu?: ")
    restart = restart.lower()
    if restart == "yes":
        Menu()
    else:
        print("\n Thank you for trying out my notaso program! Have a great day :) \n ") 

#function that finds a specific professors grade percentage.

def FindGrade():

    try:
        professorinput = input("\n Which Professor would you like to know the grade of?: ")

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
        clear()
        print("//////////////////////////////////////////////////\n")
        print(f"{professorinput}'s grade is: ", percent.text)
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
        FindGrade()

#Main function

def Menu():
    clear()
    print("\n Welcome to a simple Notaso Webscraping Program, please choose an option below \n ")
    print("1) List of Professors of a desired Department.")
    print("2) Find The grade percentage of your desired professor")

    try:

        option = (int(input("Please choose a number: ")))

        if(option == 1):
            ListProfessors()
        if (option == 2):
            FindGrade()
    except ValueError:
        print("Incorrect option, please try again")
        Menu()

Menu()
