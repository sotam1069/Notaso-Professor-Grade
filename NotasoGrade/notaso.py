from enum import Enum
from turtle import title
from bs4 import BeautifulSoup
import requests

def FindGrade():

    url = "https://notaso.com/universities/urpm/ciencias-de-computadora/"

    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")

    l1 = []

    btag = doc.find_all("b")
    for i in btag:
        for text in i:
            text.split()

            names = {text : 0}
            l1.append(names)

    try:

        professorinput = input("Which Computer Science Professor would you like to know the grade of?: ")

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

        print(f"{professorinput}'s grade is: ", percent.text)

    except AttributeError:
        print("That Professors name is incorrect, please try again")
        FindGrade()


FindGrade()




