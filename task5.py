import cv2
face__cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
capture = cv2.VideoCapture(0)
while True:
    ret,frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face__cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
     cv2.rectangle(frame,(x,y), (x+w, y+h),(0,255,0), 2)
    cv2.imshow("face detection", frame)
    if cv2.waitKey(1) == 13:
       break
capture.release()    
cv2.destroyAllWindows()