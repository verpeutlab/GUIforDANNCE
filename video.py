#necessary python function (not using tkinter)
import cv2

#captures the video
cap = cv2.VideoCapture('/Users/ishaan/Downloads/0.mp4')
 
# if the video is opened it plays or displays an error
if (cap.isOpened()== False):
  print("Error opening video stream or file")
 
#basically allows the video to play until a frame isn't there(it ends) or a frame doesn't work 
while (cap.isOpened()):
    
    ret, frame = cap.read()
    if ret == True:
 
        
        cv2.imshow('Frame', frame)
 
        
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
 
    else:
        break
 
cap.release()

#allows you to close the program 
cv2.destroyAllWindows()
