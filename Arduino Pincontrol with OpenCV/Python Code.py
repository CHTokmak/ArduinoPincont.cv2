import cv2
import serial
import time
levis = cv2.CascadeClassifier("***.xml")
webcam = cv2.VideoCapture(0)
arduino = serial.Serial("com3",9600)
while True:
    kontrol,cerceve = webcam.read()
    gri = cv2.cvtColor(cerceve,cv2.COLOR_BGR2GRAY)
    sonuc = levis.detectMultiScale(gri,1.1,4)

    for (x,y,genislik,yukseklik) in sonuc:
        cv2.putText(cerceve,"FİRE",(x,y),cv2.FONT_ITALIC,1,(255,0,0),2)
        cv2.rectangle(cerceve,(x,y),(x+genislik,y+yukseklik),(255,0,0),2)
        arduino.write(b'1')
        time.sleep(1)
    cv2.imshow("1",cerceve)
    arduino.write(b'0')
    if cv2.waitKey(10) == 27:
        break
webcam.release()
cv2.destroyAllWindows()