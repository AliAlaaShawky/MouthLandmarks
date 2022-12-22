import dlib
import cv2 
from math import  sqrt

camera = cv2.VideoCapture(0)
def gen():
    sampleNum=0
    detector=dlib.get_frontal_face_detector()
    path="C:/Users/xps/Desktop/test/shape_predictor_68_face_landmarks.dat"
    face_detector=dlib.shape_predictor(path)
    while True:
        _,frame=camera.read()
        if not _:
            break
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces=detector(gray)
        font = cv2.FONT_HERSHEY_DUPLEX
        for face in faces:
            x1=face.left()
            y1=face.top()
            x2=face.right()
            y2=face.bottom()
            landmarks=face_detector(gray,face)
            x5=landmarks.part(3).x
            y5=landmarks.part(3).y

            x6=landmarks.part(13).x
            y6=landmarks.part(13).y
            x7=landmarks.part(7).x
            
            y7=landmarks.part(7).y
            x8=landmarks.part(10).x
            
            y8=landmarks.part(10).y
            
           
            cv2.circle(frame,(x5,y5),3,(0,0,0),-1)
            cv2.circle(frame,(x6,y6),3,(0,0,255),-1)
            cv2.circle(frame,(x7,y7),3,(0,255,0),-1)
            cv2.circle(frame,(x8,y8),3,(255,0,0),-1)
            cv2.rectangle(frame,(x5,y5),(x2,y2),(0,255,0),3)

           # cv2.putText(frame, s, (x1 + 6, y2 - 6),font, 1.0, (255, 255, 255), 2)
        cv2.imshow("my mouth",frame)
        if cv2.waitKey(10) & 0xff ==ord('q'):
            break
        
gen()       
camera.release()
cv2.destroyAllWindows()