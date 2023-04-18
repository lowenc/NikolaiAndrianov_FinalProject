#Name: Nikolai Andrianov - Nathan Lowe, Hugo Bourinbayar, Payton Cook, Jimmy Zimmer
#email: lowenc@mail.uc.edu, bourinhh@mail.uc.edu, cookpk@mail.uc.edu, zimmejc@mail.uc.edu
#Assignment Title: Final Project
#Course: IS 4010
#Semester/Year: Spring 2023
#Brief Description: 
#Citations: 
#Anything else that's relevant:

# picture.py
from PIL import *
import json
import requests
def pictureDisplay():
    image = Image.open("grouppicture.jpg")
    image.show(title='Us at the former Lindner building')
    #This is the picture function
def jsonExtract():
    response = requests.get('EncryptedGroupHints Spring 2023 Section 001.json')
    json_string = response.content
    parsed_json = json.loads(json_string)
    print(parsed_json)