from streamlit import *
from maps_img_to_face import *
from rec_fac_in_inputimg import *
from io import BytesIO
from PIL import Image
import cv2,numpy as np

title("Attendance")
date = date_input("Enter the date")
edit_attandance = text_input("Enter the name of one student you want to change the attendance of(IF there are multiple names seperate the names by a comma and space(eg Name1, Name2)")
#a function to that lets the user take in an input image from which the face recogntition and maooing would happen
def fun():
    img = file_uploader("To take attendance upload the image here")
    if not img == None:
        dic_student_list['Name'] += [date]
        image_bytes = BytesIO(img.read())
        pil_image = Image.open(image_bytes)
        opencv_image = cv2.cvtColor(np.array(pil_image),cv2.COLOR_RGB2BGR)
        extract_faces(opencv_image)
#the function will be called only when both the date and edit_attendance are non empty 
if date != '' and edit_attandance == '':
    fun()
#splitting the input names by a comma into a list which will used to edit attendan
edit_names_list=edit_attandance.split(', ')
#to show attendance sheet at all times
if edit_attandance == '':
    subheader("Attendance sheet")
    t1, t2 = columns([1,3])
    t1.table(dict.keys(dic_student_list))
    t2.table(dict.values(dic_student_list))
    #finds the students name in the dictionary, alters the attendance and shows the attendance table
elif edit_attandance != '':
    for name in edit_names_list:
        attandance = dic_student_list[name]
        n = len(attandance)
        if date in dic_student_list['Name']:
            i = dic_student_list['Name'].index(date)
            if attandance[i] == 'Present':
                attandance[i] = 'Absent'
            elif attandance[i] == 'Absent':
                attandance[i] = 'Present'
        else:
            write("You have not taken attedance on that day")
    subheader("Attendance sheet")
    t1, t2 = columns([1,3])
    t1.table(dict.keys(dic_student_list))
    t2.table(dict.values(dic_student_list))
    Abesnties = []
    for key in dict.keys(dic_student_list):
        if key != 'Name':
            if dic_student_list[key][n-1] == 'Absent':
                Abesnties += [key]
    write("List of absenties")
    write(Abesnties)
