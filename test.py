import cv2
print(cv2.__version__)


camset1 = "nvarguscamerasrc ! nvvidconv ! video/x-raw, width=1024, height=576, format=BGRx ! videoconvert ! video/x-raw, format=BGR "
dispW=640
dispH=480
flip=2
camset2='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

 

cam = cv2.VideoCapture(0)
#cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
#cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
print(cam.isOpened())
print(cam.read())

while cam.isOpened():
   ret, frame = cam.read()

   img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)   
   cv2.imshow('Cuadro', img)

   if cv2.waitKey(1)==ord('q'):
      break

cam.release()
cv2.destroyAllWindows()
