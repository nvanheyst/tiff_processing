#save a 16 bit TIFF file with radiometric data from a usb thermal camera

import cv2

cap = cv2.VideoCapture(“/dev/video0”)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 512)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('Y','1','6',' '))
cap.set(cv2.CAP_PROP_CONVERT_RGB, 0)

framecount=1 #adjust for more than one frame
frame_buf=[]
folder = #path

for _ in range(framecount): #setup to handle capture of multiple frames
    stream_ret, frame = cap.read()
    if stream_ret:
        cv2.imshow("image", frame)

        while true:
            if cv2.waitKey(1) == ord('q'): #hold image up until q is pressed
                break;
                
        frame_buf.append(frame)
        
cv2.destroyAllWindows()

#save images, setup for multiple frames if needed
num=0
while len(frame_buf)>0:
    cv2.imwrite(f'{folder}/cap_{num}.tiff', frame_buf.pop(0))
    num += 1
