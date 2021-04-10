import cv2
#Capture video from webcam
vid_capture = cv2.VideoCapture(0)
vid_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
vid_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
vid_cod = cv2.VideoWriter_fourcc(*'XVID')
path = "video_pred/cam_video"

for x in range (14,20):
     counter = 0
     output = cv2.VideoWriter(path+str(x)+".avi", vid_cod, 30.0, (1280, 720))
     while(True):
          # Capture each frame of webcam video
          ret,frame = vid_capture.read()
          cv2.imshow("My cam video", frame)
          output.write(frame)
          counter = counter + 1
          # Close and break the loop after pressing "x" key
          if cv2.waitKey(1) & counter == 150:
              break
x = x + 1


# close the already opened camera
vid_capture.release()
# close the already opened file
output.release()
# close the window and de-allocate any associated memory usage
cv2.destroyAllWindows()