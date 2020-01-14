import sys
import numpy as np
import cv2
import sqlite3



sys.path.append('/usr/local/lib/python2.7/site-packages')




face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)



def insertOrUpdate(Id,Name):


    conn=sqlite3.connect("FaceData.db")

    cursor = conn.cursor()
    # cmd= INSERT INTO StudentsFaces(ID,Name)Values((Id),(Name))
    cmd = "SELECT * FROM StudentsData WHERE ID = " + Id
    cursor = conn.execute(cmd)
    isRecordExist = 0
    for row in cursor:       
        isRecordExist = 1
    if isRecordExist == 1:
        conn.execute("UPDATE StudentsData SET Name = ? WHERE ID = ?",(Name,Id))
    else:
        conn.execute("INSERT INTO StudentsData(ID,Name)Values(?,?)",(Id,Name))
    conn.commit()
    conn.close()




Id = input("enter users id :")
Name = input("enter the name:")



sampleNum = 0

insertOrUpdate(Id,Name)

while True:
    # Read the frame
    ret, img = cap.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        sampleNum=sampleNum+1

        cv2.imwrite("dataSet/Users."+str(Id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img, (x,y), (x+w, y+h),(255,0,0),2)
        cv2.putText(img,"Face Detected",(x,y+h+30),cv2.FONT_HERSHEY_SIMPLEX,1,255)
        cv2.waitKey(300)
        
    # Display
    cv2.imshow("Face", img)
    # Stop if escape key is pressed
    cv2.waitKey(1)
# Release the VideoCapture object
    if(sampleNum>20):
        cap.release()
        break
