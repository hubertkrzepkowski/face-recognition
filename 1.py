import face_recognition
<<<<<<< HEAD
import os, sys
import cv2
import numpy as np
from tinydb import TinyDB, Query
import tkinter.scrolledtext as tkscrolled
from tkinter import *
root = Tk()

nazwisko = ''
recognized_Faces = set([])


def Photo():
    cap = cv2.VideoCapture(0)
    print(os.listdir('.//zdjecia'))
    while (True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == 13:
            cv2.imwrite(".//zdjecia/"+entry.get()+entry1.get()+".jpg", frame)
            entry.delete(0, END)
            entry1.delete(0,END)
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

def fr():

        known_face_encodings = []
        known_face_names = []

        video_capture = cv2.VideoCapture(0)
        zdjecia =os.listdir('.//zdjecia')
        print(zdjecia)

        for zdjecie in zdjecia:
            image = face_recognition.load_image_file('.//zdjecia/'+zdjecie)
            known_face_encodings.append(face_recognition.face_encodings(image)[0])
            known_face_names.append(zdjecie[:-4])



        # Initialize some variables
        face_locations = []
        face_encodings = []
        face_names = []
        process_this_frame = True

        while True:
            # Grab a single frame of video
            ret, frame = video_capture.read()

            # Resize frame of video to 1/4 size for faster face recognition processing
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_small_frame = small_frame[:, :, ::-1]

            # Only process every other frame of video to save time
            if process_this_frame:
                # Find all the faces and face encodings in the current frame of video
                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

                face_names = []
                for face_encoding in face_encodings:
                    # See if the face is a match for the known face(s)
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                    name = "???"

                    # If a match was found in known_face_encodings, just use the first one.
                    if True in matches:
                        first_match_index = matches.index(True)
                        name = known_face_names[first_match_index]
                      #  recognized_Faces.add(name)
                    face_names.append(name)

            process_this_frame = not process_this_frame

            # Display the results
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                # Draw a box around the face
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                # Draw a label with a name below the face
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

            # Display the resulting image
                cv2.imshow('Video', frame)

            if cv2.waitKey(1) & 0xFF == 13:
                for face in recognized_Faces:
                    T.insert(END, face)
                    T.insert(END, "\n")

                T.config(state=DISABLED)
                video_capture.release()
                cv2.destroyAllWindows()
                break



large_font = ('Verdana',15)



entry = Entry(root, font=large_font)
entry.insert(0, 'Imie')
entry.pack()

entry1 = Entry(root,font=large_font)
entry1.insert(0, 'Nazwisko')
entry1.pack()

root.title("Obecność")
root.geometry("1024x600+50+50")

print_button = Button(root, text='Dodawanie Osoby!', command=Photo, height =3, width = 30)
print_button.pack()

print_button1 = Button(root, text='Sprawdź obecność!', command=fr, height =3, width =30)
print_button1.pack()

label = Label(root, text='Lista Obecności :',font=large_font)
label.pack()
T = Text(root, height=30, width=50)
T.pack()



root.mainloop()
=======
import cv2



# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# Load a sample picture and learn how to recognize it.
J_image = face_recognition.load_image_file("1.jpg")
J_face_encoding = face_recognition.face_encodings(J_image)[0]

# Load a sample picture and learn how to recognize it.
E_image = face_recognition.load_image_file("3.jpg")
E_face_encoding = face_recognition.face_encodings(E_image)[0]


# Load a second sample picture and learn how to recognize it.
B_image = face_recognition.load_image_file("2.jpg")
B_face_encoding = face_recognition.face_encodings(B_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    J_face_encoding,
    E_face_encoding,
    B_face_encoding
]
known_face_names = [
    "Hubert",
    "Emil",
    "Bartosz"
]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "???"

            # If a match was found in known_face_encodings, just use the first one.
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
>>>>>>> 50f4370f88f8443a5056465f2288ca8f66e17b76
