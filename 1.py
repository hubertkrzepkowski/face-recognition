from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime
import face_recognition
import os, sys
import cv2
import numpy as np
#from tinydb import TinyDB, Query
import tkinter.scrolledtext as tkscrolled
from tkinter import *
root = Tk()


nazwa=''
nazwisko = ''
recognized_Faces = set([])



def Photo():
    messagebox.showinfo("INFO", "Aby zapisać osobe wcisnij enter")
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
            face_locations = face_recognition.face_locations(frame)
            if 1 == len(face_locations):
             cv2.imwrite(".//zdjecia/"+entry.get().strip()+" "+entry1.get().strip()+" "+entryindeks.get().strip()+".jpg", frame)
             entry1.delete(0,END)
             entry.delete(0,END)
             entryindeks.delete(0,END)
             entry.insert(0, 'Imie')
             entry1.insert(0, 'Nazwisko')
             entryindeks.insert(0, 'Numer Indeksu')
             break
            else:
                messagebox.showinfo("INFO", "Nie wykryto twarzy lub wykryto wiecej niz jedna twarz - Sprobuj ponownie")

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

def fr():
        messagebox.showinfo("INFO", "Aby zakonczyc sprawdzanie obecnosci wcisnij enter")
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
                        recognized_Faces.add(name)
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
             #3   T.delete(S, END)
            if cv2.waitKey(1) & 0xFF == 13:
                currentDT = datetime.datetime.now()
                i=1
                plik = open('.//ListyObecnosci/'+entryprzedmiot.get()+" "+entrygrupa.get()+" "+(currentDT.strftime("%Y-%m-%d %H,%M"))+".txt", 'w')
                try:
                 plik.write(entryprzedmiot.get()+"\n"+entrygrupa.get()+"\n"+(currentDT.strftime("%Y-%m-%d %H:%M:%S"))+"\n")

                 for face in recognized_Faces:
                     plik.write(str(i))
                     plik.write("."+face +"\n")
                     i=i+1

                finally:
                    plik.close()
                    entryprzedmiot.delete(0,END)
                    entrygrupa.delete(0,END)
                    entryprzedmiot.insert(0, 'Przedmiot')
                    entrygrupa.insert(0, 'Grupa')
                    messagebox.showinfo("INFO", "Lista obecnosci została zapisana do pliku \""+entryprzedmiot.get()+" "+entrygrupa.get()+" "+(currentDT.strftime("%Y-%m-%d %H,%M"))+".txt\"" +" w folderze ListyObecnosci.")
                video_capture.release()
                cv2.destroyAllWindows()
                break



large_font = ('Verdana',15)



entry = Entry(root, font=large_font)
entry.insert(0, 'Imie')
entry.grid(row=0,column=1 )

entry1 = Entry(root,font=large_font)
entry1.insert(0, 'Nazwisko')
entry1.grid(row=1, column=1 )

entryindeks= Entry(root,font=large_font)
entryindeks.insert(0, 'Numer Indeksu')
entryindeks.grid(row=2, column=1)

entryprzedmiot = Entry(root,font=large_font)
entryprzedmiot.insert(0, 'Przedmiot')
entryprzedmiot.grid(row=0, column=0)

entrygrupa = Entry(root,font=large_font)
entrygrupa.insert(0, 'Grupa')
entrygrupa.grid(row=1, column=0)

root.title("Obecnosć")
root.geometry("530x300+50+50")

print_button = Button(root, text='Dodawanie Osoby!', command=Photo, height =3, width = 30)
print_button.grid(row=3, column=1)

#print_button_email = Button(root, text='email', command=send_message, height =3, width = 30)
#print_button_email.grid(row=3, column=1)

print_button1 = Button(root, text='Sprawdz obecnosć!', command=fr, height =3, width =30)
print_button1.grid(row=3, column=0)





root.mainloop()

