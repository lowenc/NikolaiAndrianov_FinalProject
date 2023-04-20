#Name: Nikolai Andrianov - Nathan Lowe, Hugo Bourinbayar, Payton Cook, Jimmy Zimmer
#email: lowenc@mail.uc.edu, bourinhh@mail.uc.edu, cookpk@mail.uc.edu, zimmejc@mail.uc.edu
#Assignment Title: Final Project
#Course: IS 4010
#Semester/Year: Spring 2023
#Brief Description: This project extracts data from a json and txt file and compares the two lists. 
#It also shows an image of our group at the location
#Citations: https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
# https://www.geeksforgeeks.org/python-removing-newline-character-from-string/
# https://bobbyhadz.com/blog/python-remove-newline-from-list
#Anything else that's relevant:

# functions.py
from PIL import Image
import json

#  This is the picture method
def pictureDisplay():
    image = Image.open("../grouppicture.jpg")
    image.show(title='Us at the former Lindner building')
    
#  This method extracts the JSON and puts it into a list called 'lineValues'
def jsonExtract():
    with open('../EncryptedGroupHints Spring 2023 Section 001.json') as f:
        data = json.load(f)
    lineValues = data['Nikolai Andrianov']
    return lineValues

#  This method utilizes the list that was created in jsonExtract method
def txtExtract():
    extractedNumbers = jsonExtract()
    extractedNumbers = [eval(i) for i in extractedNumbers]
#  This function reads the txt file and loads it into a list called 'lines'
    with open('../english.txt') as f:
        lines = f.readlines()
#  This portion of the code removes the new line '\n' part of the 'lines' list 
#  making a clean string to work with called 'new_list'
    new_list = [
    item.replace('\r', '').replace('\n', '')
    for item in lines]    
#  This part compares the two lists generated in jsonExtract and earlier in txtExtract
    slicedLines = [new_list[i-1] for i in extractedNumbers]
    print(slicedLines)