import cv2
import face_recognition
import os
#defining a list with students in them and then sorting
known_face_names = ["Mathew","Rohit","Akshat","Kevin","Parthiv","Jeeva"]
known_face_names = sorted(known_face_names)
#a dictionary whose keys are student names and the values their attendance
dic_student_list={"Name" : []}
for i in known_face_names:
    dic_student_list[i]=[]
# function that maps the recognized faces from the input images to the student list
def img_map():
    known_images = []
    names = set()
    known_rgb_images = []
    known_face_locations = []
    known_face_encodings = []
    rgb_location_pair = []
    new_images = []
    new_rgb_images = []
    new_face_locations = []
    new_rgb_location_pair = []
    new_face_encodings = []
    #
    files = os.listdir("path")#enter the path of your  file which has the name and img of all students(the file better be named student list)
    directories = os.listdir("path of extracted faces")#enter the path of the extracted faces
    #read all the valid image type files in the list of directories and append them to a list
    for img in files:
        if img[-3:]=='jpg':
            known_images.append(cv2.imread(f"path of student list/{img}"))
    #read the images extracted from the group photo and append them all to a list 
    for i in range(len(directories)):
        new_images.append(cv2.imread(f"path of extracted faces/{i+1}.jpg"))
        
    #convert the images to RGB and then get locations of faces in each image, to convert it to its encoding
    for i in known_images:
        known_rgb_images.append(cv2.cvtColor(i, cv2.COLOR_BGR2RGB))
    for i in known_rgb_images:
        known_face_locations.append(face_recognition.face_locations(i))
    for i in range(len(known_rgb_images)):
        rgb_location_pair.append((known_rgb_images[i],known_face_locations[i]))
    for i in rgb_location_pair:
        known_face_encodings.append(face_recognition.face_encodings(i[0],i[1])) 

    #the same process again but for the group photo/ new image we take during class
    for i in new_images:
        new_rgb_images.append(cv2.cvtColor(i, cv2.COLOR_BGR2RGB))
    for i in new_rgb_images:
        new_face_locations.append(face_recognition.face_locations(i))
    for i in range(len(new_rgb_images)):
        new_rgb_location_pair.append((new_rgb_images[i],new_face_locations[i]))
    for i in new_rgb_location_pair:
        new_face_encodings.append(face_recognition.face_encodings(i[0],i[1]))     
    
    
    # Iterate through each detected face (each encoding)
    for j in range(len(new_face_encodings)):
        # Compare with known face encodings
        for i in range(len(known_face_encodings)):
            for face_encoding in new_face_encodings[j]:
                matches = face_recognition.compare_faces(known_face_encodings[i], face_encoding)
                # Check if any match is found and add 
                if True in matches:
                    first_match_index = i
                    names.add(known_face_names[first_match_index])
    # adding attendance to the dictionary  
    for i in dic_student_list:
        if i!='Name':
            if i in names:
                dic_student_list[i]+=["Present"]
            else:
                dic_student_list[i]+=["Absent"]
