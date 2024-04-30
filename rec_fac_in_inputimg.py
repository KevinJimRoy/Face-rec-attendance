import cv2
import os
import maps_img_to_face
def extract_faces(image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Load the pre-trained face detector
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Iterate over each detected face
    for i, (x, y, w, h) in enumerate(faces):
        # Extract the face region from the image
        face = image[y:y+h, x:x+w]

        #naming all faces
        name = f"{i+1}"
        
        # Ensure the output directory exists
        if not os.path.exists("extracted_faces"):
            os.makedirs("extracted_faces")
        # Write the face image to a file with the provided name
        output_path = os.path.join("extracted_faces", f"{name}.jpg")
        cv2.imwrite(output_path, face)
    #calling a function that helps map the faces detected in the above programme with students in our student list
    maps_img_to_face.img_map()